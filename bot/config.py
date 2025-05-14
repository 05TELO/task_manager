import os

from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "")
TG_BOT_SECRET = os.getenv("TELEGRAM_BOT_TOKEN", "")
