from sqlalchemy.orm import Session
from repository.payment_repository import PaymentRepository
from tables.payment_base import PaymentBase, PaymentUpdate

class PaymentService:

    def __init__(self,
                 db: Session):
        self.payment_repository = PaymentRepository(db)


    def create_payment(self,
                       payment: PaymentBase) -> PaymentBase:
        return self.payment_repository.create_payment(payment)
        
    def get_payment(self,
                    payment_id: int) -> PaymentBase:
        return self.payment_repository.get_payment(payment_id)
    
    def get_payments_by_group(self,
                              group_id: int):
        return self.payment_repository.get_payments_by_group(group_id)

    def get_payments_by_user(self,
                              user_id: int):
        return self.payment_repository.get_payments_by_user(user_id)
    
    def get_payments_by_user_and_group(self,
                              user_id: int,
                              group_id: int):
        return self.payment_repository.get_payments_by_user_and_group(user_id, group_id)
    
    def update_payment(self,
                       payment_id: int,
                       payment_update: PaymentUpdate) -> PaymentBase:
        return self.payment_repository.update_payment(payment_id, payment_update)
        

    def delete_payment(self,
                       payment: PaymentBase) -> PaymentBase:
        return self.payment_repository.delete_payment(payment)