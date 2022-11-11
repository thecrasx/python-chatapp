
from PySide6.QtCore import QPropertyAnimation, QEasingCurve


class FriendsContainerAnimation(QPropertyAnimation):    
    def __init__(self, target, propertyName) -> None:
        super().__init__(target, propertyName)
        
        self.__running = False
        self.finished.connect(self._onAnimationFinish)


    def _onAnimationFinish(self):
        self.__running = False
   
    
    def slide(self, width, duration):     
        if not self.__running:
            self.__running = True

            if width == 0:
                endWidth = 300
            else:
                endWidth = 0
            
            self.setDuration(duration)
            self.setStartValue(width)
            self.setEndValue(endWidth)
            self.setEasingCurve(QEasingCurve.InOutQuart)
            self.start()





