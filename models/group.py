from pydantic import BaseModel
from typing import Optional

class GroupModel(BaseModel):
    name: str

    class Config:
        orm_mode = True 

class GroupUpdate(BaseModel):
    name: Optional[str] = None

    class Config:
        orm_mode = True 
