import imp
from server.Connection.Request.request import Request
from server.Connection.connections import Connections
from server.Connection.Request.request_handler import RequestHandler
from server.exceptions import ClientDisconnected
from server.errors import BadRequestError
from server.Connection.Response.response import ConnectConfirmation, Response
from server.Database.SQLite.sqlite_client import SQLiteClient
from server.Connection.client_credentials import ClientCredentials


import threading
import datetime
import pickle








class ClientHandler:
    def __init__(self, client, addr, connections, database, BUFFERSIZE,
                        MAX_LOGIN_ATTEMPTS = 5):
        
        self.client = client
        self.clientAddress = addr
        self.clientIP = addr[0]
        self.clientPORT = addr[1]

        self.clientCredentials = ClientCredentials()

        self.database = database

        if self.database == 'sqlite':
            self.database = SQLiteClient("localhost", 10345)

        self.requestHandler = RequestHandler(client=self.client,
                                            clientCredentials=self.clientCredentials,
                                            clientAddress=self.clientAddress,
                                            connections=connections,
                                            database=self.database)
        
        self.BUFFSIZE = BUFFERSIZE
        self.MAX_LOGIN_ATTEMPTS = MAX_LOGIN_ATTEMPTS

        self.clientConnected = False
        self.clientValidated = False

        


        self.handleClient()
    
    
    
    def sendConnectConfirmation(self):
        return ConnectConfirmation(isConnected=True, BUFFERSIZE=self.BUFFSIZE).encode()    
    
    
    
    def processReceivedData(self, receivedData):
        try:
            receivedData = pickle.loads(receivedData)
            print(receivedData)
            
            if receivedData() == "Request":
                self.requestHandler.handle(receivedData)

            elif receivedData() == "Response":
                pass

            else:
                raise BadRequestError()
            
        except:
            raise BadRequestError()


    
    def handleClient(self):
        try:
            self.clientConnected = True
            self.client.send(self.sendConnectConfirmation())

            while not self.clientValidated:
                receivedData = self.client.recv(self.BUFFSIZE)

                self.processReceivedData(receivedData)

        except ConnectionResetError:
            print(f"Client [ {self.clientIP}:{self.clientPORT} ] forcibly disconnected")
            
        