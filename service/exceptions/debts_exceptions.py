MESSAGE_DEBT_IS_NEGATIVE = "La deuda no puede no ser un numero natural"
MESSAGE_DEBT_NOT_REGISTERED = "La deuda de id {debt_id} no existe"
MESSAGE_DEBT_ALREADY_REGISTERED = "La deuda de id {debt_id} ya existe"

class DebtIsInvalid(Exception):
    def __init__(self):
        self.message = MESSAGE_DEBT_IS_NEGATIVE
        super().__init__(self.message)

class DebtNotRegistered(Exception):
    def __init__(self, debt_id):
        self.message = MESSAGE_DEBT_NOT_REGISTERED.format(debt_id=debt_id)
        super().__init__(self.message)

class DebtAlreadyRegistered(Exception):
    def __init__(self, debt_id):
        self.message = MESSAGE_DEBT_ALREADY_REGISTERED.format(debt_id=debt_id)
        super().__init__(self.message)