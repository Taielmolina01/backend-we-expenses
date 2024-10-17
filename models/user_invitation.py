from pydantic import BaseModel
from typing import Optional
from datetime import date

class UserInvitationModel(BaseModel):
    invitator_email: str
    guest_email: str
    id_group: int
    send_date: date
    expire_date: date

class UserInvitationUPdate(BaseModel):
    invitator_email: Optional[str] = None
    guest_email: Optional[str] = None
    id_group: Optional[int] = None
    send_date: Optional[date] = None
    expire_date: Optional[date] = None