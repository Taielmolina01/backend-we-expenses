from models.debt import DebtState, DebtUpdate
from models.user import UserModel
from models.group import GroupModel
from models.user_invitation import UserInvitationModel
from service.debt_service import DebtService
from service.group_service import GroupService
from service.user_service import UserService
from tables.user_base import UserBase
from tables.group_base import GroupBase
from models.user_by_group import UserByGroupModel
from models.payment import PaymentModel, Category
from datetime import date

def create_group_model():
    return GroupModel(name="MyGroup")

def create_group_model_2():
    return GroupModel(name="MyGroup2")

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

def create_payment_model(payer: UserBase, group: GroupBase, category: Category):
    return PaymentModel(
        group_id=group.group_id,
        payer_email=payer.email,
        date=date(2024, 10, 21),
        category=category,
        amount=200
    )

def create_invitation_model():
    return UserInvitationModel(
        invitator_email="test2@example.com",
        guest_email="test@example.com",
        group_id=1,
        send_date=date(2024, 10, 21),
        expire_date=date(2024, 10, 28)
    )

def update_debt_model(state: DebtState):
    return DebtUpdate(
        state=state
    )

def verify_debt(session, debt: int):
    user_base_one = UserService(session).get_user("test@example.com")
    user_base_two = UserService(session).get_user("test2@example.com")
    group_base = GroupService(session).get_group(1)
    debt_by_creditor = DebtService(session).get_debts_by_creditor(user_base_one.email)[0]
    debt_by_debtor = DebtService(session).get_debts_by_debtor(user_base_two.email)[0]
    assert debt_by_creditor.group_id == debt_by_debtor.group_id == group_base.group_id
    assert debt_by_creditor.creditor_email == debt_by_debtor.creditor_email
    assert debt_by_creditor.debtor_email == debt_by_debtor.debtor_email
    assert debt_by_creditor.debt_id == debt_by_debtor.debt_id
    assert debt_by_creditor.payment_id == debt_by_debtor.payment_id 
    assert debt_by_creditor.percentage == debt_by_debtor.percentage
    assert user_base_one.balance == -debt
    assert user_base_two.balance == debt