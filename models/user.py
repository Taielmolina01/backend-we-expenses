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
    name: Optional[str] = None
    balance: Optional[float] = None

    class Config:
        orm_mode = True 