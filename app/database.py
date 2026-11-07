#imports
from sqlalchemy import create_engine, URL
from app.config import db_settings


settings = db_settings()  # Create an instance of the db_settings class to access the database settings
db_connection = URL.create(
    drivername="postgresql+psycopg",
    host = settings.db_host,
    port = settings.db_port,
    database = settings.db_name,
    username = settings.db_user,
    password = settings.db_password
)

engine_start = create_engine(
    db_connection,
    pool_pre_ping=True,
)
