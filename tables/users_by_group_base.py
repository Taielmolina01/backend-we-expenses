from database import Base
from sqlalchemy import Column, Integer, ForeignKey, String
from pydantic import BaseModel

class UserInGroupBase(Base):
    __tablename__ = "users_by_group"

    group_id = Column(Integer, ForeignKey("groups.group_id"))
    user_email = Column(String, ForeignKey("users.email"))