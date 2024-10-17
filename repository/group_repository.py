from sqlalchemy.orm import Session
from tables.group_base import GroupBase
from models.group import GroupModel

class GroupRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_group(self, 
                     group: GroupModel) -> GroupBase:
        self.db.add(group)
        self.db.commit()
        self.db.refresh(group)
        return group

    def get_group(self, 
                  group_id: int) -> GroupBase:
        return self.db.query(GroupBase).filter(GroupBase.group_id == group_id).first()
    
    def update_group(self, 
                     group: GroupModel) -> GroupBase:
        self.db.commit()
        self.db.refresh(group)
        return group
    
    def delete_group(self, 
                     group: GroupModel) -> bool:
        self.db.delete(group)
        self.db.commit()
        return True