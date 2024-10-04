from sqlalchemy.orm import Session
from tables.group_base import GroupBase, GroupUpdate
from repository.group_repository import GroupRepository
from exceptions.groups_exceptions import *

class GroupService:

    def __init__(self,
                 db: Session):
        self.group_repository = GroupRepository(db)

    def create_group(self,
                     group: GroupBase) -> GroupBase:
        registered_group = self.get_group(group.group_id)
        if registered_group is not None:
            raise GroupAlreadyRegistered(group.group_id)
        if not group.name:
            raise GroupWithoutName()
        return self.group_repository.create_group(group)

    def get_group(self,
                group_id: int) -> GroupBase:
        group = self.group_repository.get_group(group_id)
        if not group:
            raise GroupNotRegistered(group.group_id)
        return group
    
    def update_group(self, 
                    group_id: int, 
                    group_update: GroupUpdate) -> GroupBase:
        group = self.get_user(group_id)
        if group_update.name is not None:
            group.name = group_update.name
        return self.user_repository.update_user(group)
    
    def delete_group(self,
                     group: GroupBase) -> bool:
        group = self.get_group(group.group_id)
        return self.group_repository.delete_group(group)
        
