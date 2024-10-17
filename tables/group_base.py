from database import Base
from sqlalchemy import Column, Integer, String
from typing import Optional
from pydantic import BaseModel

class GroupBase(Base):
    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


