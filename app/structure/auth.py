#imports
from pydantic import BaseModel, EmailStr


class login_syntax_request(BaseModel):
    email: EmailStr
    password: str

