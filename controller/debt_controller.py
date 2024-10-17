from fastapi import APIRouter, Depends, HTTPException, status, Query
from service.debt_service import *
from database import get_database
from sqlalchemy.orm import Session
from models.debt import DebtModel, DebtUpdate
from service.exceptions.debts_exceptions import *

router = APIRouter()

@router.post("/debts")
async def create_debt(debt: DebtModel,
                      db: Session = Depends(get_database)) :
    try:
        return DebtService(db).create_debt(debt)
    except DebtAlreadyRegistered as e:
        raise HTTPException(status_code=HTTPException.HTTP_400_BAD_REQUEST, detail=e.message)
    except DebtIsInvalid as e:
        raise HTTPException(status_code=HTTPException.HTTP_400_BAD_REQUEST, detail=e.message)
    
@router.get("/debts/{debt_id}")
async def get_debt(debt_id: int,
                      db: Session = Depends(get_database)):
    try:
        return DebtService(db).get_debt(debt_id)
    except DebtNotRegistered as e:
        raise HTTPException(status_code=HTTPException.HTTP_404_NOT_FOUND, detail=e.message)
    
@router.put("/debts/{debt_id}")
async def update_debt(debt_id: int,
                      debt_update: DebtUpdate,
                      db: Session = Depends(get_database)):
    try:
        return DebtService(db).update_debt(debt_id, debt_update)
    except DebtNotRegistered as e:
        raise HTTPException(status_code=HTTPException.HTTP_404_NOT_FOUND, detail=e.message)
    except DebtIsInvalid as e:
        raise HTTPException(status_code=HTTPException.HTTP_400_BAD_REQUEST, detail=e.message)


@router.delete("/debts")
async def delete_debt(debt: DebtModel,
                      db: Session = Depends(get_database)):
    try:
        return DebtService(db).delete_debt(debt)
    except DebtNotRegistered as e:
        raise HTTPException(status_code=HTTPException.HTTP_404_NOT_FOUND, detail=e.message)