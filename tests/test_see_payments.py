from pytest_bdd import scenario, given, when, then
from main import app  # Asegúrate de importar tu aplicación FastAPI
from service.user_service import UserService
from models.user import UserModel

@scenario("../features/see_payments.feature", "Ver gastos de un grupo")
def test_invite_unregisted_members():
    pass

@scenario("../features/see_payments.feature", "Ver gastos de un grupo nuevo")
def test_invite_unregisted_members():
    pass

@given('pertenezco a un grupo')
def user_registered(session):
    #todo()
    pass

@given('pertenezco a un grupo nuevo')
def user_registered(session):
    #todo()
    pass

@when('veo los gastos del grupo')
def step_impl(context):
    #todo()
    pass

@then('veo listados los gastos del grupo')
def step_impl(context):
    #todo()
    pass

@then('no veo ningún gasto registrado')
def step_impl(context):
    #todo()
    pass
