import pickle



class Request:
    def encode(self):
        return pickle.dumps(self)

    def __call__(self):
        return "Request"





class CredentialsValidation(Request):
    def __init__(self,username=False, password=False, email=False):
        super().__init__()

        self.username = username
        self.password = password
        self.email = email

    def type(self):
        return "CredentialsValidation"




class GetUserData(Request):
    def __init__(self, password, username=None, email=None):
        super().__init__()

        self.password = password
        self.username = username
        self.email = email

    def type(self):
        return "GetUserData"


class GetUsersData(Request):
    def __init__(self, username, amount):
        super().__init__()

        self.username = username
        self.amount = amount

    def type(self):
        return "GetUsersData"



class GetFriendData(Request):
    def __init__(self, friendId):
        super().__init__()

        self.friendId = friendId

    def type(self):
        return "GetFriendData"


class Message(Request):
    def __init__(self, message, toUser):
        super().__init__()

        self.message = message
        self.toUser = toUser

    def type(self):
        return ""




class FriendRequest(Request):
    def __init__(self, toUser):
        super().__init__()

        self.toUser = toUser

    def type(self):
        return ""




class BlockUser(Request):
    def __init__(self, user):
        super().__init__()

        self.user = user

    def type(self):
        return "BlockUser"




class UsernameChange(Request):
    def __init__(self, newUsername, password):
        super().__init__()

        self.newUsername = newUsername
        self.password = password

    def type(self):
        return "UsernameChange"




class PasswordChange(Request):
    def __init__(self, password, newPassword):
        super().__init__()

        self.password = password
        self.newPassword = newPassword

    def type(self):
        return "PasswordChange"




class EmailChange(Request):
    def __init__(self, newEmail, password):
        super().__init__()

        self.newEmail = newEmail
        self.password = password

    def type(self):
        return "EmailChange"




class ProfilePhotoChange(Request):
    def __init__(self, newPhoto):
        super().__init__()

        self.newPhoto = newPhoto

    def type(self):
        return "ProfilePhotoChange"




class AccountDelete(Request):
    def __init__(self, password):
        super().__init__()

        self.password = password

    def type(self):
        return "AccountDelete"


class CancelAccountDeletion(Request):
    def __init__(self):
        super().__init__()


    def type(self):
        return "CancelAccountDeletion"


class RegisterRequest(Request):
    def __init__(self, email, username, password, dateOfBirthday):
        super().__init__()

        self.email = email
        self.username = username
        self.password = password
        self.dateOfBirthday = dateOfBirthday

    def type(self):
        return "RegisterRequest"


class LoginRequest(Request):
    def __init__(self, password, username=None, email=None):
        super().__init__()

        self.username = username
        self.email = email
        self.password = password
    
    def type(self):
        return "LoginRequest"


class FindNewFriends(Request):
    def __init__(self, username, amount=5):
        super().__init__()

        self.amount = amount
        self.username = username
    
    def type(self):
        return "FindNewFriends"


class SendFriendRequest(Request):
    def __init__(self, friendId):
        super().__init__()
        self.friendId = friendId

    def type(self):
        return "SendFriendRequest"


class AcceptFriendRequest(Request):
    def __init__(self, friendId):
        super().__init__()
        self.friendId = friendId

    def type(self):
        return "AcceptFriendRequest"


class DeclineFriendRequest(Request):
    def __init__(self, friendId):
        super().__init__()
        self.friendId = friendId

    def type(self):
        return "DeclineFriendRequest"


class CancelFriendRequest(Request):
    def __init__(self, friendId):
        super().__init__()
        self.friendId = friendId

    def type(self):
        return "CancelFriendRequest"


class GetFriendRequests(Request):
    def __init__(self):
        super().__init__()

    def type(self):
        return "GetFriendRequests"


class GetFriends(Request):
    def __init__(self):
        super().__init__()

    def type(self):
        return "GetFriends"