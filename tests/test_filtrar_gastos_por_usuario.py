from pytest_bdd import scenario, given, when, then
from main import app  # Asegúrate de importar tu aplicación FastAPI
from service.user_service import UserService
from models.user import UserModel

@scenario("../features/filtrar_gastos_por_usuario.feature", "Filtrar gastos por nombre de usuario")
def test_invite_unregisted_members():
    pass

@scenario("../features/filtrar_gastos_por_usuario.feature", "Filtrar gastos por nombre de usuario sin registros")
def test_invite_unregisted_members():
    pass

@given('pertenezco a un grupo y existen gastos registrados para el usuario seleccionado')
def user_registered(session):
    #todo()
    pass

@given('pertenezco a un grupo pero no hay gastos registrados para el usuario seleccionado')
def user_registered(session):
    #todo()
    pass

@when('filtro los gastos por el nombre de ese usuario')
def step_impl(context):
    #todo()
    pass

@then('veo una lista de los gastos de ese usuario y las categorías correspondientes')
def step_impl(context):
    #todo()
    pass

@then('no veo ningún gasto y me avisa diciendo “No hay gastos registrados para este usuario”')
def step_impl(context):
    #todo()
    pass
