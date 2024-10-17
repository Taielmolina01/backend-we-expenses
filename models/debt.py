from pydantic import BaseModel, Optional

class DebtModel(BaseModel):
    payment_id: int
    group_id: int
    debtor_email: str
    creditor_email: str
    percentage: float

class DebtUpdate(BaseModel):
    payment_id: Optional[int] = None
    group_id: Optional[int] = None
    debtor_id: Optional[int] = None
    creditor_id: Optional[int] = None
    percentage: Optional[float] = None
