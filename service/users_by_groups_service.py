from sqlalchemy.orm import Session
from repository.users_by_groups_repository import UsersByGroupRepository
from service.group_service import GroupService
from service.user_service import UserService
from service.exceptions.groups_exceptions import GroupNotRegistered
from service.exceptions.users_exceptions import UserNotRegistered
from service.exceptions.users_by_groups_exceptions import UserNotRegisteredInGroup
from tables.users_by_group_base import UserInGroupBase
from models.user_by_group import UserByGroupModel

def create_user_by_group_from_model(user_by_group: UserByGroupModel) -> UserInGroupBase:
    return UserInGroupBase(
        group_id = user_by_group.group_id,
        user_email = user_by_group.user_email
    )

class UserByGroupService:

    def __init__(self,
                 db: Session):
        self.users_by_groups_repository = UsersByGroupRepository(db)
        self.group_service = GroupService(db)
        self.user_service = UserService(db)

    def add_user_in_group(self,
                          user_in_group: UserByGroupModel) -> UserInGroupBase:
        self.validates_registered_group_and_user(user_in_group)
        if not self.__is_user_in_group(user_in_group.group_id, user_in_group.user_id):
            return self.users_by_groups_repository.add_user_in_group(create_user_by_group_from_model(user_in_group))
    
    def __is_user_in_group(self,
                         group_id: int,
                         user_email: str) -> bool:
        
        users = self.get_users_by_group(group_id)
        return user_email in users # dudo que asi esté bien pero la idea es lo q cuenta

    def validates_registered_group_and_user(self,
                                            user_in_group: UserByGroupModel) -> None:
        group = self.user_service.get_group(user_in_group.group_id)
        user_registered = self.user_service.get_user(user_in_group.user_id)
        if not group:
            raise GroupNotRegistered(user_in_group.group_id)
        if not user_registered:
            raise UserNotRegistered(user_in_group.user_id)

    def get_users_by_group(self,
                        group_id: int) -> list[UserInGroupBase]:
        group = self.group_service.get_group(group_id)
        if not group:
            raise GroupNotRegistered(group_id)
        return self.users_by_groups_repository.get_users_by_group(group_id)
    
    def get_groups_by_user(self,
                           user_id: int) -> list[UserInGroupBase]:
        user = self.group_service.get_group(user_id)
        if not user:
            raise UserNotRegistered(user_id)
        return self.users_by_groups_repository.get_groups_by_user(user_id)
    
    def delete_user_in_group(self,
                             user_in_group: UserByGroupModel) -> UserInGroupBase:
        self.validates_registered_group_and_user(user_in_group)
        if not self.__is_user_in_group(user_in_group.group_id, user_in_group.user_id):
            raise UserNotRegisteredInGroup(user_in_group.user_id, user_in_group.group_id)    
        return self.users_by_groups_repository.add_user_in_group(user_in_group)
        