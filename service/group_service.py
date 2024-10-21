from sqlalchemy.orm import Session
from models.group import GroupModel, GroupUpdate
from tables.group_base import GroupBase
from repository.group_repository import GroupRepository
from service.exceptions.groups_exceptions import *

def create_group_from_model(group_model: GroupModel) -> GroupBase:
    return GroupBase(
        name=group_model.name
    )

class GroupService:

    def __init__(self,
                 db: Session):
        self.group_repository = GroupRepository(db)

    def create_group(self,
                     group: GroupModel) -> GroupBase:
        if not group.name:
            raise GroupWithoutName()
        return self.group_repository.create_group(create_group_from_model(group))

    def get_group(self,
                group_id: int) -> GroupBase:
        group = self.group_repository.get_group(group_id)
        if not group:
            raise GroupNotRegistered()
        return group
    
    def update_group(self, 
                    group_id: int, 
                    group_update: GroupUpdate) -> GroupBase:
        group = self.get_group(group_id)
        if group_update.name is not None:
            group.name = group_update.name
        return self.user_repository.update_user(group)
    
    def delete_group(self,
                     group_id: int) -> bool:
        group = self.get_group(group_id)
        return self.group_repository.delete_group(group)
        
