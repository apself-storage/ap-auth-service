#imports
from fastapi import APIRouter
from app.structure.auth import login_syntax_request

route_auth = APIRouter()

@route_auth.post("/login")
def login(request: login_syntax_request):
    return{
        "message": "ok"
    }
