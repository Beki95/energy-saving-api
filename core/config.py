import os

from dotenv import load_dotenv
from pydantic import BaseSettings

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path)


class Settings(BaseSettings):
    DATABASE_URL = os.getenv('DATABASE_URL')
    REDIS_URL = os.getenv('REDIS_URL', default='redis://localhost')


settings = Settings()
