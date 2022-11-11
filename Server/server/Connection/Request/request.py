from server.password_encoder  import passwEncode

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





class Message(Request):
    def __init__(self, message, toUser):
        super().__init__()

        self.message = message
        self.toUser = toUser





class FriendRequest(Request):
    def __init__(self, toUser):
        super().__init__()

        self.toUser = toUser





class BlockUser(Request):
    def __init__(self, user):
        super().__init__()

        self.user = user





class UsernameChange(Request):
    def __init__(self, newUsername, password):
        super().__init__()

        self.newWsername = newUsername
        self.password = passwEncode(password)





class PasswordChange(Request):
    def __init__(self, password, newPassword):
        super().__init__()

        self.password = passwEncode(password)
        self.newPassword = passwEncode(newPassword)





class EmailChange(Request):
    def __init__(self, newEmail, password):
        super().__init__()

        self.newEmail = newEmail
        self.password = passwEncode(password)





class ProfilePhotoChange(Request):
    def __init__(self, newPhoto):
        super().__init__()

        self.newPhoto = newPhoto





class AccountDelete(Request):
    def __init__(self, password):
        super().__init__()

        self.password = passwEncode(password)



class CancelAccountDeletion(Request):
    def __init__(self):
        super().__init__()



class LoginRequest(Request):
    def __init__(self, password, username=None, email=None):
        super().__init__()

        self.username = username
        self.email = email
        self.password = passwEncode(password)



class RegisterRequest(Request):
    def __init__(self, password, username=None, email=None):
        super().__init__()

        self.username = username
        self.email = email
        self.password = passwEncode(password)