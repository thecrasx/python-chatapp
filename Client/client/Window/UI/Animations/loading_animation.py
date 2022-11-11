from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from client.Window.UI.Animations.animation_pause import AnimationPause



class LoadingAnimation(QPropertyAnimation):
    def __init__(self, target) -> None:
        super().__init__(target, b"maximumSize")
        
        self._target = target

        self.finished.connect(self._onAnimationFinish)

        self.animationPause = AnimationPause(0.5)
        self.animationPause.signals.pauseFinished.connect(self.__onAnimationPauseFinished)

        # Direction 1 = In
        # Direction 0 = Out
        self.__direction = 0

        self.__running = False
        self.__autoStart = False


    def __onAnimationPauseFinished(self):
        if self.__autoStart:
            self.load()
    
    
    def _onAnimationFinish(self):
        self.__running = False

        if self.__autoStart:
            self.animationPause.start()
        
        
    def stop(self):
        self.__autoStart = False
   
    
    def load(self, duration=1000):     
        if not self.__running:
            self.__running = True
            self.__autoStart = True
            
            if self.__direction == 0:
                self.__direction = 1
                start = self._target.maximumSize()
                end = start / 1.5
            
            else:
                self.__direction = 0
                start = self._target.maximumSize()
                end = start * 1.5
            
            self.setDuration(duration)
            self.setStartValue(start)
            self.setEndValue(end)
            self.setEasingCurve(QEasingCurve.InOutExpo)
            self.start()


