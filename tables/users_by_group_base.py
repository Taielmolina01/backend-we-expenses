from database import Base
from sqlalchemy import Column, Integer

class GroupBase(Base):
    __tablename__ = "users_by_group"

    group_id = Column(Integer, ForeignKey())
    user_id = Column(Integer, ForeignKey())