from pytest_bdd import scenario, given, when, then
import pytest
from fastapi.testclient import TestClient
from main import app  # Asegúrate de importar tu aplicación FastAPI
from service.group_service import GroupService
from models.group import GroupModel
from models.user import UserModel
from tables.group_base import GroupBase
from tables.user_base import UserBase

client = TestClient(app)

@scenario("../features/delete_group.feature", "Borrar grupo siendo un usuario no registrado")
def test_delete_group_as_admin():
  pass

@scenario("../features/delete_group.feature", "Borrar grupo siendo usuario registrado no siendo parte del grupo")
def test_delete_group_not_as_admin():
  pass

@scenario("../features/delete_group.feature", "Borrar grupo siendo usuario registrado siendo parte del grupo")
def test_delete_group_not_as_admin():
  pass

@given("no estoy registrado")
def admin_of_group(session):
  pass

@given("estoy registrado")
def not_admin_of_group(session):
  pass

@when("elimino un grupo")
def delete_group_not_as_admin():
  pass

@when("elimino un grupo en el que no soy parte")
def delete_group_not_as_admin():
  pass

@when("elimino un grupo en el que no soy parte")
def delete_group_not_as_admin():
  pass

@then("no se elimina")
def group_deleted():
  pass

@then("se me indica que no pertenezco al grupo")
def group_deleted():
  pass

@then("se elimina")
def group_deleted():
  pass