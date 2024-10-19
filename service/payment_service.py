from sqlalchemy.orm import Session
from repository.payment_repository import PaymentRepository
from models.payment import PaymentModel, PaymentUpdate
from tables.payment_base import PaymentBase
from service.exceptions.payments_exceptions import *
from service.users_by_groups_service import UserByGroupService
from service.debt_service import DebtService
from models.debt import DebtModel, DebtUpdate

def create_payment_from_model(payment_model: PaymentModel) -> PaymentBase:
    return PaymentBase(
        group_id = payment_model.group_id,
        payer_email = payment_model.payer_email,
        date = payment_model.date,
        category = payment_model.category,
        amount = payment_model.amount
    )

class PaymentService:

    def __init__(self,
                 db: Session):
        self.payment_repository = PaymentRepository(db)
        self.user_by_group = UserByGroupService(db)
        self.debt_service = DebtService(db)

    def create_payment(self,
                       payment: PaymentModel,
                       percentages: dict[str, float]) -> PaymentBase:
        users = self.user_by_group.get_users_by_group(payment.group_id)
        if len(percentages) > len(users):
            raise PaymentWithMoreDistributionsThanGroupUsers()
        if len(users) > len(percentages):
            raise PaymentWithLessDistributionsThanGroupUsers()
        for u in users:
            self.debt_service.create_debt(DebtModel(payment_id=payment.payment_id, 
                                                    group_id=payment.group_id, 
                                                    debtor_email=u.user_email, 
                                                    creditor_email=payment.payer_email, 
                                                    percentage=percentages[u.user_email]))
        return self.payment_repository.create_payment(create_payment_from_model(payment))

        
    def get_payment(self,
                    payment_id: int) -> PaymentBase:
        return self.payment_repository.get_payment(payment_id)
    
    def get_payments_by_group(self,
                              group_id: int) -> list[PaymentBase]:
        return self.payment_repository.get_payments_by_group(group_id)

    def get_payments_by_user(self,
                              user_id: int) -> list[PaymentBase]:
        return self.payment_repository.get_payments_by_user(user_id)
    
    def get_payments_by_user_and_group(self,
                              user_id: int,
                              group_id: int) -> list[PaymentBase]:
        return self.payment_repository.get_payments_by_user_and_group(user_id, group_id)
    
    def update_payment(self,
                       payment_id: int,
                       payment_update: PaymentUpdate,
                       percentages: list[int]) -> PaymentBase:
        # agregar la logica de la deuda a cada usuario del grupo
        registered_payment = self.get_payment(payment_id)
        if not registered_payment:
            raise PaymentNotRegistered()
        new_payment = create_payment_from_model(payment_update)
        users = self.user_by_group.get_users_by_group(new_payment.group_id)
        if len(percentages) > len(users):
            raise PaymentWithMoreDistributionsThanGroupUsers()
        if len(users) > len(percentages):
            raise PaymentWithLessDistributionsThanGroupUsers()
        for u in users:
            self.debt_service.update_debt(DebtUpdate(payment_id=new_payment.payment_id, 
                                                    group_id=new_payment.group_id, 
                                                    debtor_email=u.user_email, 
                                                    creditor_email=new_payment.payer_email, 
                                                    percentage=percentages[u.user_email]))
        return self.payment_repository.update_payment(new_payment)

        

    def delete_payment(self,
                       payment: PaymentModel) -> bool:
        registered_payment = self.get_payment(payment.payment_id)
        if not registered_payment:
            raise PaymentNotRegistered()
        debts = self.debt_service.get_debts_by_payment_id(payment.payment_id)
        for d in debts:
            self.debt_service.delete_debt(d)
        return self.payment_repository.delete_payment(payment)