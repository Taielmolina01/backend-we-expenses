from pydantic import BaseModel, Optional

class PaymentModel(BaseModel):
    payment_id: int
    group_id: int
    debtor_id: str
    creditor_id: str
    percentage: float

class PaymentUpdate(BaseModel):
    payment_id: Optional[int] = None
    group_id: Optional[int] = None
    debtor_id: Optional[str] = None
    creditor_id: Optional[str] = None
    percentage: Optional[float] = None