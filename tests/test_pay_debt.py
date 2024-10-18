from pytest_bdd import scenario, given, when, then
from main import app  # Asegúrate de importar tu aplicación FastAPI
from service.user_service import UserService
from models.user import UserModel

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
    #todo()
    pass

@given('soy parte de un evento/grupo en el que soy el único participante')
def user_registered(session):
    #todo()
    pass

@given('soy parte de un evento/grupo en el que hay más de un participante')
def user_registered(session):
    #todo()
    pass

@when('liquido mis deudas del evento/grupo')
def step_impl(context):
    #todo()
    pass

@then('no liquido mis deudas')
def step_impl(context):
    #todo()
    pass

@then('mi saldo actual sigue siendo el previo')
def step_impl(context):
    #todo()
    pass

@then('mi saldo actual es $0')
def step_impl(context):
    #todo()
    pass

