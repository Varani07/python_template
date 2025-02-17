import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv("DEBUG", "False").lower() in ["true", "1", "yes"]
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///app.db")

SECRET_KEY = os.getenv("SECRET_KEY", "sua-chave-secreta-aqui")

FLASK_SETTINGS = {
    "DEBUG": DEBUG,
    "ENV": ENVIRONMENT,
    "SECRET_KEY": SECRET_KEY,
    "SQLALCHEMY_DATABASE_URI": DATABASE_URL
}