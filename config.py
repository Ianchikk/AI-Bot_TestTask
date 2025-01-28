import os
from dotenv import load_dotenv

# Încarcă variabilele de mediu din fișierul .env
load_dotenv()

class Config:
    # Token-ul botului Telegram
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    # Cheia API OpenAI
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # URL-ul de conectare la baza de date PostgreSQL
    DATABASE_URL = os.getenv("DATABASE_URL")