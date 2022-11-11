from server.errors import BadRequestError
from server.exceptions import ClientDisconnected, InvalidCredentials
from server.Connection.Response.response import *
from server.Database.database import Database




class RequestHandler:
    def __init__(self, client, clientCredentials, clientAddress, connections, database, FORMAT = "utf-8"):
        self.connections = connections
        self.FORMAT = FORMAT

        self.database = database
        self.client = client
        self.clientAddress = clientAddress
        self.clientCredentials = clientCredentials

        self.clientValidated = False


    def __addClientToConnections(self):
        if not self.clientValidated:
            if self.clientCredentials.userId:
                self.connections.add(userId = self.clientCredentials.userId,
                                    socket = self.client,
                                    address = self.clientAddress)

                self.clientValidated = True

    
    def getClientData(self, userId):
        return self.connections.get(userId)
    
    
    def handle(self, request: object):
        
        if request.type() == "CredentialsValidation":
            if self.database.isCredentialsValid(request.password, request.username, request.email):
                self.client.send(CredentialsValidation(True).encode())
            
            else:
                self.client.send(CredentialsValidation(False).encode())


        
        elif request.type() == "LoginRequest":
            if self.database.isCredentialsValid(request.password, request.username, request.email):
                self.client.send(LoginValidation(True).encode())

                userData = self.database.getUserData(username=request.username)

                self.clientCredentials.userId = userData["user_id"]
                self.clientCredentials.username = request.username
                self.clientCredentials.email = request.email

                self.__addClientToConnections()

                
            
            else:
                self.client.send(LoginValidation(False).encode())
                
                # Returns -1 only when login fails
                return -1


        elif request.type() == "RegisterRequest":
            username = True
            email = True
            
            if self.database.checkIfUsernameExists(request.username):
                username = False

            if self.database.checkIfEmailExists(request.email):
                email = False

            if not email or not username:
                self.client.send(RegisterValidation(False, username, email).encode())

            else:
                if self.database.addUser(request.username, request.email, request.password):
                    self.client.send(RegisterValidation(True).encode())

                    userData = self.database.getUserData(username=request.username)

                    self.clientCredentials.userId = userData["user_id"]
                    self.clientCredentials.username = request.username
                    self.clientCredentials.email = request.email

                    self.__addClientToConnections()

                else:
                    self.client.send(RegisterValidation(False).encode())


        
        elif request.type() == "UsernameChange":
            username = True
            password = True

            if not self.database.isCredentialsValid(request.password, self.clientCredentials.username):
                password = False
       
            if self.database.checkIfUsernameExists(request.newUsername):
                username = False

            if username and password:
                if self.database.changeUsername(self.clientCredentials.username, request.newUsername):
                    self.client.send(UsernameChangeValidation(True).encode())

                    self.clientCredentials.username = request.newUsername
                else:
                    self.client.send(UsernameChangeValidation(False).encode())

            else:
                self.client.send(UsernameChangeValidation(False, username, password).encode())


        
        elif request.type() == "EmailChange":
            email = True
            password = True

            if not self.database.isCredentialsValid(request.password, email = self.clientCredentials.email):
                password = False
       
            if self.database.checkIfEmailExists(request.newEmail):
                email = False

            if email and password:
                if self.database.changeEmail(self.clientCredentials.email, request.newEmail):
                    self.client.send(EmailChangeValidation(True).encode())

                    self.clientCredentials.email = request.newEmail

                else:
                    self.client.send(EmailChangeValidation(False).encode())

            else:
                self.client.send(EmailChangeValidation(False, email, password).encode())



        
        elif request.type() == "PasswordChange":
            password = True

            if not self.database.isCredentialsValid(request.password, self.clientCredentials.username, self.clientCredentials.email):
                password = False

            if password:
                if self.database.changePassword(request.newPassword, self.clientCredentials.username, self.clientCredentials.email):
                    self.client.send(PasswordChangeValidation(True).encode())
                else:
                    self.client.send(PasswordChangeValidation(False).encode())

            else:
                self.client.send(PasswordChangeValidation(False, password).encode())


        elif request.type() == "ProfilePhotoChange":
            
            if self.database.changeProfilePhoto(request.newPhoto, self.clientCredentials.username, self.clientCredentials.email):
                self.client.send(ProfilePhotoChangeValidation(True).encode())

            else:
                self.client.send(ProfilePhotoChangeValidation(False).encode())


        elif request.type() == "GetUserData":
            password = True

            if not self.database.isCredentialsValid(request.password, self.clientCredentials.username, self.clientCredentials.email):
                password = False

            
            if password:
                userData = self.database.getUserData(username=self.clientCredentials.username, email=self.clientCredentials.email)

                if userData:
                    userId = userData["user_id"]
                    username = userData["username"]
                    email = userData["email"]
                    photo = userData["profile_photo"]

                    self.clientCredentials.userId = userId

                    self.client.send(UserData(userId, username, email, photo).encode())

                else:
                    self.client.send(UserData(None, None, None, None).encode())


        elif request.type() == "GetUsersData":
            usersData = self.database.getUsersData(request.username, request.amount)

            self.client.send(UsersData(usersData).encode())


        elif request.type() == "FindNewFriends":
            newFriends = self.database.findNewFriends(self.clientCredentials.userId, request.username, request.amount)

            self.client.send(NewFriends(newFriends).encode())

        
        elif request.type() == "SendFriendRequest":
            if self.database.sendFriendRequest(self.clientCredentials.userId, request.friendId):
                self.client.send(FriendRequestSent(True, request.friendId).encode())

                recipient = self.getClientData(request.friendId)
                
                
                if recipient:
                    userData = self.database.getUserData(userId=self.clientCredentials.userId)

                    if userData:
                        recipient.client.send(NewFriendRequest(userData).encode())
                    

            else:
                self.client.send(FriendRequestSent(False, request.friendId).encode())


        
        elif request.type() == "AcceptFriendRequest":
            if self.database.acceptFriendRequest(self.clientCredentials.userId, request.friendId):
                self.client.send(FriendRequestAccepted(True, request.friendId).encode())
                
                recipient = self.getClientData(request.friendId)
                
                if recipient:
                    userData = self.database.getUserData(self.clientCredentials.userId)
                    recipient.client.send(FriendRequestAccepted(True, userData).encode())
                    
            else:
                self.client.send(FriendRequestAccepted(False, request.friendId).encode())

        
        elif request.type() == "DeclineFriendRequest":
            if self.database.declineFriendRequest(self.clientCredentials.userId, request.friendId):
                self.client.send(FriendRequestDeclined(True, request.friendId).encode())

                recipient = self.getClientData(request.friendId)
                
                if recipient:
                    recipient.client.send(FriendRequestDeclined(True, self.clientCredentials.userId).encode())

            else:
                self.client.send(FriendRequestDeclined(False, request.friendId).encode())

        
        elif request.type() == "CancelFriendRequest":
            if self.database.cancelFriendRequest(self.clientCredentials.userId, request.friendId):
                self.client.send(FriendRequestCanceled(True, request.friendId).encode())

                recipient = self.getClientData(request.friendId)
                
                if recipient:
                    recipient.client.send(FriendRequestCanceled(True, self.clientCredentials.userId).encode())

            else:
                self.client.send(FriendRequestCanceled(False, request.friendId).encode())


        
        elif request.type() == "GetFriends":
            data = self.database.getFriends(self.clientCredentials.userId)
            
            if data:
                self.client.send(Friends(data).encode())
                


            








    #############################################################################
    #                                 FUNCTIONS                                 #
    #############################################################################


    def isCredentialsValid(self, password, username=None, email=None) -> bool:
        return self.database.isCredentialsValid(password, username, email)
    