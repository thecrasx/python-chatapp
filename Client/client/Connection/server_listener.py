from PySide6.QtCore import QThread
from client.Window.UI.Elements.custom_signals import ResponseSignal
import pickle



class ServerListener(QThread):
    def __init__(self, server: object, signals, connected, buffersize):
        super().__init__()

        self.BUFFERSIZE = buffersize
        self.server = server
        self.connected = connected
        self.listening = False

        
        self.signals = signals       
        
        self.signals.connectionSignal.connectedToServer.connect(self.__onConnect)



    
    def __onConnect(self, connected):
        if connected:
            self.connected = True
        
        else:
            self.listening = False
            self.connected = False



    
    def run(self):
        self.listening = True
        
        while self.connected:
            try:
                receivedData = self.server.recv(self.BUFFERSIZE)

                self.processReceivedData(receivedData)


            except ConnectionRefusedError:
                print("[SERVER LISTENER] Connection Refused")
                self.signals.connectionSignal.connectionRefused.emit()
                break

            except ConnectionResetError:
                print("[SERVER LISTENER] Connection Reset")
                self.signals.connectionSignal.connectionRefused.emit()
                break

            except OSError as e:
                print("[SERVER LISTENER] OS Error")
                print(e)
                break





    def processReceivedData(self, receivedData):
        receivedData = pickle.loads(receivedData)
        print(receivedData())

        try:
            if receivedData() == "Request":
                pass

            elif receivedData() == "Response":
                self.signals.responseSignal.newResponse.emit(receivedData)
        
        except Exception as e:
            print(e)


