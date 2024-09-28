from sqlalchemy.orm import Session

class UsersByGroupRepository:

    def __init__(self, db: Session):
        self.db = db