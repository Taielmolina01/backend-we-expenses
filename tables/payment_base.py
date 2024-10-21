from database import Base
import enum
from sqlalchemy import Column, Integer, Float, Date, Enum, ForeignKey, String
from models.payment import Category

class PaymentBase(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    group_id = Column(Integer, ForeignKey("groups.group_id"))
    payer_email = Column(String, ForeignKey("users.email"))
    date = Column(Date)
    category = Column(Enum(Category))
    amount = Column(Float)