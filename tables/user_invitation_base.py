from database import Base
from sqlalchemy import Column, Integer, ForeignKey, String, Date
from datetime import datetime, timedelta, timezone

class UserInvitationBase(Base):
    __tablename__ = "invitations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    invitator_email = Column(String, ForeignKey("users.email"))
    guest_email = Column(String, ForeignKey("users.email"))
    id_group = Column(Integer, ForeignKey("groups.id"))
    send_date = Column(Date, default=lambda: datetime.now(timezone.utc).date())
    expire_date = Column(Date, default=lambda: (datetime.now(timezone.utc) + timedelta(days=7)).date())
