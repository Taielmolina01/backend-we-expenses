from pydantic import ModelBase, Optional

class UserModel(ModelBase):
    email: str
    name: str
    balance: float
    password: str

class UserUpdate(ModelBase):
    email: Optional[str] = None
    name: Optional[str] = None
    balance: Optional[float] = None
    password: Optional[str] = None