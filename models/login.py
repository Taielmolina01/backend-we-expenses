from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str or None = None

class UserLoginModel(BaseModel):
    email: str
    password: str
