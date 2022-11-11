import pickle




class Response:
    def encode(self):
        return pickle.dumps(self)

    def __call__(self):
        return "Response"





# [ FIRST RESPONSE ] SENDS TO THE CLIENT CONNECTION STATUS & BUFFER SIZE 
class ConnectConfirmation(Response):
    def __init__(self, isConnected: bool, BUFFERSIZE: int):
        super().__init__()

        self.isConnected = isConnected
        self.BUFFERSIZE = BUFFERSIZE

    def type(self):
        return "ConnectConfirmation"








class CredentialsValidation(Response):
    def __init__(self, credentialsValidated: bool,
                    username=False, password=False, email=False):
        super().__init__()

        self.credentialsValidated = credentialsValidated

        if not self.credentialsValidated:
            self.username = username
            self.password = password
            self.email = email

    def type(self):
        return "CredentialsValidation"




class LoginValidation(Response):
    def __init__(self, loggedIn: bool):
        super().__init__()
        
        self.loggedIn = loggedIn

    def type(self):
        return "LoginValidation"





class RegisterValidation(Response):
    def __init__(self, registered: bool, username=True, email=True):
        super().__init__()

        self.registered = registered
        
        self.username = username
        self.email = email

    def type(self):
        return "RegisterValidation"
        



class MessageSentConfirmation(Response):
    def __init__(self, message, isSent):
        super().__init__()
        self.message = message
        self.isSent = isSent



class UsernameChangeValidation(Response):
    def __init__(self, changed, newUsername=True, password=True):
        super().__init__()

        self.changed = changed
        self.newUsername = newUsername
        self.password = password

    def type(self):
        return "UsernameChangeValidation"



class EmailChangeValidation(Response):
    def __init__(self, changed, newEmail=True, password=True):
        super().__init__()

        self.changed = changed
        self.newEmail = newEmail
        self.password = password

    def type(self):
        return "EmailChangeValidation"




class PasswordChangeValidation(Response):
    def __init__(self, changed, password=True):
        super().__init__()

        self.changed = changed
        self.password = password

    def type(self):
        return "PasswordChangeValidation"


class ProfilePhotoChangeValidation(Response):
    def __init__(self, changed):
        super().__init__()

        self.changed = changed

    def type(self):
        return "ProfilePhotoChangeValidation"


class UserData(Response):
    def __init__(self, userId, username, email, photo):
        super().__init__()

        self.userId = userId
        self.username = username
        self.email = email
        self.photo = photo

    def type(self):
        return "UserData"


class UsersData(Response):
    def __init__(self, usersData):
        super().__init__()

        self.usersData = usersData

    def type(self):
        return "UsersData"


# 'NewFriends' is a response for request 'FindNewFriends'
class NewFriends(Response):
    def __init__(self, newFriends):
        super().__init__()

        self.newFriends = newFriends

    def type(self):
        return "NewFriends"


class NewFriendRequest(Response):
    def __init__(self, friend):
        super().__init__()

        self.friend = friend

    def type(self):
        return "NewFriendRequest"


class FriendRequestSent(Response):
    def __init__(self, sent, friendId):
        super().__init__()

        self.sent = sent
        self.friendId = friendId

    def type(self):
        return "FriendRequestSent"

    

class FriendRequestAccepted(Response):
    def __init__(self, accepted, friend):
        super().__init__()

        self.accepted = accepted
        self.friend = friend

    def type(self):
        return "FriendRequestAccepted"



class FriendRequestDeclined(Response):
    def __init__(self, declined, friendId):
        super().__init__()

        self.declined = declined
        self.friendId = friendId

    def type(self):
        return "FriendRequestDeclined"



class FriendRequestCanceled(Response):
    def __init__(self, canceled, friendId):
        super().__init__()

        self.canceled = canceled
        self.friendId = friendId

    def type(self):
        return "FriendRequestCanceled"


class Friends(Response):
    def __init__(self, friends):
        super().__init__()
        self.friends = friends

    def type(self):
        return "Friends"