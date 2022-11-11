from client.image_loader import ImageLoader
from client.Window.Connection_UI.data_load import DataLoad





class Login:
    def __init__(self, mainWindow):
        self.window = mainWindow
        
        self.ui = self.window.ui
        self.signals = self.window.signals
        self.account = self.window.account
        self.connectionUI = self.window.connectionUI

        self.email = None
        self.username = None
        self.password = None
        
        self.ui.loginCredentialsStatusLabel.hide()

        
        self.signals.responseSignal.credentialsValidated.connect(self.__onCredentialsValidated)
        self.signals.responseSignal.loginValidated.connect(self.__onLoginValidated)
        self.signals.responseSignal.userData.connect(self.__updateUserData)
        self.signals.accountSignal.loggedIn.connect(self.__onLogin)

        self.loggedIn = False





    def login(self):
        self.email = self.ui.emailInput.text().replace(" ", "")
        self.password = self.ui.passwordInput.text().replace(" ", "")
        self.username = None
        
        if self.email != "":
            if not "@" in self.email:
                self.username = self.email
                self.email = None


        if self.email or self.username and self.password:
            self.ui.loginCredentialsStatusLabel.hide()

            self.connectionUI.request.isCredentialsValid(
                                                    password=self.password, 
                                                    username=self.username, 
                                                    email=self.email )


        else:
            if not self.email and not self.username and not self.password:
                self.ui.loginCredentialsStatusLabel.setText("Enter a email and password")

            elif not self.email and not self.username:
                self.ui.loginCredentialsStatusLabel.setText("Enter a email or username")

            elif not self.password:
                self.ui.loginCredentialsStatusLabel.setText("Enter a password")

            self.ui.loginCredentialsStatusLabel.show()
    
    
    def __onCredentialsValidated(self, validated):
        if validated:
            self.connectionUI.request.login(
                                        password=self.password, 
                                        username=self.username, 
                                        email=self.email )
            
            self.ui.loginCredentialsStatusLabel.hide()

        else:
            self.ui.loginCredentialsStatusLabel.setText("Email or password is invalid")
            self.ui.loginCredentialsStatusLabel.show()

    
    
    def __onLoginValidated(self, validated):
        if validated:
            self.loggedIn = True
            self.signals.accountSignal.loggedIn.emit()
            
            self.connectionUI.request.getUserData(
                                        password=self.password, 
                                        username=self.username, 
                                        email=self.email)
            

        else:
            self.loggedIn = False
            self.ui.loginCredentialsStatusLabel.setText("Email or password is invalid")
            self.ui.loginCredentialsStatusLabel.show()


    def __updateUserData(self, data):
        if data.userId:
            self.account.userId = data.userId

        if data.username:
            self.account.username = data.username
            self.ui.userNameLMLabel.setText(data.username)
            self.ui.usernameSettingsLabel.setText(data.username)
            self.ui.userNameSettingsLabel.setText(data.username)


        if data.email:
            self.account.email = data.email
            self.ui.emailSettingsLabel.setText(data.email)



        
        if data.photo:
            imgByteArray = ImageLoader.getBytesFromHex(data.photo)

            ImageLoader.setPixmap(self.ui.userPhotoLMLabel, imgByteArray, 70)
            ImageLoader.setPixmap(self.ui.userPhotoSettingsLabel, imgByteArray, 60)


    def __onLogin(self):
        DataLoad(self.connectionUI.request)




    
    