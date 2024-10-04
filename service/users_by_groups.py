from sqlalchemy.orm import Session
from repository.users_by_group_repository import UsersByGroupRepository
from service.group_service import GroupService
from service.user_service import UserService
from service.exceptions.groups_exceptions import GroupNotRegistered
from service.exceptions.users_exceptions import UserNotRegistered
from service.exceptions.user_in_group_exceptions import UserNotRegisteredInGroup
from tables.users_by_group_base import UserInGroupBase

class UsersByGroupService:

    def __init__(self,
                 db: Session):
        self.users_by_groups_repository = UsersByGroupRepository(db)
        self.group_service = GroupService(db)
        self.user_service = UserService(db)

    def add_user_in_group(self,
                          user_in_group: UserInGroupBase) -> UserInGroupBase:
        self.validates_registered_group_and_user()
        if not self.__is_user_in_group(user_in_group.group_id, user_in_group.user_id):
            return self.users_by_groups_repository.add_user_in_group(user_in_group)
    
    def __is_user_in_group(self,
                         group_id: int,
                         user_id: int) -> bool:
        
        users = self.get_users_by_group(group_id)
        return user_id in users # dudo que asi esté bien pero la idea es lo q cuenta

    def validates_registered_group_and_user(self,
                                            user_in_group: UserInGroupBase) -> None:
        group = self.user_service.get_group(user_in_group.group_id)
        user_registered = self.user_service.get_user(user_in_group.user_id)
        if group is None:
            raise GroupNotRegistered(user_in_group.group_id)
        if user_registered is None:
            raise UserNotRegistered(user_in_group.user_id)

    def get_users_by_group(self,
                        group_id: int) -> list[UserInGroupBase]:
        return self.users_by_groups_repository.get_users_by_group(group_id)
    
    def get_groups_by_user(self,
                           user_id: int) -> list[UserInGroupBase]:
        return self.users_by_groups_repository.get_groups_by_user(user_id)
    
    def delete_user_in_group(self,
                             user_in_group: UserInGroupBase) -> UserInGroupBase:
        self.validates_registered_group_and_user(user_in_group)
        if not self.__is_user_in_group(user_in_group.group_id, user_in_group.user_id):
            raise UserNotRegisteredInGroup(user_in_group.user_id, user_in_group.group_id)    
        return self.users_by_groups_repository.add_user_in_group(user_in_group)
        