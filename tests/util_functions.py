from models.user import UserModel
from models.group import GroupModel
from tables.user_base import UserBase
from tables.group_base import GroupBase
from models.user_by_group import UserByGroupModel
from models.payment import PaymentModel, Category
from datetime import date

def create_group_model():
    return GroupModel(name="MyGroup")

def create_user_model():
    return UserModel(
        email="test@example.com",
        name="MyUser1",
        password="securepassword1"
    )

def create_user_model_2():
    return UserModel(
        email="test2@example.com",
        name="MyUser2",
        password="securepassword2"
    )

def create_group_model_without_name():
    return GroupModel(name="")

def create_user_in_group_model(user: UserBase, group: GroupBase):
    return UserByGroupModel(    
            group_id=group.group_id,
            user_email=user.email)

def create_payment_model(user: UserBase, group: GroupBase, category: Category):
    return PaymentModel(
        group_id=group.group_id,
        payer_email=user.email,
        date=date(2024, 10, 21),
        category=category,
        amount=200
    )