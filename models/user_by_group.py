from pydantic import BaseModel
from typing import Optional

class UserByGroupModel(BaseModel):
    group_id: int
    user_email: str

class UserByGroupUpdate(BaseModel):
    group_id: Optional[int]
    user_email: Optional[str]