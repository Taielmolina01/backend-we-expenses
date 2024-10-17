from pydantic import BaseModel
from typing import Optional

class GroupModel(BaseModel):
    name: str

class GroupUpdate(BaseModel):
    name: Optional[str] = None
