from pytest_bdd import scenario, given, when, then
from main import app 
from service.group_service import GroupService
from models.group import GroupModel
from service.exceptions.groups_exceptions import *
import pytest
from service.user_invitation_service import UserInvitationModel
from datetime import date
from util_functions import *

@scenario("../features/create_group.feature", "Crear un grupo sin nombre")
def test_create_group_without_name():
    pass

@scenario("../features/create_group.feature", "Crear un grupo con nombre")
def test_create_group_with_valid_name():
    pass

@given('que tengo una sesión iniciada')
def user_logged(session):
    pass

@given('que no tengo una sesión iniciada')
def user_not_logged(session):
    pass

def create_invitation_model():
    return UserInvitationModel(
        invitator_email="test2@example.com",
        guest_email="test@example.com",
        group_id=1,
        send_date=date(2024, 10, 21),
        expire_date=date(2024, 10, 28)
    )

@when('creo un grupo sin nombre')
def step_impl(session):
    group_service = GroupService(session)
    with pytest.raises(GroupWithoutName):
        group_service.create_group(create_group_model_without_name())

@when('creo un grupo con nombre')
def step_impl(session):
    GroupService(session).create_group(create_group_model())

@then('no se crea el grupo')
def step_impl(session):
    with pytest.raises(GroupNotRegistered):
        GroupService(session).get_group(1)

@then('se crea el grupo')
def step_impl(session):
    assert GroupService(session).get_group(1).name == "MyGroup"
    assert GroupService(session).get_group(1).group_id == 1
