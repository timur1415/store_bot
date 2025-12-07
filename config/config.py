import os
from dotenv import load_dotenv

load_dotenv()   

TOKEN = os.getenv('TOKEN')
TELEGRAM_WEBHOOK_PATH = os.getenv("TELEGRAM_WEBHOOK_PATH")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
SECRET_TOKEN = os.getenv("SECRET_TOKEN", '123')
GPT_TOKEN = os.getenv("CHAT_GPT_TOKEN")
CP_PUBLIC_ID = os.getenv('CP_PUBLIC_ID')