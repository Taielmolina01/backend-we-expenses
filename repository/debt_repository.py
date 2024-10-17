from sqlalchemy.orm import Session
from tables.debt_base import DebtBase
from models.debt import DebtModel, DebtUpdate

class DebtRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_debt(self, 
                    debt: DebtModel) -> DebtBase:
        self.db.add(debt)
        self.db.commit()
        self.db.refresh(debt)
        return debt

    def get_debt(self, 
                 debt_id: int) -> DebtBase:
        return self.db.query(DebtBase).filter(DebtBase.debt_id == debt_id).first()
    
    def get_debts_by_user_and_group(self, 
                                    user_email: str, 
                                    group_id: int) -> list[DebtBase]:
        return self.db.query(DebtBase).filter(DebtBase.debtor_id == user_email and DebtBase.group_id == group_id).all()
    
    def get_debts_by_debtor(self, 
                            user_email: str) -> list[DebtBase]:
        return self.db.query(DebtBase).filter(DebtBase.debtor_id == user_email).all()
    
    def get_debts_by_creditor(self, 
                              user_email: str) -> list[DebtBase]:
        return self.db.query(DebtBase).filter(DebtBase.creditor_id == user_email).all()

    def get_debts_by_group(self, 
                           group_id: int) -> list[DebtBase]:
        return self.db.query(DebtBase).filter(DebtBase.group_id == group_id).all()
    
    def get_debts_by_payment_id(self, 
                                payment_id: int) -> list[DebtBase]:
        return self.db.query(DebtBase).filter(DebtBase.payment_id == payment_id).all()
    
    def update_debt(self, 
                    debt: DebtUpdate) -> DebtBase:
        self.db.commit()
        self.db.refresh(debt)
        return debt
    
    def delete_debt(self, 
                    debt: DebtModel) -> bool:
        self.db.delete(debt)
        self.db.commit()
        return True