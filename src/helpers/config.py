from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os

# Load environment variables explicitly
load_dotenv()

class Settings(BaseSettings):

    APP_NAME : str
    APP_VERSION : str
    OPENAI_KEY : str

    FILE_ALLOWED_TYPES : list
    FILE_ALLOWED_SIZE : int
    FILE_DEFAULT_CHUNK_SIZE : int

    class config:
        env_file = ".env"

def get_settings():
    return Settings()
