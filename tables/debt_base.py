from database import Base
from pydantic import BaseModel
from sqlalchemy import Column, Integer, Float, ForeignKey, String
from typing import Optional

class DebtBase(Base):
    __tablename__ = "debts"

    debt_id = Column(Integer, primary_key=True, autoincrement=True)
    payment_id = Column(Integer, ForeignKey("payments.payment_id"))
    group_id = Column(Integer, ForeignKey("groups.group_id"))
    debtor_email = Column(String, ForeignKey("users.email"))
    creditor_email = Column(String, ForeignKey("users.email"))
    percentage = Column(Float)
