MESSAGE_PAYMENT_HAVE_NOT_CATEGORY = "El pago debe pertenecer a una categoría"

class PaymentWithoutCategory(Exception):
    def __init__(self):
        self.message = MESSAGE_PAYMENT_HAVE_NOT_CATEGORY
        super().__init__(self.message)