from sqlalchemy.orm import Session
from tables.debt_base import DebtBase

class DebtRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_debt(self, debt: DebtBase) -> DebtBase:
        self.db.add(debt)
        self.db.commit()
        self.db.refresh(debt)
        return debt

    def get_debt(self, debt_id: int) -> DebtBase:
        return self.db.query(DebtBase).filter(DebtBase.debt_id == debt_id).first()
    
    def get_debts_by_user_and_group(self, user_id: int, group_id: int) -> list[DebtBase]:
        return self.db.query(DebtBase).filter(DebtBase.debtor_id == user_id and DebtBase.group_id == group_id).all()
    
    def get_debts_by_debtor(self, user_id: int) -> list[DebtBase]:
        return self.db.query(DebtBase).filter(DebtBase.debtor_id == user_id).all()
    
    def get_debts_by_creditor(self, user_id: int) -> list[DebtBase]:
        return self.db.query(DebtBase).filter(DebtBase.creditor_id == user_id).all()

    def get_debts_by_group(self, group_id: int) -> list[DebtBase]:
        return self.db.query(DebtBase).filter(DebtBase.group_id == group_id).all()
    
    def get_debts_by_payment_id(self, payment_id: int) -> list[DebtBase]:
        return self.db.query(DebtBase).filter(DebtBase.payment_id == payment_id).all()
    
    def update_debt(self, debt: DebtBase) -> DebtBase:
        self.db.commit()
        return debt
    
    def delete_debt(self, debt_id: int) -> bool:
        debt = self.get_debt(debt_id)
        self.db.delete(debt)
        self.db.commit()
        return True