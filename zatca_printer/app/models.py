from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, rep_code, name):
        self.id = str(id)
        self.rep_code = rep_code
        self.name = name
