from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from models.user import UserLoginModel
from sqlalchemy.orm import Session
from database import get_database
from service.user_service import UserService
from service.exceptions.users_exceptions import UserNotRegistered

router = APIRouter()

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.put("/login")
async def login(user: UserLoginModel,
                 db: Session = Depends(get_database)):
    try:
        registered_user = UserService(db).get_user(user.email)
    except UserNotRegistered as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)        