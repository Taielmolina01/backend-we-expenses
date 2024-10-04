from fastapi import APIRouter, Depends, HTTPException, status, Query
from service.group_service import *
from database import get_database
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/groups")
async def create_group(group: GroupBase,
                       db: Session = Depends(get_database)):
    try:
        return GroupService(db).create_group(group)
    except GroupAlreadyRegistered as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)
    
@router.get("/groups")
async def get_groups(db: Session = Depends(get_database)):
    return GroupService(db).get_groups

@router.get("/groups/{group_id}")
async def get_group(group_id: int,
                    db: Session = Depends(get_database)):
    try:
        return GroupService(db).get_group(group_id)
    except GroupNotRegistered as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)

@router.put("/groups/{group_id}")
async def update_group(group_id: int,
                       group_update: GroupUpdate,
                       db: Session = Depends(get_database)):
    try:
        return GroupService(db).update_group(group_id, group_update)
    except GroupNotRegistered as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)

@router.delete("/groups/{group_id}")
async def delete_group(group: GroupBase,
                       db: Session = Depends(get_database)):
    try:
        return GroupService(db).delete_group(group)
    except GroupNotRegistered as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)