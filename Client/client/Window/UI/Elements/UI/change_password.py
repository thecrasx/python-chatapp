from client.Window.UI.Elements.UI.ui_overlay import OverlayUI

from PySide6.QtWidgets import QWidget

from client.Window.qtui_converter import UIToPyConverter



def uiChangePasswordFormConvert():
        UIToPyConverter(path = "./client/Window/UI/.design_file/change_password.ui", 
                        output = "./client/Window/UI/ui_change_password_form.py")


from client.Window.UI.ui_change_password_form import Ui_ChangePasswordForm


class ChangePasswordOverlay(OverlayUI):
    def __init__(self, mainWindow):
        super().__init__(mainWindow)
        self.__setupOverlayUI()

        self.window = mainWindow
        self.ui = self.window.ui
        self.connectionUI = self.window.connectionUI
        self.signals = self.window.signals

        self.signals.responseSignal.passwordChangeValidated.connect(self.__onPasswordChangeValidation)
        self.signals.responseSignal.invalidPassword.connect(self.__onInvalidPassword)




    def __setupOverlayUI(self):
        widget = QWidget()

        self.overlayUI = Ui_ChangePasswordForm()
        self.overlayUI.setupUi(widget)
        self.addWidget(self.overlayUI.passwordChangeContainer)

    
    def clearStatus(self):
        self.overlayUI.currentPasswordStatusLabel.clear()
        self.overlayUI.newPasswordStatusLabel.clear()
        self.overlayUI.confirmPasswordStatusLabel.clear()


    
    def changePassword(self):
        self.clearStatus()

        password = self.overlayUI.currentPasswordInput.text().replace(" ", "")
        newPassword = self.overlayUI.newPasswordInput.text().replace(" ", "")
        confirmPassword = self.overlayUI.confirmPasswordInput.text().replace(" ", "")

        if not password:
            self.overlayUI.currentPasswordStatusLabel.setText("Enter a current password")

        if not newPassword:
            self.overlayUI.newPasswordStatusLabel.setText("Enter a new password")
        
        if not confirmPassword:
            self.overlayUI.confirmPasswordStatusLabel.setText("Confirm the password")

        
        if newPassword != confirmPassword:
            self.overlayUI.confirmPasswordStatusLabel.setText("- Passwords do not match!")
            newPassword = None

        
        elif password and newPassword:
            if password != newPassword:
                self.connectionUI.request.changePassword(password, newPassword)
            else:
                self.overlayUI.newPasswordStatusLabel.setText(" - New password is the same as current")




    def __onInvalidPassword(self):
        self.overlayUI.currentPasswordStatusLabel.setText("- Invalid Password")


    def __onPasswordChangeValidation(self, validated):
        if validated:
            self.clearStatus()

            self.overlayUI.currentPasswordInput.clear()
            self.overlayUI.newPasswordInput.clear()
            self.overlayUI.confirmPasswordInput.clear()

            self.hide()
