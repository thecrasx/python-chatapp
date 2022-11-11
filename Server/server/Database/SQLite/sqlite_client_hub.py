from server.Connection.log import Log
from threading import Thread
import socket
import pickle
import os

from server.Connection.Response.response import *




class SQLiteClientHub:
    def __init__(self, IP, PORT, SERVER_IP, SERVER_PORT, 
                        BUFFERSIZE=4096, FORMAT="utf-8", LOG=True):
        
        self.IP = IP
        self.PORT = PORT
        self.ADDR = (self.IP, self.PORT)

        self.BUFFERSIZE = 16384
        self.FORMAT = FORMAT

        self.clientsConnected = 0
        self.clients = {} # {"client_id", socket}
        
        self.hub = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.hub.bind(self.ADDR)
        
        self.log = Log("SQLITE-CLIENT-HUB", console=LOG)
        
        # SQLiteServer
        self.serverIP = SERVER_IP
        self.serverPORT = SERVER_PORT
        self.serverADDR = (self.serverIP, self.serverPORT)
        

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect(self.serverADDR)

        self.log("Connected to the server")

        self.start()

        



    def start(self):
        serverThread = Thread(target=self.handleServer)
        serverThread.start()

        self.hub.listen()
        self.log("Listening...")

        while True:
            client, addr = self.hub.accept()
            self.clientsConnected += 1
            client_id = self.clientsConnected
            
            self.log(f"({client_id}) Client <{addr[0]}:{addr[1]}> has connected")

            self.clients[self.clientsConnected] = client

            clientThread = Thread(target=self.handleClient, 
                            args=(client, addr, client_id), daemon=True)
            clientThread.start()


    
    def handleClient(self, client, addr, client_id):
        try:
            while True:
                request = client.recv(self.BUFFERSIZE)

                if request:              
                    request = pickle.loads(request)               
                    
                    request["id"] = client_id
                    functionName = request["functionName"]

                    request = pickle.dumps(request)

                    self.server.send(request)
                    self.log(f"({client_id}) Client has requested '{functionName}'")
        
        except ConnectionResetError:
            self.clients.pop(client_id)
            self.log(f"({client_id}) Client has disconnected")

    
    
    def handleServer(self):
        while True:
            response = pickle.loads(self.server.recv(self.BUFFERSIZE))

            try:
                client_id = response["id"]
                client = self.clients[client_id]
                
                response = pickle.dumps(response)
                client.send(response)
                
                self.log(f"The Server has responded to the Client ({client_id})")

            except Exception as e:
                print(e)





if __name__ == "__main__":
    os.system("cls")
    hub = SQLiteClientHub(IP="localhost", PORT=9191,
                        SERVER_IP="localhost", SERVER_PORT=9999)