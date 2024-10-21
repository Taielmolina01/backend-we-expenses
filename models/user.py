from pydantic import BaseModel
from typing import Optional

class UserModel(BaseModel):
    email: str
    name: str
    balance: Optional[float] = 0
    password: str

    class Config:
        orm_mode = True 

class UserResponseModel(BaseModel):
    email: str
    name: str
    balance: Optional[float] = 0

class UserUpdate(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None
    balance: Optional[float] = None
    password: Optional[str] = None

    class Config:
        orm_mode = True 