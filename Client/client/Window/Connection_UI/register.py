from client.Connection.password_encoder import passwEncode





class Register:
    def __init__(self, mainWindow):
        self.window = mainWindow
        self.ui = self.window.ui
        self.signals = self.window.signals
        self.account = self.window.account
        self.connectionUI = self.window.connectionUI

        self.signals.responseSignal.usernameTaken.connect(self.__onUsernameTaken)
        self.signals.responseSignal.emailTaken.connect(self.__onEmailTaken)
        self.signals.responseSignal.registerValidated.connect(self.__onRegisterValidation)

        self.username = None
        self.email = None
        self.password = None



    def register(self):
        if self.isInputValid():
            self.connectionUI.request.register(self.email, self.username, self.password, "12.12.2022")
        else:
            pass


    def isInputValid(self):
        email = None
        username = None
        password = None
        passwordConfirm = None


        # EMAIL
        if self.ui.emailInputR.text().replace(" ", "") != "":
            email = self.ui.emailInputR.text()
            
            if not "@" in email:
                self.ui.emailStatusLabel.setText("- Enter a valid email address!")
                email = None
            else:
                self.ui.emailStatusLabel.clear()
        
        else:
            self.ui.emailStatusLabel.setText("- Enter a email!")
            email = None




        # USERNAME
        if self.ui.usernameInput.text().replace(" ", "") != "":
            username = self.ui.usernameInput.text()
            self.ui.usernameStatusLabel.clear()

        else:
            self.ui.usernameStatusLabel.setText("- Enter a username!")
            username = None




        # PASSWORD
        if self.ui.passwordInputR.text().replace(" ", "") != "":
            password = self.ui.passwordInputR.text()
            self.ui.passwordStatus.clear()

        else:
            self.ui.passwordStatus.setText("- Enter a password!")





        # CONFIRM PASSWROD
        if self.ui.confirmPasswordInput.text().replace(" ", "") != "":
            passwordConfirm = self.ui.confirmPasswordInput.text()
            self.ui.confirmPasswordStatusLabel.clear()

        else:
            self.ui.confirmPasswordStatusLabel.setText("- Confirm the password!")





        if password != None and passwordConfirm != None:
            if passwordConfirm != password:
                self.ui.confirmPasswordStatusLabel.setText("- Passwords do not match!")
                password = None
                passwordConfirm = None

            else:
                self.ui.confirmPasswordStatusLabel.clear()


        if email and username and password:
            self.email = email
            self.username = username
            self.password = password

            return True
        
        else:
            return False

    
    
    def __onUsernameTaken(self):
        self.ui.usernameStatusLabel.setText("- Taken")

    def __onEmailTaken(self):
        self.ui.emailStatusLabel.setText("- Taken")


    def __onRegisterValidation(self, validated):
        print(validated)
        if validated:
            self.account.email = self.email
            self.account.username = self.username
            self.ui.userNameLMLabel.setText(self.username)
            self.signals.accountSignal.registered.emit()
            self.window.buttons.resetFocus()
