from pydantic import BaseModel
from typing import Optional
import enum
from datetime import date

class Category(enum.Enum):
    FOOD = 0
    UTILITIES = 1
    CLOTHING = 2
    HEALTCARE = 3
    PERSONAL = 4
    EDUCATION = 5
    GIFTS = 6
    ENTERTAINMENT = 7

class PaymentModel(BaseModel):
    group_id: int
    payer_email: str
    date: date
    category: Category
    amount: float

    class Config:
        orm_mode = True 

class PaymentUpdate(BaseModel):
    group_id: Optional[int] = None
    payer_email: Optional[str] = None
    date: Optional[date] = None
    category: Optional[Category] = None
    amount: Optional[float] = None

    class Config:
        orm_mode = True 