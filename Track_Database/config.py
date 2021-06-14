import os
from dotenv import load_dotenv

load_dotenv()

# данные для подключения к PostgreSQL
LOGIN = str(os.getenv("LOGIN"))
PASSWORD = str(os.getenv("PASSWORD"))
HOST = str(os.getenv("HOST"))
DB_NAME = str(os.getenv("DB_NAME"))
