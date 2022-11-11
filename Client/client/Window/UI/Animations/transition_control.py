from client.Window.UI.Animations.transition_animation import TransitionAnimation
from client.Window.UI.Elements.UI.ui_overlay import OverlayUI






class TransitionControl:
    def __init__(self, mainWindow):
        self.window = mainWindow
        
        self.ui = self.window.ui
        self.signals = self.window.signals

        # Overlay
        self.ui.transitionEffect = OverlayUI(self.window)
        self.ui.transitionEffect.setOffset(self.ui.titleBar)
        self.ui.transitionEffect.hide()

        self.transition = TransitionAnimation(self.ui.transitionEffect, rgb=(39, 40, 45))
        self.transition.signals.alphaMaximum.connect(self.__onAlphaMaximum)

        self.signals.accountSignal.loggedIn.connect(self.loginTransition)
        self.signals.accountSignal.registered.connect(self.registerTransition)
        self.signals.connectionSignal.connected.connect(self.connectTransition)

        self.loggedIn = False
        self.registered = False
        self.connect = False

        self.connected = False


    
    def loginTransition(self):
        self.loggedIn = True
        self.transition.load()


    def registerTransition(self):
        self.registered = True
        self.transition.load()


    def connectTransition(self, connected):
        self.connect = True

        if connected:
            self.connected = True
            self.window.loadingAnimation.stop()
            self.transition.load()
        
        else:
            self.connected = False
            self.window.loadingAnimation.load()
            self.transition.load()

    
    def __onAlphaMaximum(self):
        if self.loggedIn:
            self.ui.application.setCurrentWidget(self.ui.mainScreen)
            self.loggedIn = False

        elif self.registered:
            self.ui.application.setCurrentWidget(self.ui.mainScreen)
            self.registered = False

        elif self.connect:
            if self.connected:
                self.ui.application.setCurrentWidget(self.ui.loginScreen)
            else:
                self.ui.application.setCurrentWidget(self.ui.loadingScreen)

            self.connect = False