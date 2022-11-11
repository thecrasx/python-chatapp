from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Property, QObject
from client.Window.UI.Elements.custom_signals import AnimationSignal

 
class TransitionAnimation(QObject):
    def __init__(self, target, rgb):
        super().__init__()
        self._target = target
        
        self.red = rgb[0]
        self.green = rgb[1]
        self.blue = rgb[2]
        self.alpha = 0

        self.signals = AnimationSignal()

        self.animation = QPropertyAnimation(self, b"alphaValue")
        self.animation.finished.connect(self.__onAnimationFinished)
        self.running = False

        self.__alphaMaximumSignalEmited = False

    
    def __onAnimationFinished(self):
        self.__alphaMaximumSignalEmited = False
        self.running = False
        self._target.hide()


    @Property(int)
    def alphaValue(self):
        return self.alpha

    @alphaValue.setter
    def alphaValue(self, value):
        self.alpha = value
        self._target.setStyleSheet(f"background-color: rgba({self.red}, {self.green}, {self.blue}, {self.alpha})")

        if value == 255:
            if not self.__alphaMaximumSignalEmited:
                self.signals.alphaMaximum.emit()
                self.__alphaMaximumSignalEmited = True


    
    def load(self, duration=1500):
        if not self.running:
            self.running = True
            self._target.show()

            self.animation.setDuration(duration)
            self.animation.setKeyValueAt(0, 0)
            self.animation.setKeyValueAt(0.3, 255)
            self.animation.setKeyValueAt(0.6, 255)
            self.animation.setKeyValueAt(1, 0)
            self.animation.setEasingCurve(QEasingCurve.Linear)
            self.animation.start()