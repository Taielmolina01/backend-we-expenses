from fastapi import APIRouter, Depends, HTTPException, status, Query
from service.group_service import *
from database import get_database
from sqlalchemy.orm import Session
from models.group import GroupModel, GroupUpdate
from controller.user_controller import get_current_active_user
from models.user import UserModel
from controller.users_by_groups_controller import add_user_in_group
from models.user_by_group import UserByGroupModel

router = APIRouter()

@router.post("/groups")
async def create_group(group: GroupModel,
                       db: Session = Depends(get_database),
                       current_user: UserModel = Depends(get_current_active_user)):
    group = GroupService(db).create_group(group)
    add_user_in_group(UserByGroupModel(
        group_id=group.group_id,
        user_email=current_user.email
    ))
    return group 
    
@router.get("/groups")
async def get_groups(db: Session = Depends(get_database),
                     current_user: UserModel = Depends(get_current_active_user)):
    return GroupService(db).get_groups()

@router.get("/groups/{group_id}")
async def get_group(group_id: int,
                    db: Session = Depends(get_database),
                    current_user: UserModel = Depends(get_current_active_user)):
    try:
        return GroupService(db).get_group(group_id)
    except GroupNotRegistered as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)

@router.put("/groups/{group_id}")
async def update_group(group_id: int,
                       group_update: GroupUpdate,
                       db: Session = Depends(get_database),
                       current_user: UserModel = Depends(get_current_active_user)):
    try:
        return GroupService(db).update_group(group_id, group_update)
    except GroupNotRegistered as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)

@router.delete("/groups/{group_id}")
async def delete_group(group: GroupModel,
                       db: Session = Depends(get_database),
                       current_user: UserModel = Depends(get_current_active_user)):
    try:
        return GroupService(db).delete_group(group)
    except GroupNotRegistered as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)