#imports
from pydantic_settings import BaseSettings, SettingsConfigDict

class db_settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env") #retrieves password from .env file

    db_host: str = "127.0.0.1"
    db_port: int = 5432
    db_name: str = "ap_auth"
    db_user: str = "ap_auth_user"
    db_password: str



