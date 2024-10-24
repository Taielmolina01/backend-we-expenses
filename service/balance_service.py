from sqlalchemy.orm import Session
from models.user import UserUpdate
from models.debt import DebtState, DebtBase, DebtUpdate
from models.payment import PaymentBase
from service.user_service import UserService

class BalanceService:
    def __init__(self, db: Session):
        self.user_service = UserService(db)
    
    def update_balance_on_debt_change(self, 
                                      debtor_email: str, 
                                      creditor_email: str, 
                                      amount: float, 
                                      new_state: DebtState, 
                                      old_state: DebtState):
        debtor = self.user_service.get_user(debtor_email)
        creditor = self.user_service.get_user(creditor_email)
        
        if new_state == DebtState.PAID and old_state == DebtState.UNPAID:
            debtor.balance -= amount
            creditor.balance += amount
        elif new_state == DebtState.UNPAID and old_state == DebtState.PAID:
            debtor.balance += amount
            creditor.balance -= amount
        
        self.user_service.update_user(debtor.email, UserUpdate(balance=debtor.balance))
        self.user_service.update_user(creditor.email, UserUpdate(balance=creditor.balance))

    def update_balance_on_percentage_change(self, 
                                            debtor_email: str, 
                                            creditor_email: str, 
                                            original_amount: float, 
                                            percentage_difference: float):
        debtor = self.user_service.get_user(debtor_email)
        creditor = self.user_service.get_user(creditor_email)
        amount_change = original_amount * percentage_difference

        debtor.balance -= amount_change
        creditor.balance += amount_change

        self.user_service.update_user(debtor.email, UserUpdate(balance=debtor.balance))
        self.user_service.update_user(creditor.email, UserUpdate(balance=creditor.balance))

    def update_balance_on_payment(self, 
                                  payer_email: str, 
                                  amount: float, 
                                  percentages: dict[str, float], 
                                  users: list[str]):
        payer = self.user_service.get_user(payer_email)
        payer.balance -= amount

        for user_email in users:
            user = self.user_service.get_user(user_email)
            user_percentage = percentages.get(user_email, 0)
            user.balance += user_percentage * amount
            self.user_service.update_user(user.email, UserUpdate(balance=user.balance))
        
        self.user_service.update_user(payer.email, UserUpdate(balance=payer.balance))