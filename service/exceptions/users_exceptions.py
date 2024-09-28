MESSAGE_USER_HAVE_NOT_NAME = "El usuario debe poseer un nombre"

class UserWithoutName(Exception):
    def __init__(self):
        self.message = MESSAGE_USER_HAVE_NOT_NAME
        super().__init__(self.message)