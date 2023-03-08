import os

from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    database_url: str = Field(..., env='DATABASE_URL')
    
settings = Settings()