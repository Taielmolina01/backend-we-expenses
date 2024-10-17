from sqlalchemy.orm import Session
from tables.group_base import GroupBase, GroupResponse

class GroupRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_group(self, group: GroupBase) -> GroupResponse:
        self.db.add(group)
        self.db.commit()
        self.db.refresh(group)
        return group

    def get_group(self, group_id: int) -> GroupResponse:
        return self.db.query(GroupBase).filter(GroupBase.group_id == group_id).first()
    
    def update_group(self, group: GroupBase) -> GroupResponse:
        self.db.commit()
        self.db.refresh(group)
        return group
    
    def delete_group(self, group: GroupBase) -> bool:
        self.db.delete(group)
        self.db.commit()
        return True