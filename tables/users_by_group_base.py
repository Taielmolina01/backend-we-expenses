from database import Base
from sqlalchemy import Column, Integer, ForeignKey

class GroupBase(Base):
    __tablename__ = "users_by_group"

    group_id = Column(Integer, ForeignKey("groups.group_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))