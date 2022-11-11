import socket
import pickle
from time import sleep


from client.Connection.Response.response import Response
from client.Connection.Request.request import Request
from client.Window.UI.Elements.custom_signals import ConnectionSignal
from client.Connection.server_listener import ServerListener
from client.Connection.connection_timeout import ConnectionTimeout

from PySide6.QtCore import QThread

    

class Client:
    def __init__(self, IP, PORT, signals, FORMAT = "utf-8"):
        self.BUFFSIZE = 16384
        self.FORMAT = FORMAT
        
        # UI
        self.signals = signals
        self.signals.connectionSignal.connectedToServer.connect(self.__onConnect)
        self.signals.connectionSignal.connectionRefused.connect(self.__onConnectionRefused)
        
        # SERVER
        self.connected = False
        self.autoReconnect = True

        self.serverIP = IP
        self.serverPORT = PORT
        self.serverADDR = (self.serverIP, self.serverPORT)
        
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__connectThread = ConnectThread(self.server, self.serverADDR, self.signals)
        
        # Server Listener
        self.serverListener = ServerListener(server=self.server, 
                                            signals=self.signals,
                                            connected=self.connected,
                                            buffersize=self.BUFFSIZE)

      
        # Connection Timeout
        self.connectionTimeout = ConnectionTimeout()
        self.connectionTimeout.signals.connectionTimeout.connect(self.__onConnectionTimeout)
        self.connectionTimeout.signals.connectionTimeoutExpired.connect(self.__onConnectionTimeoutExpired)
        
        self.response = Response(self, self.server)
        self.request = Request(self.server, self.signals)


        # Connection Refused Counter Resets On Connection Success
        self.__connectionRefusedCounter = 0


    def setupServer(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__connectThread.server = self.server
        self.serverListener.server = self.server
        self.response.server = self.server
        self.request.server = self.server

    
    
    def disconnect(self):
        self.server.close()
    
    
    def connect(self):  
        if not self.connected:
            self.__connectThread.start()


    def listen(self):
        if not self.serverListener.listening:
            self.serverListener.start()
    
    
    
    def sendRequest(self, request): 
        if self.connected:
            self.server.send(request)



    def timeout(self, time: int = 30):
        # time (sec)
        self.__connectionRefusedCounter += 1

        if time > 0:
            if time == 30:
                if self.__connectionRefusedCounter == 1:
                    time = 10
                
                elif self.__connectionRefusedCounter >= 2:
                    time = 30
                
                elif self.__connectionRefusedCounter >= 5:
                    time = 60

            print("Connection Timeout")
            self.connectionTimeout.timeout(time)
                

    
    def __onConnect(self, connected):
        if connected:
            print("[Client] Connected")
            self.connected = True
            self.__connectionRefusedCounter = 0
            self.listen()

        else:
            print("[Client] Disconnected")
            self.connected = False

    
    
    def __onConnectionRefused(self):
        if self.connected:
            self.signals.connectionSignal.connectedToServer.emit(False)
            self.disconnect()
            self.setupServer()
        
        self.timeout(1)

    
    def __onConnectionTimeout(self):
        pass


    def __onConnectionTimeoutExpired(self):
        if self.autoReconnect:
            self.connect()





class ConnectThread(QThread):
    def __init__(self, server, addr, signals):
        super().__init__()

        self.signals = signals
        self.server = server
        self.addr = addr

    def run(self):
        try:
            self.server.connect(self.addr)
            self.signals.connectionSignal.connectedToServer.emit(True)
        
        except ConnectionRefusedError:
            self.signals.connectionSignal.connectionRefused.emit()