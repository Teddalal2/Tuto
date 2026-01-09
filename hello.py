import os
from dotenv import load_dotenv

# Read from environment
api_key = os.environ.get("API_KEY")
database = os.environ.get("DATABASE_URL")
print(f"API Key: {api_key}")


load_dotenv()
db_password = os.getenv("DB_PASSWORD")
print(f"Database Password: {db_password}")
print("Hello, World!")





