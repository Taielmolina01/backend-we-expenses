from database import Base
from sqlalchemy import Column, Integer, String

class UserBase(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    balance = Column(Integer, default=0)