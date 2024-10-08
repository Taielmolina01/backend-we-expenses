from fastapi import APIRouter, Depends, HTTPException, status, Query
from database import get_database
from sqlalchemy.orm import Session
from service.users_by_groups_service import UsersByGroupService
from service.exceptions.groups_exceptions import GroupNotRegistered
from service.exceptions.users_exceptions import UserNotRegistered
from service.exceptions.users_by_groups_exceptions import UserNotRegisteredInGroup
from tables.users_by_group_base import UserInGroupBase

router = APIRouter()

@router.post("/groups/{group_id}/users/{user_id}")
async def add_user_in_group(user_in_group: UserInGroupBase,
                            db: Session = Depends(get_database)):
        try:
            return UsersByGroupService(db).add_user_in_group(user_in_group)
        except GroupNotRegistered as e:
              raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)
        except UserNotRegistered as e:
              raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)
        
@router.get("/groups/{group_id}/users")
async def get_users_by_group(group_id: int,
                             db: Session = Depends(get_database)):
        try:
            return UsersByGroupService(db).get_users_by_group(group_id)
        except GroupNotRegistered as e:
              raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)
        
@router.get("/users/{user_id}/groups")
async def get_groups_by_user(user_id: int, 
                             db: Session =  Depends(get_database)):
        try:
            return UsersByGroupService(db).get_groups_by_user(user_id)
        except UserNotRegistered as e:
              raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)

@router.delete("/groups/{group_id}/users/{user_id}")
async def delete_user_in_group(user_in_group: UserInGroupBase,
                            db: Session = Depends(get_database)):
        try:
            return UsersByGroupService(db).delete_user_in_group(user_in_group)
        except GroupNotRegistered as e:
              raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)
        except UserNotRegistered as e:
              raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)
        except UserNotRegisteredInGroup as e:
              raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)