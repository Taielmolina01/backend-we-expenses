from sqlalchemy.orm import Session
from repository.user_invitation_repository import UserInvitationRepository
from tables.user_invitation_base import UserInvitationBase
from models.user_invitation import UserInvitationModel
from service.user_service import UserService
from service.exceptions.users_exceptions import UserNotRegistered

class InvitationService:

    def __init__(self,
                 db: Session):
        self.invitation_repository = UserInvitationRepository(db)
        self.user_service = UserService(db)

    def create_invitation(self,
                          invitation: UserInvitationModel) -> UserInvitationBase:
        registered_invitator, registered_guest = self.user_service.get_user(invitation.invitator_email), self.user_service.get_user(invitation.guest_email)
        if not registered_invitator:
            raise UserNotRegistered(invitation.invitator_email)
        if not registered_guest:
            raise UserNotRegistered(invitation.guest_email)
        return self.invitation_repository.create_invitation(invitation)
        
        
    def get_invitations_by_guest(self,
                                user_email: str) -> list[UserInvitationBase]:
        registered_user = self.user_service.get_user(user_email)
        if not registered_user:
            raise UserNotRegistered(user_email)
        return self.invitation_repository.get_invitations_by_guest(user_email)
