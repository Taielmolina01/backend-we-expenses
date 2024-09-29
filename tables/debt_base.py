from database import Base
from pydantic import BaseModel
from sqlalchemy import Column, Integer, Float, ForeignKey
from typing import Optional

class DebtBase(Base):
    __tablename__ = "debts"

    debt_id = Column(Integer, primary_key=True, autoincrement=True)
    payment_id = Column(Integer, ForeignKey("payments.payment_id"))
    group_id = Column(Integer, ForeignKey("groups.group_id"))
    debtor_id = Column(Integer, ForeignKey("users.user_id"))
    creditor_id = Column(Integer, ForeignKey("users.user_id"))
    percentage = Column(Float)

class DebtUpdate(BaseModel):
    payment_id: Optional[int] = None
    group_id: Optional[int] = None
    debtor_id = Optional[int] = None
    creditor_id = Optional[int] = None
    percentage = Optional[float] = None

