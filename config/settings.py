import os
from dotenv import load_dotenv
import pydantic_settings

load_dotenv()


class Settings(pydantic_settings.BaseSettings):
    db_name: str = os.getenv('DB_NAME')
    timeout: int = os.getenv('TIMEOUT')
    max_workers: int = os.getenv('MAX_WORKERS')
    password: str = os.getenv('PASSWORD')
    user: str = os.getenv('USER')
    host: str = os.getenv('HOST')
    port: str = os.getenv('PORT')

    @property
    def postgres_dsn(self):
        return f'postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}'

    @property
    def sqlite_dsn(self):
        return f'sqlite:///../dbdir/{self.db_name}.db'

    @property
    def mysql_dsn(self):
        return f'mysql+pymysql://{self.user}:{self.password}@{self.host}/{self.db_name}'


settings = Settings()
