from databases import Base
from sqlalchemy import Column, String, Float

class UserBase(Base):
    __tablename__ = "users"

    email = Column(String, primary_key=True, nullable=False)
    name = Column(String)
    balance = Column(Float, default=0)
    password = Column(String, nullable=False)
