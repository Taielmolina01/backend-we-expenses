from databases import Base
from sqlalchemy import Column, Integer, ForeignKey, String

class UserInGroupBase(Base):
    __tablename__ = "users_by_group"

    group_id = Column(Integer, ForeignKey("groups.group_id"), primary_key=True)
    user_email = Column(String, ForeignKey("users.email"), primary_key=True)