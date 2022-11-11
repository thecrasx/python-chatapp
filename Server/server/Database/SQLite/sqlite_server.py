from threading import Thread
import socket
import pickle
from multiprocessing import Process

from server.Database.SQLite.sqlite_database import SQLite
from server.Connection.log import Log
import os

class SQLiteServer:
    def __init__(self, database, IP, PORT,
                       BUFFERSIZE = 16384, 
                       FORMAT = "utf-8",
                       LOG = True):

        self.IP = IP
        self.PORT = PORT
        self.ADDR = (self.IP, self.PORT)
        self.BUFFERSIZE = BUFFERSIZE
        self.FORMAT = FORMAT

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)

        self.database = SQLite(database)
        self.log = Log("SQLITE-SERVER", console=LOG)

        self.start()


    def start(self):
        self.server.listen()
        self.log("Listening...")
              
        self.clientHub, self.clientHubAddr = self.server.accept()
        

        if self.clientHub:
            self.log("Client Hub Connected")
            self.handle()

    
    def handle(self):
        while True:
            request = self.clientHub.recv(self.BUFFERSIZE)
            output = -1
            
            if request:
                request = pickle.loads(request)

                if request["functionName"] == "isCredentialsValid":
                    output = self.database.isCredentialsValid(**request["kwargs"])

                
                
                elif request["functionName"] == "checkIfUsernameExists":
                    output = self.database.checkIfUsernameExists(**request["kwargs"])
                    


                elif request["functionName"] == "checkIfEmailExists":
                    output = self.database.checkIfEmailExists(**request["kwargs"])

                
                
                elif request["functionName"] == "addUser":
                    output = self.database.addUser(**request["kwargs"])
                
                
                
                elif request["functionName"] == "deleteUser":
                    output = self.database.deleteUser(**request["kwargs"])
                
                
                
                elif request["functionName"] == "changeUsername":
                    output = self.database.changeUsername(**request["kwargs"])
                
                
                
                elif request["functionName"] == "changeEmail":
                    output = self.database.changeEmail(**request["kwargs"])
                
                
                
                elif request["functionName"] == "changePassword":
                    output = self.database.changePassword(**request["kwargs"])

                
                elif request["functionName"] == "changeProfilePhoto":
                    output = self.database.changeProfilePhoto(**request["kwargs"])
            
                
                elif request["functionName"] == "getUserData":
                    output = self.database.getUserData(**request["kwargs"])

                
                elif request["functionName"] == "getUsersData":
                    output = self.database.getUsersData(**request["kwargs"])


                elif request["functionName"] == "sendFriendRequest":
                    output = self.database.sendFriendRequest(**request["kwargs"])


                elif request["functionName"] == "acceptFriendRequest":
                    output = self.database.acceptFriendRequest(**request["kwargs"])
            

                elif request["functionName"] == "declineFriendRequest":
                    output = self.database.declineFriendRequest(**request["kwargs"])
                    
                elif request["functionName"] == "cancelFriendRequest":
                    output = self.database.cancelFriendRequest(**request["kwargs"])

                elif request["functionName"] == "getUserRequests":
                    output = self.database.getUserRequests(**request["kwargs"])


                elif request["functionName"] == "getFriendRequests":
                    output = self.database.getFriendRequests(**request["kwargs"])

                
                elif request["functionName"] == "getFriends":
                    output = self.database.getFriends(**request["kwargs"])


                elif request["functionName"] == "findNewFriends":
                    output = self.database.findNewFriends(**request["kwargs"])








            if output != -1:
                request["output"] = output

                response = pickle.dumps(request)
                self.clientHub.send(response)







if __name__ == "__main__":
    os.system("cls")
    server = SQLiteServer("test", "localhost", 9999)
    server.start()