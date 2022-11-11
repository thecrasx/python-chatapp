from client.Window.UI.Elements.UI.ui_overlay import OverlayUI

from PySide6.QtWidgets import QWidget

from client.Window.qtui_converter import UIToPyConverter



def uiChangeEmailFormConvert():
        UIToPyConverter(path = "./client/Window/UI/.design_file/change_email.ui", 
                        output = "./client/Window/UI/ui_change_email_form.py")


from client.Window.UI.ui_change_email_form import Ui_ChangeEmailForm


class ChangeEmailOverlay(OverlayUI):
    def __init__(self, mainWindow):
        super().__init__(mainWindow)
        self.__setupOverlayUI()

        self.window = mainWindow
        self.ui = self.window.ui
        self.connectionUI = self.window.connectionUI
        self.signals = self.window.signals

        self.signals.responseSignal.emailChangeValidated.connect(self.__onEmailChangeValidation)
        self.signals.responseSignal.newEmailTaken.connect(self.__onEmailTaken)
        self.signals.responseSignal.invalidPassword_E.connect(self.__onInvalidPassword)


        self.__newEmail = None


    def __setupOverlayUI(self):
        widget = QWidget()


        self.overlayUI = Ui_ChangeEmailForm()
        self.overlayUI.setupUi(widget)
        self.addWidget(self.overlayUI.emailChangeContainer)


    def clearStatus(self):
        self.overlayUI.newEmailStatusLabel.clear()
        self.overlayUI.passwordStatusLabel.clear()



    def changeEmail(self):
        self.clearStatus()

        newEmail = self.overlayUI.newEmailInput.text().replace(" ", "")
        password = self.overlayUI.passwordInput.text().replace(" ", "")

        if newEmail and password:
            self.connectionUI.request.changeEmail(newEmail, password)
            self.__newEmail = newEmail

        else:
            if not newEmail:
                self.overlayUI.newEmailStatusLabel.setText("- Enter a email")

            if not password:
                self.overlayUI.passwordStatusLabel.setText("- Enter a password")




    def __onEmailTaken(self):
        self.overlayUI.newEmailStatusLabel.setText("- Taken")


    def __onInvalidPassword(self):
        self.overlayUI.passwordStatusLabel.setText("- Invalid Password")


    def __onEmailChangeValidation(self, validated):
        if validated:
            self.clearStatus()
            self.overlayUI.newEmailInput.clear()
            self.overlayUI.passwordInput.clear()

            self.ui.emailSettingsLabel.setText(self.__newEmail)

            self.hide()

