import os
from dotenv import load_dotenv
import pydantic_settings

load_dotenv()


class Settings(pydantic_settings.BaseSettings):
    db_name: str = os.getenv('DB_NAME')
    db_type: str = os.getenv('DB_TYPE')
    db_path: str = os.getenv('DB_PATH')
    url: str = os.getenv('URL')
    timeout: int = os.getenv('TIMEOUT')
    max_workers: int = os.getenv('MAX_WORKERS')
    password: str = os.getenv('PASSWORD')
    user: str = os.getenv('USER')
    host: str = os.getenv('HOST')
    port: str = os.getenv('PORT')


settings = Settings()
