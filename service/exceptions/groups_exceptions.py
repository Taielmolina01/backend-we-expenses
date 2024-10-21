MESSAGE_GROUP_NOT_REGISTERED = "El grupo no existe"
MESSAGE_GROUP_HAVE_NOT_NAME = "El grupo debee poseer un nombre"

class GroupNotRegistered(Exception):
    def __init__(self):
        self.message = MESSAGE_GROUP_NOT_REGISTERED
        super().__init__(self.message)

class GroupWithoutName(Exception):
    def __init__(self):
        self.message = MESSAGE_GROUP_HAVE_NOT_NAME
        super().__init__(self.message)