import os
from dotenv import load_dotenv
from supabase import create_client, Client
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

# Инициализация Supabase
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

app = FastAPI()

# Разрешаем запросы с фронтенда (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/projects")
async def get_projects():
    try:
        # Запрос к таблице через API SDK
        response = supabase.table("projects").select("*").execute()
        return response.data
    except Exception as e:
        return {"error": str(e)}
