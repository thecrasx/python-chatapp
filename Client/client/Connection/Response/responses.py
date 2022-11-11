import pickle




class Response:
    def encode(self):
        return pickle.dumps(self)

    def __call__(self):
        return Response




# [ FIRST RESPONSE ] SENDS TO THE CLIENT CONNECTION STATUS & BUFFER SIZE 
class ConnectConfirmation(Response):
    def __init__(self, isConnected: bool, BUFFERSIZE: int) -> None:
        super().__init__()

        self.isConnected = isConnected
        self.BUFFERSIZE = BUFFERSIZE







class CredentialsValidation(Response):
    def __init__(self, credentialsValidated: bool,
                    username=False, password=False, email=False):

        super().__init__()

        self.credentialsValidated = credentialsValidated

        if not self.credentialsValidated:
            self.username = username
            self.password = password
            self.email = email







class LoginValidation(Response):
    def __init__(self, loggedIn: bool):
        super().__init__()

        self.loggedIn = loggedIn







class RegisterValidation(Response):
    def __init__(self, registered: bool):
        super().__init__()

        self.registered = registered
        






class MessageSentConfirmation(Response):
    def __init__(self, message, isSent) -> None:
        super().__init__()

        self.message = message
        self.isSent = isSent