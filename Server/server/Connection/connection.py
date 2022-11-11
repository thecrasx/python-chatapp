from server.Connection.connections import Connections
from server.Connection.Request.request_handler import RequestHandler
from server.Connection.client_handler import ClientHandler
from multiprocessing import Process

from threading import Thread
import socket


SQLITE_DATABASE = True

if SQLITE_DATABASE:
    from server.Database.SQLite.sqlite_server import SQLiteServer
    from server.Database.SQLite.sqlite_client_hub import SQLiteClientHub



class Server:
    def __init__(self, IP, PORT,
                       BUFFERSIZE = 16384, 
                       FORMAT = "utf-8"):

        self.IP = IP
        self.PORT = PORT
        self.ADDR = (self.IP, self.PORT)
        self.BUFFSIZE = BUFFERSIZE
        self.FORMAT = FORMAT
        
        self.database = None

        if SQLITE_DATABASE:
            Process(target=SQLiteServer, args=("test", "localhost", 9999), daemon=True).start()
            Process(target=SQLiteClientHub, args=("localhost", 10345, "localhost", 9999), daemon=True).start()

            self.database = "sqlite"

        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.bind(self.ADDR)

        self.connections = Connections()
        
    
    
    
    def start(self):
        print("LISTENING")
        self._server.listen()

        while True:
            client, addr = self._server.accept()
            print("Connected")

            thread = Thread(target=ClientHandler, 
                            args=(client, addr, self.connections, self.database, self.BUFFSIZE), daemon=True)
            thread.start()




if __name__ == "__main__":
    server = Server("localhost", 9292)
    server.start()
