








class ResponseHandler:
    def __init__(self, mainWindow, responseSignals):
        self.window = mainWindow
        self.ui = self.window.ui

        self.responseSignals = responseSignals


    
    def _onLoggedIn(self, loggedIn):
        if loggedIn:
            self.ui.application.setCurrentWidget(self.ui.mainScreen)