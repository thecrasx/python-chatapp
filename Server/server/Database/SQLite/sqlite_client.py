
import pickle
import socket
import os



class SQLiteClient:
    def __init__(self, IP, PORT, FORMAT = "utf-8"):
        self.serverIP = IP
        self.serverPORT = PORT
        self.serverADDR = (self.serverIP, self.serverPORT)
        
        self.BUFFERSIZE = 16384
        self.FORMAT = FORMAT

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect(self.serverADDR)


    def sendRequest(self, request):
        req = pickle.dumps(request)
        self.server.send(req)

    
    def recive(self):
        while True:
            response = self.server.recv(self.BUFFERSIZE)
            
            if response:
                response = pickle.loads(response)
                return response["output"]


    def makeRequest(self, functionName, **kwargs):
        return {"functionName": functionName, "kwargs": kwargs}

    
    
    def isCredentialsValid(self, password, username=None, email=None):
        request = self.makeRequest("isCredentialsValid", password=password, username=username, email=email)
        self.sendRequest(request)

        return self.recive()




    def checkIfUsernameExists(self, username):
        request = self.makeRequest("checkIfUsernameExists", username=username)
        self.sendRequest(request)

        return self.recive()



    def checkIfEmailExists(self, email):
        request = self.makeRequest("checkIfEmailExists", email=email)
        self.sendRequest(request)

        return self.recive()



    #############################################



    def addUser(self, username, email, password):
        request = self.makeRequest("addUser", password=password, 
                                    username=username, email=email)
        self.sendRequest(request)

        return self.recive()


    def deleteUser(self, username=None, email=None):
        request = self.makeRequest("deleteUser", username=username, email=email)
        self.sendRequest(request)

        return self.recive()



    def getUserData(self, userId=None, username=None, email=None):
        request = self.makeRequest("getUserData", userId=userId, username=username, email=email)
        self.sendRequest(request)

        return self.recive()


    
    def getUsersData(self, username, amount):
        request = self.makeRequest("getUsersData", username=username, amount=amount)
        self.sendRequest(request)

        return self.recive()



    #############################################



    def changeUsername(self, oldUsername, newUsername):
        request = self.makeRequest("changeUsername", oldUsername=oldUsername, newUsername=newUsername)
        self.sendRequest(request)

        return self.recive()



    def changeEmail(self, oldEmail, newEmail):
        request = self.makeRequest("changeEmail", oldEmail=oldEmail, newEmail=newEmail)
        self.sendRequest(request)

        return self.recive()



    def changePassword(self, newPassword, username=None, email=None):
        request = self.makeRequest("changePassword", newPassword=newPassword, username=username, email=email)
        self.sendRequest(request)

        return self.recive()

    
    def changeProfilePhoto(self, newPhoto, username=None, email=None):
        request = self.makeRequest("changeProfilePhoto", photo=newPhoto, username=username, email=email)
        self.sendRequest(request)

        return self.recive()

    
    #############################################


    def sendFriendRequest(self, userId, friendId):
        request = self.makeRequest("sendFriendRequest", userId=userId, friendId=friendId)
        self.sendRequest(request)

        return self.recive()


    def acceptFriendRequest(self, userId, friendId):
        request = self.makeRequest("acceptFriendRequest", userId=userId, friendId=friendId)
        self.sendRequest(request)

        return self.recive()


    def declineFriendRequest(self, userId, friendId):
        request = self.makeRequest("declineFriendRequest", userId=userId, friendId=friendId)
        self.sendRequest(request)

        return self.recive()


    def cancelFriendRequest(self, userId, friendId):
        request = self.makeRequest("cancelFriendRequest", userId=userId, friendId=friendId)
        self.sendRequest(request)

        return self.recive()


    def getUserRequests(self, userId):
        request = self.makeRequest("getUserRequests", userId=userId)
        self.sendRequest(request)

        return self.recive()


    def getFriendRequests(self, userId):
        request = self.makeRequest("getFriendRequests", userId=userId)
        self.sendRequest(request)

        return self.recive()


    def getFriends(self, userId):
        request = self.makeRequest("getFriends", userId=userId)
        self.sendRequest(request)

        return self.recive()

    
    def findNewFriends(self, userId, username, amount):
        request = self.makeRequest("findNewFriends", userId=userId, username=username, amount=amount)
        self.sendRequest(request)

        return self.recive()





if __name__ == "__main__":
    os.system("cls")
    client = SQLiteClient("localhost", 10345)
    client.isCredentialsValid("MyPassword", email="Crasx")
    client.recive()
