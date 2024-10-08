from database import Base
from sqlalchemy import Column, Integer, String, Float
from pydantic import Optional, BaseModel


class UserBase(Base):
    __tablename__ = "users"

#    user_id = Column(Integer, primary_key=True, autoincrement=True)
    mail = Column(Integer, primary_key=True)
    name = Column(String)
    balance = Column(Float, default=0)
    password = Column(String)

class UserUpdate(BaseModel):
    name = Optional[str] = None
    balance = Optional[float] = None