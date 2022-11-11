




class DataLoad:
    def __init__(self, request: object):
        self.request = request
        self.loadFriends()


    def loadFriends(self):
        self.request.getFriends()