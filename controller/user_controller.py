from fastapi import APIRouter, Depends, HTTPException, status, Query
from database import get_database
from sqlalchemy.orm import Session
from models.user_base import UserModel, UserUpdate
from service.user_service import UserService
from service.exceptions.users_exceptions import *
from service.users_by_groups_service import UserByGroupService
from passlib.context import CryptContext

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify(plain_password: str, hashed_password: str):     
  return pwd_context.verify(plain_password, hashed_password)

@router.post("/users")
async def create_user(user: UserModel, 
                      db: Session = Depends(get_database)):
    try:
        new_user = UserModel(email=user.email,
                            name=user.name,
                            balance=user.balance,
                            password=hash_password(user.password))
        return UserService(db).create_user(new_user)
    except UserAlreadyRegistered as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)
    except UserWithoutName as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)
    
@router.get("/users")
async def get_users(db: Session = Depends(get_database)):
    return UserService(db).get_users()

@router.post('/login')
def login(user: UserModel, 
          db: Session = Depends(get_database)) -> bool:
    try:
        registered_user = UserService.get_user(user.email)
        if verify(user.password, registered_user.password):
            return True
        return False
    except UserNotRegistered as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)        
       

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