from pytest_bdd import scenario, given, when, then
from main import app  # Asegúrate de importar tu aplicación FastAPI
from service.user_service import UserService
from models.user import UserModel
from service.users_by_groups_service import UserByGroupService
from tests.util_functions import *

@scenario("../features/see_groups.feature", "Ver grupos de los que soy parte")
def test_invite_unregisted_members():
    pass

@scenario("../features/see_groups.feature", "No tengo grupos")
def test_invite_unregisted_members():
    pass

@given('soy parte de un grupo')
def user_registered(session):
    user_service = UserService(session)
    user_base_one = user_service.create_user(create_user_model())
    group_one = GroupService(session).create_group(create_group_model())
    group_two = GroupService(session).create_group(create_group_model_2())
    UserByGroupService(session).add_user_in_group(create_user_in_group_model(user_base_one, group_one))
    UserByGroupService(session).add_user_in_group(create_user_in_group_model(user_base_one, group_two))

@given('no soy parte de un grupo')
def user_registered(session):
    UserService(session).create_user(create_user_model())

@when('entre a la aplicación')
def step_impl(session):
    pass

@then('veo una lista de mis grupos')
def step_impl(session):
    user_base = UserService(session).get_user("test@example.com")
    groups = UserByGroupService(session).get_groups_by_user(user_base.email)
    assert groups[0].name == "MyGroup"
    assert groups[1].name == "MyGroup2"

@then('veo un mensaje que dice “No tienes grupos”')
def step_impl(session):
    user_base = UserService(session).get_user("test@example.com")
    groups = UserByGroupService(session).get_groups_by_user(user_base.email)
    assert len(groups) == 0
