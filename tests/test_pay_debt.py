from pytest_bdd import scenario, given, when, then
from main import app  # Asegúrate de importar tu aplicación FastAPI
from models.debt import DebtUpdate
from service.debt_service import DebtService
from service.group_service import GroupService
from service.payment_service import PaymentService
from service.user_service import UserService
from models.user import UserModel
from service.users_by_groups_service import UserByGroupService
from tests.util_functions import *

@scenario("../features/pay_debts.feature", "Liquidar deudas sin ser parte de un evento/grupo")
def test_invite_unregisted_members():
    pass

@scenario("../features/pay_debts.feature", "Liquidar deudas siendo el único participante")
def test_invite_unregisted_members():
    pass

@scenario("../features/pay_debts.feature", "Liquidar deudas siendo parte de un evento/grupo con más participantes")
def test_invite_unregisted_members():
    pass

@given('no soy parte de un evento/grupo')
def user_registered(session):
    UserService(session).create_user(create_user_model())

@given('soy parte de un evento/grupo en el que soy el único participante')
def user_registered(session):
    user = UserModel(email="single_user@example.com", name="Single User", balance=0, password="password")
    user_service = UserService(session)
    user_base = user_service.create_user(user)
    group_base = GroupService(session).create_group(create_group_model())
    UserByGroupService(session).add_user_in_group(create_user_in_group_model(user_base, group_base))

@given('soy parte de un evento/grupo en el que hay más de un participante')
def user_registered(session):
    # Create an event/group with multiple users
    user_service = UserService(session)
    user_base_one = user_service.create_user(create_user_model())
    user_base_two = user_service.create_user(create_user_model_2())
    group_base = GroupService(session).create_group(create_group_model())
    UserByGroupService(session).add_user_in_group(create_user_in_group_model(user_base_one, group_base))
    UserByGroupService(session).add_user_in_group(create_user_in_group_model(user_base_two, group_base))

@when('liquido mis deudas del evento/grupo')
def step_impl(session):
    user_base = UserService(session).get_user("single_user@example.com")
    group_base = GroupService(session).get_group(1)
    PaymentService(session).create_payment(create_payment_model(user_base, group_base, Category.ENTERTAINMENT), {user_base.email: 1})
    debt_base = DebtService(session).get_debt(1)
    DebtService(session).update_debt(debt_base.debt_id, update_debt_model(DebtState.PAID))

@then('no liquido mis deudas')
def step_impl(session):
    user_base = UserService(session).get_user("single_user@example.com")
    group_base = GroupService(session).get_group(1)
    PaymentService(session).create_payment(create_payment_model(user_base, group_base, Category.ENTERTAINMENT), {user_base.email: 1})

@then('mi saldo actual sigue siendo el previo')
def step_impl(session):
    verify_debt(session, 200)

@then('mi saldo actual es $0')
def step_impl(session):
    verify_debt(session, 0)

