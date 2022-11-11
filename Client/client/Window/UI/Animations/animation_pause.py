from client.Window.UI.Elements.custom_signals import AnimationSignal
from PySide6.QtCore import  QThread
from time import sleep





class AnimationPause(QThread):
    def __init__(self, sec) -> None:
        super().__init__()
        self.__pause = sec
        self.signals = AnimationSignal()

    
    def setPauseTime(self, sec):
        self.__pause = sec
    
    def run(self):
        sleep(self.__pause)
        self.signals.pauseFinished.emit()