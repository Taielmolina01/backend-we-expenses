from fastapi import APIRouter, Depends, HTTPException, status, Query
from models.payment import PaymentModel, PaymentUpdate
from database import get_database
from sqlalchemy.orm import Session
from service.payment_service import PaymentService

router = APIRouter()

@router.post("/payments")
async def create_payment(payment: PaymentModel,
                         percentages: list[int],
                       db: Session = Depends(get_database)):
        return PaymentService(db).create_payment(payment, percentages)
        
@router.get("/payments/{payment_id}")
async def get_payment(payment_id: int,
                    db: Session = Depends(get_database)):
        return PaymentService(db).get_payment(payment_id)

@router.get("/groups/{group_id}/payments")
async def get_payments_by_group(group_id: int,
                              db: Session = Depends(get_database)):
        return PaymentService(db).get_payments_by_group(group_id)

@router.get("/users/{user_email}/payments")
async def get_payments_by_user(user_email: str,
                              db: Session = Depends(get_database)):
        return PaymentService(db).get_payments_by_user(user_email)
    
@router.get("/groups/{group_id}/users/{user_email}/payments")
async def get_payments_by_user_and_group(user_email: str,
                              group_id: int,
                              db: Session = Depends(get_database)):
        return PaymentService(db).get_payments_by_user_and_group(user_email, group_id)
    
@router.put("/payments/{payment_id}")
async def update_payment(payment_id: int,
                       payment_update: PaymentUpdate,
                       percentages: list[int],
                       db: Session = Depends(get_database)):
        return PaymentService(db).update_payment(payment_id, payment_update, percentages)
        
@router.delete("/payments")
async def delete_payment(payment: PaymentModel,
                       db: Session = Depends(get_database)):
        return PaymentService(db).delete_payment(payment)