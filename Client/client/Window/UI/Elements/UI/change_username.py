from ast import main
from client.Window.UI.Elements.UI.ui_overlay import OverlayUI
from client.Window.qtui_converter import UIToPyConverter
from PySide6.QtWidgets import QWidget



def uiChangeUsernameFormConvert():
        UIToPyConverter(path = "./client/Window/UI/.design_file/change_username.ui", 
                        output = "./client/Window/UI/ui_change_username_form.py")



from client.Window.UI.ui_change_username_form import Ui_ChangeUsernameForm


class ChangeUsernameOverlay(OverlayUI):
    def __init__(self, mainWindow):
        super().__init__(mainWindow)
        self.__setupOverlayUI()
        
        self.window = mainWindow
        self.ui = self.window.ui
        self.connectionUI = self.window.connectionUI
        self.signals = self.window.signals

        self.signals.responseSignal.usernameChangeValidated.connect(self.__onUsernameChangeValidation)
        self.signals.responseSignal.newUsernameTaken.connect(self.__onUsernameTaken)
        self.signals.responseSignal.invalidPassword_U.connect(self.__onInvalidPassword)


        self.__newUsername = None
    
    def __setupOverlayUI(self):
        widget = QWidget()
        self.overlayUI = Ui_ChangeUsernameForm()
        self.overlayUI.setupUi(widget)
        self.addWidget(self.overlayUI.usernameChangeContainer)

    #########################################
    
    
    def clearStatus(self):
        self.overlayUI.newUsernameStatusLabel.clear()
        self.overlayUI.passwordStatusLabel.clear()



    def changeUsername(self):
        self.clearStatus()

        newUsername = self.overlayUI.newUsernameInput.text().replace(" ", "")
        password = self.overlayUI.passwordInput.text().replace(" ", "")

        if newUsername and password:
             self.connectionUI.request.changeUsername(newUsername, password)
             self.__newUsername = newUsername

        else:
            if not newUsername:
                self.overlayUI.newUsernameStatusLabel.setText("- Enter a username")

            if not password:
                self.overlayUI.passwordStatusLabel.setText("- Enter a password")



    
    def __onUsernameTaken(self):
        self.overlayUI.newUsernameStatusLabel.setText("- Taken")


    def __onInvalidPassword(self):
        self.overlayUI.passwordStatusLabel.setText("- Invalid Password")


    def __onUsernameChangeValidation(self, validated):
        if validated:
            self.clearStatus()
            self.overlayUI.newUsernameInput.clear()
            self.overlayUI.passwordInput.clear()

            self.ui.userNameLMLabel.setText(self.__newUsername)
            self.ui.userNameSettingsLabel.setText(self.__newUsername)
            self.ui.usernameSettingsLabel.setText(self.__newUsername)

            self.hide()