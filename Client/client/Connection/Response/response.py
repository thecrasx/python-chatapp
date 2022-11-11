from client.Connection.Response.responses import *


from client.Window.UI.Elements.custom_signals import ResponseSignal






class Response:
    def __init__(self, client, server):
        self.client = client
        self.server = server
        self.signals = self.client.signals

        self.responseSignal = self.signals.responseSignal

        self.signals.responseSignal.newResponse.connect(self.__onNewResponse)



    def __onNewResponse(self, response):
        self.load(response)



    def load(self, response):
        print(response)

        if response.type() == "ConnectConfirmation":
            if response.isConnected:
                self.client.connected = True
                self.client.BUFFSIZE = response.BUFFERSIZE

                self.signals.connectionSignal.connected.emit(True)
                print("Successfully connected")
            
            else:
                self.signals.connectionSignal.connected.emit(False)


        elif response.type() == "CredentialsValidation":
            if response.credentialsValidated:
                print("Valid Credentials")
                self.responseSignal.credentialsValidated.emit(True)
            
            else:
                print("Invalid Credentials")
                self.responseSignal.credentialsValidated.emit(False)



        elif response.type() == "LoginValidation":
            if response.loggedIn:
                print("Login Succeeded")
                self.responseSignal.loginValidated.emit(True)
            
            else:
                print("Login Failed")
                self.responseSignal.loginValidated.emit(False)
        
        
        
        elif response.type() == "RegisterValidation":
            if response.registered:
                self.responseSignal.registerValidated.emit(True)
            
            else:
                self.responseSignal.registerValidated.emit(False)

                if not response.username:
                    self.responseSignal.usernameTaken.emit()

                if not response.email:
                    self.responseSignal.emailTaken.emit()


        elif response.type() == "UsernameChangeValidation":
            if response.changed:
                self.responseSignal.usernameChangeValidated.emit(True)
            
            else:
                self.responseSignal.usernameChangeValidated.emit(False)

                if not response.newUsername:
                    self.responseSignal.newUsernameTaken.emit()

                if not response.password:
                    self.responseSignal.invalidPassword_U.emit()


        elif response.type() == "EmailChangeValidation":
            if response.changed:
                self.responseSignal.emailChangeValidated.emit(True)
            
            else:
                self.responseSignal.emailChangeValidated.emit(False)

                if not response.newEmail:
                    self.responseSignal.newEmailTaken.emit()

                if not response.password:
                    self.responseSignal.invalidPassword_E.emit()


        elif response.type() == "PasswordChangeValidation":
            if response.changed:
                self.responseSignal.passwordChangeValidated.emit(True)
                
            else:
                self.responseSignal.passwordChangeValidated.emit(False)

                if not response.password:
                    self.responseSignal.invalidPassword.emit()


        elif response.type() == "UserData":
            self.responseSignal.userData.emit(response)


        elif response.type() == "UsersData":
            self.responseSignal.usersData.emit(response.usersData)
                
        elif response.type() == "NewFriends":
            self.responseSignal.newFriends.emit(response.newFriends)

        
        elif response.type() == "NewFriendRequest":
            self.responseSignal.newFriendRequest.emit(response.friend)


        elif response.type() == "FriendRequestSent":
            if response.sent:
                self.responseSignal.friendRequestSent.emit(response.friendId)


        elif response.type() == "FriendRequestAccepted":
            if response.accepted:
                self.responseSignal.friendRequestAccepted.emit(response.friend)


        elif response.type() == "FriendRequestDeclined":
            if response.declined:
                self.responseSignal.friendRequestDeclined.emit(response.friendId)


        elif response.type() == "FriendRequestCanceled":
            if response.canceled:
                self.responseSignal.friendRequestCanceled.emit(response.friendId)


        elif response.type() == "Friends":
            self.responseSignal.friends.emit(response.friends)



        