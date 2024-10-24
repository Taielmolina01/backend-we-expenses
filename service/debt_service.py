from sqlalchemy.orm import Session
from tables.debt_base import DebtBase
from models.debt import DebtModel, DebtUpdate, DebtState
from repository.debt_repository import DebtRepository
from service.exceptions.debts_exceptions import *
from service.user_service import UserService
from service.balance_service import BalanceService
from models.user import UserUpdate

def create_debt_from_model(debt_model: DebtModel) -> DebtBase:
    return DebtBase(
        payment_id = debt_model.payment_id,
        group_id = debt_model.group_id,
        debtor_email = debt_model.debtor_email,
        creditor_email = debt_model.creditor_email,
        percentage = debt_model.percentage,
        state = debt_model.state
    )

class DebtService:

    def __init__(self,
                 db: Session):
        self.debt_repository = DebtRepository(db)
        self.user_service = UserService(db)
        self.balance_service = BalanceService()

    def create_debt(self,
                    debt: DebtModel) -> DebtBase:
        return self.debt_repository.create_debt(create_debt_from_model(debt))
        
    def get_debt(self,
                 debt_id: int) -> DebtBase:
        return self.debt_repository.get_debt(debt_id)
    
    def get_debts_by_user_and_group(self, 
                                    user_email: str, 
                                    group_id: int) -> list[DebtBase]:
        return self.debt_repository.get_debts_by_user_and_group(user_email, group_id)
    
    def get_debts_by_debtor(self, 
                            user_email: str) -> list[DebtBase]:
        return self.debt_repository.get_debts_by_debtor(user_email)
    
    def get_debts_by_creditor(self, 
                              user_email: str) -> list[DebtBase]:
        return self.debt_repository.get_debts_by_creditor(user_email)

    def get_debts_by_group(self, 
                           group_id: int) -> list[DebtBase]:
        return self.debt_repository.get_debts_by_group(group_id)
    
    def get_debts_by_payment_id(self, 
                                payment_id: int) -> list[DebtBase]:
        return self.debt_repository.get_debts_by_payment_id(payment_id)
            
    def update_debt(self,
                    debt_id: int,
                    debt_update: DebtUpdate) -> DebtBase:
        debt = self.get_debt(debt_id)
        if not debt:
            raise DebtNotRegistered(debt_id)
        if debt_update.creditor_email:
            debt.creditor_email = debt_update.creditor_email
        if debt_update.debtor_email:
            debt.debtor_email = debt_update.debtor_email
        if debt_update.group_id:
            debt.group_id = debt_update.group_id
        if debt_update.payment_id:
            debt.payment_id = debt_update.payment_id
        if debt_update.percentage:
            debt.percentage = debt_update.percentage
            self.__update_balances(debt, debt_update)
        if debt_update.state:
            self.__update_balances(debt, debt_update)
            debt.state = debt_update.state
        return self.debt_repository.update_debt(debt)

    def __update_balances(self,
                        original_debt: DebtBase,
                        debt_update: DebtUpdate):
        debtor = self.user_service.get_user(original_debt.debtor_email)
        creditor = self.user_service.get_user(original_debt.creditor_email)

        # amount = self.payment_and_debts_service.get_amount_by_debt(original_debt)

        # if debt_update.state and debt_update.state != original_debt.state:


        #     if debt_update.state == DebtState.PAID and original_debt.state == DebtState.UNPAID:
        #         debtor.balance -= amount
        #         creditor.balance += amount
                
        #     elif debt_update.state == DebtState.UNPAID and original_debt.state == DebtState.PAID:
        #         debtor.balance += amount
        #         creditor.balance -= amount

        # if debt_update.percentage and debt_update.percentage != original_debt.percentage:


        #     difference = debt_update.percentage - original_debt.percentage
        #     amount_change = amount * difference

        #     debtor.balance -= amount_change
        #     creditor.balance += amount_change

        # self.user_service.update_user(debtor.email, UserUpdate(balance=debtor.balance))
        # self.user_service.update_user(creditor.email, UserUpdate(balance=creditor.balance))


    def delete_debt(self,
                    debt: DebtModel) -> bool:
        registered_debt = self.get_debt(debt.debt_id)
        if not registered_debt:
            raise DebtNotRegistered(debt.debt_id)
        return self.debt_repository.delete_debt(debt)