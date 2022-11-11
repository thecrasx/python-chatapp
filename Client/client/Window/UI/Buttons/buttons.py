from client.Window.UI.Buttons.button_functions import ButtonFunctions
from PySide6.QtCore import Qt

class Buttons(ButtonFunctions):
    def __init__(self, mainWindow):
        super().__init__(mainWindow)
        

        self.ui.appExit.clicked.connect(lambda: self.window.close())
        self.ui.appMinimize.clicked.connect(lambda: self.window.showMinimized())
        self.ui.appFullscreenToggle.clicked.connect(self.toggleFullScreen)
        self.ui.friendsLMBtn.clicked.connect(lambda: self.friendsContainerSlide())
        self.ui.testChatBtn.clicked.connect(lambda: self.window.chatManager.addChat())
        self.ui.settingsLMBtn.clicked.connect(lambda: self.ui.application.setCurrentWidget(self.ui.settingsScreen))
        self.ui.exitSettingsBtn.clicked.connect(lambda: self.ui.application.setCurrentWidget(self.ui.mainScreen))

        self.ui.friendsPageBtn.clicked.connect(lambda: self.setFriendsPage(friends=True))
        self.ui.addFriendsPageBtn.clicked.connect(lambda: self.setFriendsPage(add=True))
        self.ui.blockListPageBtn.clicked.connect(lambda: self.setFriendsPage(block=True))
        self.ui.friendRequestPageBtn.clicked.connect(lambda: self.setFriendsPage(request=True))


        self.ui.toRegisterScreenBtn.clicked.connect(lambda: self.ui.application.setCurrentWidget(self.ui.registerScreen))
        self.ui.signInBtn.clicked.connect(lambda: self.ui.application.setCurrentWidget(self.ui.loginScreen))


        self.ui.registerBtn.clicked.connect(self.window.register.register)
        self.ui.loginBtn.clicked.connect(self.window.login.login)

        self.ui.usernameSettingsEditBtn.clicked.connect(self.ui.changeUsernameOverlay.show)
        self.ui.changeUsernameOverlay.overlayUI.cancelBtn.clicked.connect(self.ui.changeUsernameOverlay.hide)
        self.ui.changeUsernameOverlay.overlayUI.confirmBtn.clicked.connect(self.ui.changeUsernameOverlay.changeUsername)

        self.ui.emailSettingsEditBtn.clicked.connect(self.ui.changeEmailOverlay.show)
        self.ui.changeEmailOverlay.overlayUI.cancelBtn.clicked.connect(self.ui.changeEmailOverlay.hide)
        self.ui.changeEmailOverlay.overlayUI.confirmBtn.clicked.connect(self.ui.changeEmailOverlay.changeEmail)

        self.ui.changePasswordSettingsBtn.clicked.connect(self.ui.changePasswordOverlay.show)
        self.ui.changePasswordOverlay.overlayUI.cancelBtn.clicked.connect(self.ui.changePasswordOverlay.hide)
        self.ui.changePasswordOverlay.overlayUI.confirmBtn.clicked.connect(self.ui.changePasswordOverlay.changePassword)

        self.ui.changePhotoSettingsBtn.clicked.connect(self.window.profileUI.changeProfilePhoto)
        

        
        # #self.ui.testMessageBtn.clicked.connect(lambda: addMessage())

    
    
    
    def resetFocus(self):
        pass

        #self.ui.settingsLMBtn.setStyleSheet("outline: none")
        

