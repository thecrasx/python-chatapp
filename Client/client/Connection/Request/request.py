from urllib import request
from client.Connection.password_encoder import passwEncode
from client.Connection.Request.requests import *





class Request:
    def __init__(self, server, signals):
        self.server = server
        self.signals = signals

        self.signals.requestSignal.sendFriendRequest.connect(self.sendFriendRequest)
        self.signals.requestSignal.acceptFriendRequest.connect(self.acceptFriendRequest)
        self.signals.requestSignal.declineFriendRequest.connect(self.declineFriendRequest)
        self.signals.requestSignal.cancelFriendRequest.connect(self.cancelFriendRequest)


    def getUserData(self, password, username=None, email=None):
        request = GetUserData(password = passwEncode(password), 
                                    username = username,
                                    email = email)

        self.server.send(request.encode())

    
    def getUsersData(self, username, amount):
        request = GetUsersData(username=username, amount=amount)

        self.server.send(request.encode())
    
    def isCredentialsValid(self, password, username=None, email=None):
        request = CredentialsValidation(password = passwEncode(password), 
                                username = username,
                                email = email)

        self.server.send(request.encode())
    
    
    def login(self, password, username=None, email=None):
        request = LoginRequest(password = passwEncode(password), 
                                username = username,
                                email = email)

        self.server.send(request.encode())
    
    
    def register(self, email, username, password, dateOfBirthday):
        request = RegisterRequest(email = email, 
                                username = username,
                                password = passwEncode(password),
                                dateOfBirthday = dateOfBirthday)

        self.server.send(request.encode())


    def changeUsername(self, newUsername, password):
        request = UsernameChange(newUsername = newUsername,
                                password = passwEncode(password))

        self.server.send(request.encode())


    
    def changeEmail(self, newEmail, password):
        request = EmailChange(newEmail = newEmail,
                            password = passwEncode(password))

        self.server.send(request.encode())


    def changePassword(self, password, newPassword):
        request = PasswordChange(password = passwEncode(password),
                            newPassword = passwEncode(newPassword))

        self.server.send(request.encode())


    def changeProfilePhoto(self, photo):
        request = ProfilePhotoChange(photo)

        self.server.send(request.encode())


    def getFriendData(self, friendId):
        request = GetFriendData(friendId)

        self.server.send(request.encode())

    
    def findNewFriends(self, username, amount):
        request = FindNewFriends(username=username,
                                amount=amount)

        self.server.send(request.encode())


    def sendFriendRequest(self, friendId):
        request = SendFriendRequest(friendId)

        self.server.send(request.encode())

    
    def acceptFriendRequest(self, friendId):
        request = AcceptFriendRequest(friendId)

        self.server.send(request.encode())


    def declineFriendRequest(self, friendId):
        request = DeclineFriendRequest(friendId)

        self.server.send(request.encode())


    def cancelFriendRequest(self, friendId):
        request = CancelFriendRequest(friendId)

        self.server.send(request.encode())

    
    def getFriends(self):
        request = GetFriends()

        self.server.send(request.encode())
