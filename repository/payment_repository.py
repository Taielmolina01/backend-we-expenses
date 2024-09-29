from sqlalchemy.orm import Session
from tables.payment_base import PaymentBase


class PaymentRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_payment(self, payment: PaymentBase) -> PaymentBase:
        self.db.add(payment)
        self.db.commit()
        self.db.refresh(payment)
        return payment

    def get_payment(self, payment_id: int) -> PaymentBase:
        return self.db.query(PaymentBase).filter(PaymentBase.payment_id == payment_id).first()
    
    def get_payments_by_group(self, group_id: int) -> list[PaymentBase]:
        return self.db.query(PaymentBase).filter(PaymentBase.group_id == group_id).all()

    def get_payments_by_user(self, user_id: int) -> list[PaymentBase]:
        return self.db.query(PaymentBase).filter(PaymentBase.payer_id == user_id).all()
    
    def get_payments_by_user_and_group(self, user_id: int, group_id: int) -> list[PaymentBase]:
        return self.db.query(PaymentBase).filter(PaymentBase.payer_id == user_id and PaymentBase.group_id == group_id).all()

    def update_payment(self, payment: PaymentBase) -> PaymentBase:
        self.db.commit()
        self.db.refresh(payment)
        return payment
    
    def delete_payment(self, payment: PaymentBase) -> bool:
        self.db.delete(payment)
        self.db.commit()
        return True