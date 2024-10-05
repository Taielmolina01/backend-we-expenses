from sqlalchemy.orm import Session
from tables.debt_base import DebtBase, DebtUpdate
from repository.debt_repository import DebtRepository
from service.exceptions.debts_exceptions import *

class DebtService:

    def __init__(self,
                 db: Session):
        self.debt_repository = DebtRepository(db)

    def create_debt(self,
                    debt: DebtBase) -> DebtBase:
        registered_debt = self.get_debt(debt.debt_id)
        if registered_debt:
            raise DebtAlreadyRegistered(debt.debt_id)
        return self.debt_repository.create_debt(debt)
        
    def get_debt(self,
                 debt_id: int) -> DebtBase:
        return self.debt_repository.get_debt(debt_id)
        
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
                    debt: DebtBase) -> bool:
        registered_debt = self.get_debt(debt.debt_id)
        if not registered_debt:
            raise DebtNotRegistered(debt.debt_id)
        return self.debt_repository.delete_debt(debt)