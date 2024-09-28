MESSAGE_DEBT_IS_NEGATIVE = "La deuda no puede no ser un numero natural"

class DebtIsInvalid(Exception):
    def __init__(self):
        self.message = MESSAGE_DEBT_IS_NEGATIVE
        super().__init__(self.message)