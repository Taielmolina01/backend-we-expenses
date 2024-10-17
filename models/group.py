from pydantic import BaseModel, Optional

class GroupModel(BaseModel):
    name: str

class GroupUpdate(BaseModel):
    name: Optional[str] = None
