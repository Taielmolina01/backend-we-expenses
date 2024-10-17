from database import Base
from sqlalchemy import Column, Integer, String, Float
from pydantic import Optional, BaseModel


class UserBase(Base):
    __tablename__ = "users"

    email = Column(String, primary_key=True, nullable=False)
    name = Column(String)
    balance = Column(Float, default=0)
    password = Column(String, nullable=False)

class UserUpdate(BaseModel):
    name: Optional[str] = None
    balance: Optional[float] = None
    password: Optional[str] = None