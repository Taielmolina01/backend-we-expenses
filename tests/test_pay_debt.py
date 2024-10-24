from pytest_bdd import scenario, given, when, then
import pytest
from main import app  # Asegúrate de importar tu aplicación FastAPI
from models.debt import DebtUpdate
from service.debt_service import DebtService
from service.group_service import GroupService
from service.payment_service import PaymentService
from service.user_service import UserService
from models.user import UserModel
from service.users_by_groups_service import UserByGroupService
from tests.util_functions import *
from service.exceptions.debts_exceptions import *

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
    user = UserModel(email="single_user@example.com", name="Single User", balance=100, password="password")
    user_service = UserService(session)
    user_base = user_service.create_user(user)
    group_base = GroupService(session).create_group(create_group_model())
    UserByGroupService(session).add_user_in_group(create_user_in_group_model(user_base, group_base))
    PaymentService(session).create_payment(create_payment_model(user_base, group_base, Category.CLOTHING), {"test@example.com": 1})


@given('soy parte de un evento/grupo en el que hay más de un participante')
def user_registered(session):
    # Create an event/group with multiple users
    user_service = UserService(session)
    user_base_one = user_service.create_user(create_user_model())
    user_base_two = user_service.create_user(create_user_model_2())
    group_base = GroupService(session).create_group(create_group_model())
    UserByGroupService(session).add_user_in_group(create_user_in_group_model(user_base_one, group_base))
    UserByGroupService(session).add_user_in_group(create_user_in_group_model(user_base_two, group_base))
    PaymentService(session).create_payment(create_payment_model(user_base_one, group_base, Category.CLOTHING), {"test@example.com": 0.5, "test2@example.com": 0.5})

@when('liquido mis deudas del evento/grupo')
def step_impl(session):
    with pytest.raises(DebtNotRegistered):
        DebtService(session).update_debt(1, update_debt_model(DebtState.PAID))

@when('liquido mis deudas inexistentes del evento/grupo')
def step_impl(session):
    with pytest.raises(DebtNotRegistered):
        DebtService(session).update_debt(1, update_debt_model(DebtState.PAID))

@when('liquido todas mis deudas del evento/grupo')
def step_impl(session):
    DebtService(session).update_debt(1, update_debt_model(DebtState.PAID))

@then('no liquido mis deudas')
def step_impl(session):
    assert DebtService(session).get_debts_by_debtor("test@example.com") == []

@then('no liquido deudas y mi saldo sigue siendo el previo')
def step_impl(session):
    verify_debt(session, 100)

@then('mi saldo actual es $0')
def step_impl(session):
    verify_debt(session, 0)

