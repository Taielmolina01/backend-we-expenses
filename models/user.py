from pydantic import BaseModel
from typing import Optional
import datetime

class UserModel(BaseModel):
    email: str
    name: str
    balance: float
    password: str

    class Config:
        orm_mode = True 

class UserUpdate(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None
    balance: Optional[float] = None
    password: Optional[str] = None

    class Config:
        orm_mode = True 

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

class changepassword(BaseModel):
    email: str
    old_password: str
    new_password: str

class TokenCreate(BaseModel):
    user_id: str
    access_token: str
    refresh_token: str
    status: bool
    created_date: datetime.datetime