from database import Base
import enum
from sqlalchemy import Column, Integer, Float, Date, Enum, ForeignKey, String

class Category(enum.Enum):
    FOOD = 0
    UTILITIES = 1
    CLOTHING = 2
    HEALTCARE = 3
    PERSONAL = 4
    EDUCATION = 5
    GIFTS = 6
    ENTERTAINMENT = 7

class PaymentBase(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    group_id = Column(Integer, ForeignKey("groups.group_id"))
    payer_email = Column(String, ForeignKey("users.email"))
    date = Column(Date)
    category = Column(Enum(Category))
    amount = Column(Float)