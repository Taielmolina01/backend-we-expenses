from pytest_bdd import scenario, given, when, then
from main import app  # Asegúrate de importar tu aplicación FastAPI
from service.user_service import UserService
from models.user import UserModel

@scenario("../features/filtrar_eventos.feature", "Filtrar eventos por estado")
def test_invite_unregisted_members():
    pass

@given('soy parte de varios eventos con estados distintos')
def user_registered(session):
    #todo()
    pass

@when('entre a la aplicación y filtre por estado')
def step_impl(context):
    #todo()
    pass

@then('veo una lista de mis eventos con ese estado')
def step_impl(context):
    #todo()
    pass
