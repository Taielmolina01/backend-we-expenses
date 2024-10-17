from pytest_bdd import scenario, given, when, then
from main import app  # Asegúrate de importar tu aplicación FastAPI
from service.user_service import UserService
from models.user import UserModel

@scenario("../features/ver_grupos.feature", "Ver grupos de los que soy parte")
def test_invite_unregisted_members():
    pass

@scenario("../features/ver_grupos.feature", "No tengo grupos")
def test_invite_unregisted_members():
    pass

@given('soy parte de un grupo')
def user_registered(session):
    #todo()
    pass

@given('no soy parte de un grupo')
def user_registered(session):
    #todo()
    pass

@when('entre a la aplicación')
def step_impl(context):
    #todo()
    pass

@then('veo una lista de mis grupos')
def step_impl(context):
    #todo()
    pass

@then('veo un mensaje que dice “No tienes grupos”')
def step_impl(context):
    #todo()
    pass
