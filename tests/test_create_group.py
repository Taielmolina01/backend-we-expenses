from pytest_bdd import scenario, given, when, then
from main import app  # Asegúrate de importar tu aplicación FastAPI
from service.user_service import UserService
from models.user import UserModel

@scenario("../features/create_group.feature", "Crear un grupo con un ID existente")
def test_invite_unregisted_members():
    pass

@scenario("../features/create_group.feature", "Crear un grupo con un ID no existente")
def test_invite_registed_members():
    pass

@scenario("../features/create_group.feature", "Invitar amigos no registrados")
def test_invite_registed_members():
    pass

@scenario("../features/create_group.feature", "Invitar amigos registrados")
def test_invite_registed_members():
    pass

@given('estoy registrado en la aplicación')
def user_registered(session):
    user = UserModel(email="test@example.com", name="Test User", balance=0, password="testpassword")
    user_service = UserService(session)
    user_service.create_user(user)

@when('creo un grupo con un id de grupo ya existente')
def step_impl(context):
    #todo()
    pass

@when('creo un grupo con un id de grupo no existente')
def step_impl(context):
    #todo()
    pass 

@when('invito a mi grupo a mis amigos por nombres de usuario no registrados')
def step_impl(context):
    #todo()
    pass 

@when('invito a mi grupo a mis amigos por nombres de usuarios registrados')
def step_impl(context):
    #todo()
    pass 

@then('no se crea el grupo')
def step_impl(context):
    #todo()
    pass

@then('se crea el grupo')
def step_impl(context):
    #todo()
    pass

@then('no los invito y me avisa diciendo “no existe ese usuario”')
def step_impl(context):
    #todo()
    pass

@then('se los envía la invitación')
def step_impl(context):
    #todo()
    pass