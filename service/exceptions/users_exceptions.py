MESSAGE_USER_NOT_REGISTERED = "El usuario de email {user_email} no existe"
MESSAGE_USER_HAVE_NOT_NAME = "El usuario debe poseer un nombre"
MESSAGE_USER_ALREADY_REGISTERED = "El usuario de id {user_email} ya existe"

class UserNotRegistered(Exception):
    def __init__(self, user_email):
        self.message = MESSAGE_USER_NOT_REGISTERED.format(user_email)
        super().__init__(self.message)

class UserWithoutName(Exception):
    def __init__(self):
        self.message = MESSAGE_USER_HAVE_NOT_NAME
        super().__init__(self.message)

class UserAlreadyRegistered(Exception):
    def __init__(self, user_email):
        self.message = MESSAGE_USER_ALREADY_REGISTERED.format(user_email)
        super().__init__(self.message)