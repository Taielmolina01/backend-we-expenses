from pytest_bdd import scenario, given, when, then
from main import app  # Asegúrate de importar tu aplicación FastAPI
from service.user_service import UserService
from models.user import UserModel

@scenario("../features/ver_eventos.feature", "Ver eventos de los que soy parte")
def test_invite_unregisted_members():
    pass

@scenario("../features/ver_eventos.feature", "No tengo eventos")
def test_invite_unregisted_members():
    pass

@given('soy parte de un evento')
def user_registered(session):
    #todo()
    pass

@given('no soy parte de ningún evento')
def user_registered(session):
    #todo()
    pass

@when('entre a la aplicación')
def step_impl(context):
    #todo()
    pass

@then('veo una lista de mis eventos')
def step_impl(context):
    #todo()
    pass

@then('veo un mensaje que dice “No tienes eventos”')
def step_impl(context):
    #todo()
    pass
