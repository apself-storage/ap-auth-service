#imports
from fastapi import FastAPI
from app.routers.route_auth import route_auth

app = FastAPI() # Initiate instance

app.include_router(route_auth, prefix="/auth")



