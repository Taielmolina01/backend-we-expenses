from pytest_bdd import scenario, given, when, then
from main import app  # Asegúrate de importar tu aplicación FastAPI
from service.user_service import UserService
from models.user import UserModel
from service.group_service import GroupService
from models.group import GroupModel
from service.exceptions.groups_exceptions import *
import pytest
from service.user_invitation_service import UserInvitationModel, UserInvitationService
from datetime import date
from service.exceptions.users_exceptions import UserNotRegistered

@scenario("../features/create_group.feature", "Crear un grupo sin nombre")
def test_create_group_without_name():
    pass

@scenario("../features/create_group.feature", "Crear un grupo con nombre")
def test_create_group_with_valid_name():
    pass

@scenario("../features/create_group.feature", "Invitar amigos no registrados")
def test_invite_not_registered_members():
    pass

@scenario("../features/create_group.feature", "Invitar amigos registrados")
def test_invite_registered_members():
    pass

@given('estoy registrado en la aplicación')
def user_registered(session):
    pass

def create_group_model_without_name():
    return GroupModel(name="")

def create_group_model():
    return GroupModel(name="MyGroup")

def create_user_model():
    return UserModel(
        email="test@example.com",
        name="MyUser1",
        password="securepassword1"
    )

def create_user_model_2():
    return UserModel(
        email="test2@example.com",
        name="MyUser2",
        password="securepassword2"
    )

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

@when('invito a mi grupo a mis amigos por emails no registrados')
def step_impl(session):
    UserService(session).create_user(create_user_model())
    GroupService(session).create_group(create_group_model())
    with pytest.raises(UserNotRegistered):
        UserInvitationService(session).create_invitation(create_invitation_model())

@when('invito a mi grupo a mis amigos por emails registrados')
def step_impl(session):
    UserService(session).create_user(create_user_model())
    UserService(session).create_user(create_user_model_2())
    GroupService(session).create_group(create_group_model())
    UserInvitationService(session).create_invitation(create_invitation_model())
    
@then('no se crea el grupo')
def step_impl(session):
    with pytest.raises(GroupNotRegistered):
        GroupService(session).get_group(1)

@then('se crea el grupo')
def step_impl(session):
    assert GroupService(session).get_group(1).name == "MyGroup"
    assert GroupService(session).get_group(1).group_id == 1

@then('no los invito')
def step_impl(session):
    assert UserInvitationService(session).get_invitations_by_guest("test@example.com") == []

@then('los invito')
def step_impl(session):
   invitations = UserInvitationService(session).get_invitations_by_guest("test@example.com")
   invitation = invitations[0]
   assert invitation.invitation_id == 1
   assert invitation.invitator_email == "test2@example.com"
   assert invitation.guest_email == "test@example.com"
   assert invitation.group_id == 1
   assert invitation.send_date == date(2024, 10, 21)
   assert invitation.expire_date == date(2024, 10, 28)