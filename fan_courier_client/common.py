class BaseObject:
    def __init__(self, client_id=None, username=None, user_pass=None):
        self.client_id = client_id
        self.username = username
        self.password = user_pass

    @property
    def params(self):
        return {
            'username': self.username,
            'user_pass': self.password,
            'client_id': self.client_id,
        }
