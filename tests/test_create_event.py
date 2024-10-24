from pytest_bdd import scenario, given, when, then
from main import app  
from service.user_invitation_service import *
from service.user_service import UserService
from models.user import UserModel
from service.group_service import GroupService
from util_functions import *

@scenario("../features/create_event.feature", "Invitar miembros registrados a un evento")
def test_invite_unregisted_members():
    pass

@scenario("../features/create_event.feature", "Invitar miembros no registrados a un evento")
def test_invite_registed_members():
    pass

@given('estoy registrado en la aplicación')
def user_registered(session):
    user = UserModel(email="test@example.com", name="Test User", balance=0, password="testpassword")
    user_service = UserService(session)
    user_service.create_user(user)

@when('invito a mi evento a los miembros por nombres de usuario registrados')
def step_impl(session):
    #todo()
    pass 

@then('los invito')
def step_impl(session):
    #todo()
    pass

@when('invito a mi evento a los miembros por nombres de usuario no registrados')
def step_impl(session):
    #todo()
    pass

@then('no los invito y me avisa diciendo “no existe ese usuario”')
def step_impl(session):
    #todo()
    pass