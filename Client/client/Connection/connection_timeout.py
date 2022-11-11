from client.Window.UI.Elements.custom_signals import ConnectionSignal
from PySide6.QtCore import QThread
from time import sleep








class ConnectionTimeout(QThread):
    def __init__(self):
        super().__init__()

        self.signals = ConnectionSignal()


    def timeout(self, sec:int = 30):
        if sec > 0:
            self.time = sec
            self.start()
    
    
    def run(self):
        if self.time > 0:
            self.signals.connectionTimeout.emit()
            sleep(self.time)
            self.signals.connectionTimeoutExpired.emit()