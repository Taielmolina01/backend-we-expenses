from fastapi import APIRouter, Depends, HTTPException, status, Query
from database import get_database
from sqlalchemy.orm import Session
from tables.user_base import UserBase, UserUpdate
from service.user_service import UserService
from service.exceptions.users_exceptions import *
from service.users_by_groups_service import UserByGroupService

router = APIRouter()

@router.post("/users")
async def create_user(user: UserBase, 
                      db: Session = Depends(get_database)):
    try:
        return UserService(db).create_user(user)
    except UserAlreadyRegistered as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)
    except UserWithoutName as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)
    
@router.get("/users")
async def get_users(db: Session = Depends(get_database)):
    return UserService(db).get_users()

@router.get("/users/{user_id}")
async def get_user(user_id: int,
                   db: Session = Depends(get_database)):
    try:
        return UserService(db).get_user(user_id)
    except UserNotRegistered as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)        

@router.put("/users/{user_id}")
async def update_user(user_id: int,
                      user_update: UserUpdate,
                      db: Session = Depends(get_database)):
    try:
        return UserService(db).update_user(user_id)
    except UserNotRegistered as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)
    
@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_database)):
    try:
        return UserService(db).delete_user(user_id)
    except UserNotRegistered as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)