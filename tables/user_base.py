from database import Base
from sqlalchemy import Column, String, Float, Boolean, DateTime, ForeignKey
import datetime

class UserBase(Base):
    __tablename__ = "users"

    email = Column(String, primary_key=True, nullable=False)
    name = Column(String)
    balance = Column(Float, default=0)
    password = Column(String, nullable=False)

class ToeknTable(Base):
    __tablename__ = "token"
    user_email = Column(String, ForeignKey("users.email"))
    access_toke = Column(String(450), primary_key=True)
    refresh_toke = Column(String(450),nullable=False)
    status = Column(Boolean)
    created_date = Column(DateTime, default=datetime.datetime.now)