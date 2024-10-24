from pytest_bdd import scenario, given, when, then
from main import app  # Asegúrate de importar tu aplicación FastAPI
from service.payment_service import PaymentService
from service.user_service import UserService
from models.user import UserModel
from service.users_by_groups_service import UserByGroupService
from tests.util_functions import *

@scenario("../features/see_payments.feature", "Ver gastos de un grupo con gastos")
def test_invite_unregisted_members():
    pass

@scenario("../features/see_payments.feature", "Ver gastos de un grupo sin gastos")
def test_invite_unregisted_members():
    pass

@given('pertenezco a un grupo con gastos')
def user_registered(session):
    user_service = UserService(session)
    user_base = user_service.create_user(create_user_model())
    group_base = GroupService(session).create_group(create_group_model())
    UserByGroupService(session).add_user_in_group(create_user_in_group_model(user_base, group_base))
    PaymentService(session).create_payment(create_payment_model(user_base, group_base, Category.ENTERTAINMENT), {user_base.email: 1})
    PaymentService(session).create_payment(create_payment_model(user_base, group_base, Category.FOOD), {user_base.email: 1})
    
@given('pertenezco a un grupo sin gastos')
def user_registered(session):
    user_service = UserService(session)
    user_base = user_service.create_user(create_user_model())
    group_base = GroupService(session).create_group(create_group_model())
    UserByGroupService(session).add_user_in_group(create_user_in_group_model(user_base, group_base))

@when('veo los gastos del grupo')
def step_impl(session):
    pass

@then('veo listados los gastos del grupo')
def step_impl(session):
    payments = PaymentService(session).get_payments_by_group(1)
    assert len(payments) == 2
    assert payments[0].category == Category.ENTERTAINMENT
    assert payments[1].category == Category.FOOD

@then('no veo ningún gasto registrado')
def step_impl(session):
    payments = PaymentService(session).get_payments_by_group(1)
    assert len(payments) == 0
