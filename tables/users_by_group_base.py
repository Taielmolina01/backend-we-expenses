from database import Base
from sqlalchemy import Column, Integer, ForeignKey

class UserInGroupBase(Base):
    __tablename__ = "users_by_group"

    group_id = Column(Integer, ForeignKey("groups.group_id"))
#    user_id = Column(Integer, ForeignKey("users.user_id"))
    user_mail = Column(Integer, ForeignKey("users.mail"))