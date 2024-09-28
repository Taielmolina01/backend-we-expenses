from pydantic import BaseModel
from enum import Enum

class Category(int, Enum):
    FOOD = 0
    UTILITIES = 1
    CLOTHING = 2
    HEALTCARE = 3
    PERSONAL = 4
    EDUCATION = 5
    GIFTS = 6
    ENTERTAINMENT = 7

class Transaction(BaseModel):
    id: int
    category: Category
    amount: int    