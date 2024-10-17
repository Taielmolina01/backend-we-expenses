from pytest_bdd import scenario, given, when, then
from main import app  # Asegúrate de importar tu aplicación FastAPI
from service.user_service import UserService
from models.user import UserModel

@scenario("../features/creacion_de_eventos.feature", "Registro con un email no existente")
def test_invite_unregisted_members():
    pass

@scenario("../features/creacion_de_eventos.feature", "Registro con un email existente")
def test_invite_registed_members():
    pass

@given('estoy registrado en la aplicación')
def user_registered(session):
    user = UserModel(email="test@example.com", name="Test User", balance=0, password="testpassword")
    user_service = UserService(session)
    user_service.create_user(user)

@when('invito a mi evento a los miembros por nombres de usuario registrados')
def step_impl(context):
    #todo()
    pass 

@then('los invito')
def step_impl(context):
    #todo()
    pass

@when('invito a mi evento a los miembros por nombres de usuario no registrados')
def step_impl(context):
    #todo()
    pass

@then('no los invito y me avisa diciendo “no existe ese usuario”')
def step_impl(context):
    #todo()
    pass