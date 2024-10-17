from fastapi import APIRouter, Depends, HTTPException, status
from database import get_database
from sqlalchemy.orm import Session
from models.user_invitation import UserInvitationModel
from service.exceptions.users_exceptions import *
from service.users_by_groups_service import UserInvitationService

router = APIRouter()

@router.post("/invitations")
async def create_invitation(invitation: UserInvitationModel,
                            db: Session = Depends(get_database)):
    try: 
        return UserInvitationService(db).create_invitation(invitation)
    except UserNotRegistered as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)
    
@router.get("/invitations/{guest_email}")
async def get_invitations_by_guest(guest_email: str, 
                                   db: Session = Depends(get_database)):
    try:
        return UserInvitationService(db).get_invitations_by_guest(guest_email)
    except UserNotRegistered as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)
