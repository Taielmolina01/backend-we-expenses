from databases import Base
from sqlalchemy import Column, Integer, String

class GroupBase(Base):
    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)