from fastapi import APIRouter, Depends, HTTPException, status, Query
from database import get_database
from sqlalchemy.orm import Session
from tables.user_base import UserBase, UserUpdate
from service.user_service import UserService
from service.exceptions import *

router = APIRouter()

# post
# put
# get
# delete

@router.post("/users")
async def create_user(user: UserBase, 
                      db: Session = Depends(get_database)):

@router.get("/users")
async def get_users(db: Session = Depends(get_database)):
    

@router.get("/users/{user_id}")
async def get_user(user_id: int,
                   db: Session = Depends(get_database)):
    try:
        user = UserService.get_user(user_id)
    except UserNotRegistered as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)        

@router.put("/users/{user_id}")
async def update_user(user_id: int,
                      user_update: UserUpdate,
                      db: Session = Depends(get_database)):
    try:
        user = UserService.get_user(user_id)
    except UserNotRegistered as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)
    
@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_database)):
    try:
        user = UserService.get_user(user_id)
    except UserNotRegistered as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)

