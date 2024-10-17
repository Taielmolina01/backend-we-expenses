from sqlalchemy.orm import Session
from tables.debt_base import DebtBase
from models.debt import DebtModel, DebtUpdate
from repository.debt_repository import DebtRepository
from service.exceptions.debts_exceptions import *

class DebtService:

    def __init__(self,
                 db: Session):
        self.debt_repository = DebtRepository(db)

    def create_debt(self,
                    debt: DebtModel) -> DebtBase:
        registered_debt = self.get_debt(debt.debt_id)
        if registered_debt:
            raise DebtAlreadyRegistered(debt.debt_id)
        return self.debt_repository.create_debt(debt)
        
    def get_debt(self,
                 debt_id: int) -> DebtBase:
        return self.debt_repository.get_debt(debt_id)
    
    def get_debts_by_user_and_group(self, 
                                    user_email: str, 
                                    group_id: int) -> list[DebtBase]:
        return self.debt_repository.get_debts_by_user_and_group()
    
    def get_debts_by_debtor(self, 
                            user_email: str) -> list[DebtBase]:
        return self.debt_repository.get_debts_by_debtor()
    
    def get_debts_by_creditor(self, 
                              user_email: str) -> list[DebtBase]:
        return self.debt_repository.get_debts_by_creditor()

    def get_debts_by_group(self, 
                           group_id: int) -> list[DebtBase]:
        return self.debt_repository.get_debts_by_group()
    
    def get_debts_by_payment_id(self, 
                                payment_id: int) -> list[DebtBase]:
        return self.debt_repository.get_debts_by_payment_id()
            
    def update_debt(self,
                    debt_id: int,
                    debt_update: DebtUpdate) -> DebtBase:
        debt = self.get_debt(debt_id)
        if not debt:
            raise DebtNotRegistered(debt.debt_id)
        if debt_update.creditor_id is not None:
            debt.creditor_id = debt_update.creditor_id
        if debt_update.debtor_id is not None:
            debt.debtor_id = debt_update.debtor_id
        if debt_update.group_id is not None:
            debt.group_id = debt_update.group_id
        if debt_update.payment_id is not None:
            debt.payment_id = debt_update.payment_id
        if debt_update.percentage is not None:
            debt.percentage = debt_update.percentage
        return self.debt_repository.update_debt(debt)

    def delete_debt(self,
                    debt: DebtModel) -> bool:
        registered_debt = self.get_debt(debt.debt_id)
        if not registered_debt:
            raise DebtNotRegistered(debt.debt_id)
        return self.debt_repository.delete_debt(debt)