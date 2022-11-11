from server.password_encoder import passw_encode



class Credentials:
    def __init__(self, password, username = None, email = None):
        self.username = username
        self.email = email
        self.password = passw_encode(password)