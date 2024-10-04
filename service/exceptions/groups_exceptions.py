MESSAGE_GROUP_NOT_REGISTERED = "El usuario de id {group_id} no existe"
MESSAGE_GROUP_HAVE_NOT_NAME = "El usuario debe poseer un nombre"
MESSAGE_GROUP_ALREADY_REGISTERED = "El usuario de id {group_id} ya existe"

class GroupNotRegistered(Exception):
    def __init__(self, group_id):
        self.message = MESSAGE_GROUP_NOT_REGISTERED.format(group_id)
        super().__init__(self.message)

class GroupWithoutName(Exception):
    def __init__(self):
        self.message = MESSAGE_GROUP_HAVE_NOT_NAME
        super().__init__(self.message)

class GroupAlreadyRegistered(Exception):
    def __init__(self, group_id):
        self.message = MESSAGE_GROUP_ALREADY_REGISTERED.format(group_id)
        super().__init__(self.message)