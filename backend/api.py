import os
from dotenv import load_dotenv
from supabase import create_client, Client
from fastapi import FastAPI

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

app = FastAPI()

@app.get("/api/projects")
async def get_projects():
    # Запрос через API ключ к таблице projects
    response = supabase.table("projects").select("*").execute()
    return response.data
