from database import Base
from sqlalchemy import Column, Integer, Float

class DebtBase(Base):
    __tablename__ = "debts"

    debt_id = Column(Integer, primary_key=True, autoincrement=True)
    payment_id = Column(Integer, ForeignKey())
    group_id = Column(Integer, ForeignKey())
    debtor_id = Column(Integer, ForeignKey())
    creditor_id = Column(Integer, ForeignKey())
    percentage = Column(Float)