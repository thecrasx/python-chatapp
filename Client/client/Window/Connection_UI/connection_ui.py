from client.Connection.connection import Client
from client.Window.UI.Elements.custom_signals import ConnectionSignal
from client.Window.Connection_UI.login import Login
from client.Window.Connection_UI.register import Register
from client.Window.Connection_UI.data_load import DataLoad





class ConnectionUI:
    def __init__(self, mainWindow) -> None:
        self.window = mainWindow
        self.ui = self.window.ui
        self.signals = self.window.signals

        self.signals.windowSignal.launch.connect(self.__onWindowLaunch)

        
        self.client = Client("localhost", 9292, self.signals)
        self.request = self.client.request
        self.response = self.client.response


        self.signals.connectionSignal.connectionRefused.connect(self.__onConnectionRefused)
        self.signals.connectionSignal.connectedToServer.connect(self.__onConnect)

        self.connected = False

        

    
    
    def connect(self):
        self.client.connect()

    
    def __onConnectionRefused(self):
        pass


    def __onWindowLaunch(self):
        #return
        self.connect()

   
   
   
    def __onConnect(self, connected):
        self.connected = connected
        
        if connected:    
            print("[CONNECTION UI] Connected")
            self.signals.connectionSignal.connected.emit(True)

        else:
            print("[CONNECTION UI] Disconnected")
            self.signals.connectionSignal.connected.emit(False)


    def __onLogin(self):
        DataLoad()






