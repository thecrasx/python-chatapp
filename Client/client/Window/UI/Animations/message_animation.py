from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QSize



class MessageAnimation(QPropertyAnimation):
    def __init__(self, target, propertyName):
        super().__init__(target, propertyName)
        self._target = target

    
    def _currentSize(self):
        return QSize(self._target.width(), self._target.height())
    
    def _calculateLineIncrement(self, lineCount):
        pass
    
    
    def _calculateEndValue(self, startSize, friendsContainerClosed):
        width, height = startSize.width(), startSize.height()      

        lineCount = self._target.document().lineCount()
        
        if friendsContainerClosed:
            endWidth = width - 300
        
            endHeight = round( ( 0.5 * lineCount ) + lineCount ) * 17.4
        else:
            endWidth = width + 300

            endHeight =  round( lineCount - ( 0.5 * lineCount ) ) * 17.4
        #print(f"   Width: {width}   Height: {height}\nEndWidth: {endWidth}   EndHeight: {endHeight}")
        return QSize(endWidth, endHeight)



    def slide(self, friendsContainerClosed, duration):
        self.setDuration(duration)
        self.setStartValue(self._currentSize())
        self.setEndValue(self._calculateEndValue(self._currentSize(), friendsContainerClosed))
        self.setEasingCurve(QEasingCurve.InOutQuart)
        self.start()

        

