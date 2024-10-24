from pytest_bdd import scenario, given, when, then
from main import app  
from service.user_invitation_service import *
from service.user_service import UserService
from models.user import UserModel
from service.group_service import GroupService
from util_functions import *

@scenario("../features/configurate_payments.feature", "Configurar división por porcentaje")
def test_invite_unregisted_members():
    pass

@scenario("../features/configurate_payments.feature", "Configurar división por cantidad fija")
def test_invite_registed_members():
    pass

@scenario("../features/configurate_payments.feature", "Sin ser administrador")
def test_invite_registed_members():
    pass

@given('soy administrador del grupo')
def user_registered(session):
    #todo()
    pass 

@given('no soy administrador del grupo')
def user_registered(session):
    #todo()
    pass 

@when('configuro la división de gastos por porcentaje para cada miembro')
def step_impl(session):
    #todo()
    pass 

@when('configuro la división de gastos por cantidad fija para cada miembro')
def step_impl(session):
    #todo()
    pass 

@when('intento cambiar la forma de dividir los gastos')
def step_impl(session):
    #todo()
    pass

@then('se aplica correctamente a los gastos futuros del grupo')
def step_impl(session):
    #todo()
    pass

@then('no puedo hacerlo y me avisa que no tengo permisos')
def step_impl(session):
    #todo()
    pass