from fastapi import APIRouter, Depends, HTTPException, status
from database import get_database
from sqlalchemy.orm import Session
from models.user import UserModel, UserUpdate
from service.user_service import UserService
from service.exceptions.users_exceptions import *
from controller.login_controller import get_password_hash

router = APIRouter()


@router.post("/users")
async def create_user(user: UserModel, 
                      db: Session = Depends(get_database)):
    try:
        new_user = UserModel(email=user.email,
                            name=user.name,
                            balance=user.balance,
                            password=get_password_hash(user.password))
        return UserService(db).create_user(new_user)
    except UserAlreadyRegistered as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)
    except UserWithoutName as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)
    
@router.get("/users")
async def get_users(db: Session = Depends(get_database)):
    return UserService(db).get_users() 

@router.get("/users/{user_email}")
async def get_user(user_email: str,
                   db: Session = Depends(get_database)):
    try:
        return UserService(db).get_user(user_email)
    except UserNotRegistered as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)        

@router.put("/users/{user_email}")
async def update_user(user_email: str,
                      user_update: UserUpdate,
                      db: Session = Depends(get_database)):
    try:
        return UserService(db).update_user(user_email, user_update)
    except UserNotRegistered as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)
    
@router.delete("/users/{user_email}")
async def delete_user(user_email: str, 
                      db: Session = Depends(get_database)):
    try:
        return UserService(db).delete_user(user_email)
    except UserNotRegistered as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)