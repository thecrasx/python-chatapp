################### PySide6 ###################
from PySide6.QtCore import QObject, Signal

from client.Connection.Response.responses import Response
from client.Connection.Request.requests import Request




class AnimationSignal(QObject):
    pauseFinished = Signal()
    alphaMaximum = Signal()


class WindowSignal(QObject):
    launch = Signal()
    windowVisible = Signal(bool)



class CustomSignal(QObject):
    
    # ChatInput
    lineCountChanged = Signal()
    chatInputInFocus = Signal(bool)
    keyEnterPressed = Signal(str)

    currentChatChanged = Signal(object)
    closeChatBtnPressed = Signal(object)


class AccountSignal(QObject):
    loggedIn = Signal()
    registered = Signal()


class ConnectionSignal(QObject):
    connected = Signal(bool)
    connectedToServer = Signal(bool)
    connectionRefused = Signal()
    connectionTimeout = Signal()
    connectionTimeoutExpired = Signal()



class RequestSignal(QObject):
    requestSent = Signal()

    sendFriendRequest = Signal(int)
    acceptFriendRequest = Signal(int)
    declineFriendRequest = Signal(int)
    cancelFriendRequest = Signal(int)


class ResponseSignal(QObject):
    newResponse = Signal(Request)
    connected = Signal(bool)
    credentialsValidated = Signal(bool)
    loginValidated = Signal(bool)
    
    registerValidated = Signal(bool)
    usernameTaken = Signal()
    emailTaken = Signal()

    usernameChangeValidated = Signal(bool)
    emailChangeValidated = Signal(bool)
    passwordChangeValidated = Signal(bool)

    newUsernameTaken = Signal()
    newEmailTaken = Signal()

    invalidPassword = Signal()
    
    # Username
    invalidPassword_U = Signal()
    
    # Email
    invalidPassword_E = Signal()

    userData = Signal(object)
    usersData = Signal(list)

    friendRequests = Signal(list)
    newFriends = Signal(list)
    newFriendRequest = Signal(dict)

    friends = Signal(list)
    friendRequestSent = Signal(int)
    friendRequestAccepted = Signal(int)
    friendRequestDeclined = Signal(int)
    friendRequestCanceled = Signal(int)


class FriendsSignal(QObject):
    searchInputDelayed = Signal()
    searchInputChanged = Signal()
    searchNoInput = Signal()

    



class Signals:
    windowSignal = WindowSignal()
    customSignal = CustomSignal()
    friendsSignal = FriendsSignal()
    
    connectionSignal =  ConnectionSignal()
    requestSignal = RequestSignal()
    responseSignal = ResponseSignal()

    accountSignal = AccountSignal()

