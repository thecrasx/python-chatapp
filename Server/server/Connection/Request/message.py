



class Message:
    def __init__(self, from_user, message=None, picture=None, to_user=None, to_group=None):
        self.text = message
        self.picture = picture
        self.from_user = from_user
        self.to_user = to_user
        self.to_group = to_group