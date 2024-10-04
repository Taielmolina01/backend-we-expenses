MESSAGE_USER_NOT_REGISTERED = "El usuario de id {user_id} no pertenece al grupo de id {group_id}"

class UserNotRegisteredInGroup(Exception):
    def __init__(self, user_id, group_id):
        self.message = MESSAGE_USER_NOT_REGISTERED.format(user_id, group_id)
        super().__init__(self.message)