from pydantic import BaseModel
from typing import Optional

class UserModel(BaseModel):
    email: str
    name: str
    balance: float
    password: str

class UserUpdate(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None
    balance: Optional[float] = None
    password: Optional[str] = None