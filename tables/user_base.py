from database import Base
from sqlalchemy import Column, Integer, String, Float
from pydantic import Optional, BaseModel


class UserBase(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    balance = Column(Float, default=0)

class UserUpdate(BaseModel):
    name = Optional[str] = None
    balance = Optional[float] = None