from sqlalchemy.orm import Session
from tables.user_invitation_base import UserInvitationBase
from models.user_invitation import UserInvitationModel

class UserInvitationRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_invitation(self, 
                          invitation: UserInvitationModel) -> UserInvitationBase:
        self.db.add(invitation)
        self.db.commit()
        self.db.refresh(invitation)
        return invitation

    def get_invitations_by_guest(self, 
                                 guest_email: str) -> list[UserInvitationBase]:
        return self.db.query(UserInvitationBase).filter(UserInvitationBase.guest_email == guest_email).all()