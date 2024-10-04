from sqlalchemy.orm import Session
from repository.users_by_group_repository import UsersByGroupRepository
from service.group_service import GroupService
from tables.user_base import UserBase
from tables.group_base import GroupBase

class UsersByGroupService:

    def __init__(self,
                 db: Session):
        self.users_by_groups_repository = UsersByGroupRepository(db)

    def add_user_in_group(self,
                          group_id: int,
                          user: UserBase) -> bool:
        pass


    def get_users_by_group(self,
                        group_id: int):
        return self.users_by_groups_repository.get_users_by_group(group_id)
    
    def get_groups_by_user(self,
                           user_id: int):
        return self.users_by_groups_repository.get_groups_by_user(user_id)
    
