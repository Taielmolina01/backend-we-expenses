MESSAGE_PAYMENT_HAVE_NOT_CATEGORY = "El pago debe pertenecer a una categoría"
MESSAGE_PAYMENT_HAVE_MORE_DISTRIBUTIONS_THAN_GROUP_USERS = "El pago tiene asignado más distribuciones que personas en el grupo"
MESSAGE_PAYMENT_HAVE_LESS_DISTRIBUTIONS_THAN_GROUP_USERS = "El pago tiene asignado menos distribuciones que personas en el grupo"
MESSAGE_PAYMENT_NOT_REGISTERED = "El pago de id {payment_id} no existe"

class PaymentNotRegistered(Exception):
    def __init__(self, payment_id):
        self.message = MESSAGE_PAYMENT_NOT_REGISTERED.format(payment_id)
        super().__init__(self.message)

class PaymentWithoutCategory(Exception):
    def __init__(self):
        self.message = MESSAGE_PAYMENT_HAVE_NOT_CATEGORY
        super().__init__(self.message)

class PaymentWithMoreDistributionsThanGroupUsers(Exception):
    def __init__(self):
        self.message = MESSAGE_PAYMENT_HAVE_MORE_DISTRIBUTIONS_THAN_GROUP_USERS
        super().__init__(self.message)

class PaymentWithLessDistributionsThanGroupUsers(Exception):
    def __init__(self):
        self.message = MESSAGE_PAYMENT_HAVE_LESS_DISTRIBUTIONS_THAN_GROUP_USERS
        super().__init__(self.message)