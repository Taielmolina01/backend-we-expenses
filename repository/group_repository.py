from sqlalchemy.orm import Session
from tables.group_base import GroupBase

class GroupRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_group(self, group: GroupBase) -> GroupBase:
        self.db.add(group)
        self.db.commit()
        self.db.refresh(group)
        return group

    def get_group(self, group_id: int) -> GroupBase:
        return self.db.query(GroupBase).filter(GroupBase.group_id == group_id).first()
    
    def update_group(self, group: GroupBase) -> GroupBase:
        self.db.commit()
        self.db.refresh(group)
        return group
    
    def delete_group(self, group_id: int) -> bool:
        group = self.get_group(group_id)
        self.db.delete(group)
        self.db.commit()
        return True