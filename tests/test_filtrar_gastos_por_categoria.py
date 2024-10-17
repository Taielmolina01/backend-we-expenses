from pytest_bdd import scenario, given, when, then
from main import app  # Asegúrate de importar tu aplicación FastAPI
from service.user_service import UserService
from models.user import UserModel

@scenario("../features/filtrar_gastos_por_categoria.feature", "Filtrar gastos por una categoría específica")
def test_invite_unregisted_members():
    pass

@scenario("../features/filtrar_gastos_por_categoria.feature", "Filtrar gastos por categoría sin registros")
def test_invite_unregisted_members():
    pass

@given('pertenezco a un grupo y hay gastos registrados')
def user_registered(session):
    #todo()
    pass

@given('pertenezco a un grupo pero no hay gastos en la categoría seleccionada')
def user_registered(session):
    #todo()
    pass

@when('filtro los gastos por esa categoría')
def step_impl(context):
    #todo()
    pass

@then('veo una lista de los gastos en esa categoría')
def step_impl(context):
    #todo()
    pass

@then('no veo ningún gasto y me avisa diciendo “No hay gastos registrados en esta categoría”')
def step_impl(context):
    #todo()
    pass
