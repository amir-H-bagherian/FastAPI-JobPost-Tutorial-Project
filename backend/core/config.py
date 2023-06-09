import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(env_path)

class Settings:
    PROJECT_NAME: str = 'Job Board'
    PROJECT_VERSION: str = '1.0.0'
    
    POSTGRES_USER: str = os.environ['POSTGRES_USER']
    POSTGRES_PASSWORD: str = os.environ['POSTGRES_PASSWORD']
    POSTGRES_SERVER: str = os.environ['POSTGRES_SERVER']
    POSTGRES_PORT: str = os.environ['POSTGRES_PORT']
    POSTGRES_DB: str = os.environ['POSTGRES_DB']
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    
    
settings = Settings()