from pydantic import BaseModel
from typing import Optional
import enum

class DebtState(enum.Enum):
    UNPAID = 0
    PAID = 1

class DebtModel(BaseModel):
    payment_id: int
    group_id: int
    debtor_email: str
    creditor_email: str
    percentage: float
    debt_state: Optional[DebtState] = 0

    class Config:
        orm_mode = True 

class DebtUpdate(BaseModel):
    payment_id: Optional[int] = None
    group_id: Optional[int] = None
    debtor_id: Optional[int] = None
    creditor_id: Optional[int] = None
    percentage: Optional[float] = None
    debt_state: Optional[DebtState] = None

    class Config:
        orm_mode = True 