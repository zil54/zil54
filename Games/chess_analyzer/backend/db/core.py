import os
from dotenv import load_dotenv
import psycopg

# Load variables from .env into environment
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

async def get_connection():
    return await psycopg.AsyncConnection.connect(DATABASE_URL)