MESSAGE_GROUP_HAVE_NOT_NAME = "El grupo debe poseer un nombre"

class GroupWithoutName(Exception):
    def __init__(self):
        self.message = MESSAGE_GROUP_HAVE_NOT_NAME
        super().__init__(self.message)