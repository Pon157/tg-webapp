import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv() # Загружаем переменные из .env

app = FastAPI()

# Разрешаем запросы от фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db_connection():
    return psycopg2.connect(os.getenv("DATABASE_URL"))

@app.get("/api/projects")
def get_projects():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    # Сортировка по score от большего к меньшему
    cur.execute("SELECT * FROM projects ORDER BY score DESC")
    projects = cur.fetchall()
    cur.close()
    conn.close()
    return projects
