from sqlalchemy.orm import Session

class PaymentRepository:

    def __init__(self, db: Session):
        self.db = db