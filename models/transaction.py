from pydantic import BaseModel

class Transaction(BaseModel):
    id: int
    category: Category
    amount: int    