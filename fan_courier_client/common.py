class BaseObject:
    def __init__(self, **kwargs):
        self.client_id = kwargs.pop('client_id', '7032158')
        self.username = kwargs.pop('username', 'clienttest')
        self.password = kwargs.pop('password', 'testing')

    @property
    def params(self):
        return {
            'username': self.username,
            'user_pass': self.password,
            'client_id': self.client_id,
        }
