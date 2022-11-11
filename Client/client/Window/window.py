################### Converter ###################

__CONVERT = False

### UI Converter
if __name__ == "__main__":
    if __CONVERT:
        from client.Window.qtui_converter import UIToPyConverter
        from client.Window.UI.Elements.UI.change_username import uiChangeUsernameFormConvert
        from client.Window.UI.Elements.UI.change_email import uiChangeEmailFormConvert
        from client.Window.UI.Elements.UI.change_password import uiChangePasswordFormConvert
        
        UIToPyConverter(path = "./client/Window/UI/.design_file/form.ui", 
                        output = "./client/Window/UI/ui_form.py")
        
        uiChangeUsernameFormConvert()
        uiChangeEmailFormConvert()
        uiChangePasswordFormConvert()


################################################

################### PySide6 ###################
from time import sleep
from threading import Thread

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from client.Window.UI.Animations.transition_control import TransitionControl


################### ChatApp ###################

### Account
from client.account import Account

### UI
from client.Window.UI.ui_form import Ui_MainWindow

### UI Elements
from client.Window.UI.Elements.UI.ui_elements     import UIElements
from client.Window.UI.Elements.UI.size_grip_ui    import SizeGripUI
from client.Window.UI.Elements.UI.change_username import ChangeUsernameOverlay
from client.Window.UI.Elements.UI.change_email    import ChangeEmailOverlay
from client.Window.UI.Elements.UI.change_password import ChangePasswordOverlay
from client.Window.UI.Elements.UI.profile_ui      import ProfileUI
from client.Window.UI.Elements.chat_manager       import ChatManager
from client.Window.UI.Elements.custom_signals     import Signals
from client.Window.UI.Buttons.buttons             import Buttons
from client.Window.UI.Elements.friends            import Friends
from client.Window.UI.Elements.friends_search     import FriendsSearch

### UI Theme
from client.Window.UI.Theme.theme import Theme

### UI Animations
from client.Window.UI.Animations.friends_container_animation import FriendsContainerAnimation
from client.Window.UI.Animations.loading_animation import LoadingAnimation




### Connection UI
from client.Window.Connection_UI.login import Login
from client.Window.Connection_UI.register import Register
from client.Window.Connection_UI.connection_ui import ConnectionUI


#################### Other ####################
import sys


################################################


class MainWindow(QMainWindow):
    def __init__(self):     
        
        # Ui
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._framelessWindow(True)

        # Launched - First Time Application Becomes Visible
        self.signals = Signals()
        self.account = Account()

        self.launched = False
        self.signals.windowSignal.launch.connect(self.__onLaunch)

        # self.ui.application.setCurrentWidget(self.ui.mainScreen)
        #self.ui.application.setCurrentWidget(self.ui.loginScreen)
        self.ui.application.setCurrentWidget(self.ui.loadingScreen)

        
        self.theme = Theme("default.json")

        self.uiElements = UIElements(chatFrame=self.ui.chatBox,
                                        chatLayout=self.ui.chatBoxLayout,
                                        recentChatFrame=self.ui.recentChatLMBox,
                                        recentChatLayout=self.ui.recentChatLMBoxLayout,
                                        theme=self.theme.theme,
                                        windowSize=self.size,
                                        chatSize=self.ui.chatSAWC.width,
                                        chatInputBox=self.ui.chatInputBox,
                                        chatInput=self.ui.chatInput)


        
        self.chatManager = ChatManager(self)
        self.transitionControl = TransitionControl(self)
          
        self._previousWindowWidth = 0
        self.ui.chatContainer.hide()
        self.ui.chatInput.setDisabled(True)
        self.ui.mainFrame.setMaximumWidth(16777215)
        self.ui.titleBar.mouseMoveEvent = self.__moveWindowEvent
        self.ui.loadingLabel.setPixmap(QPixmap(u"./res/logo.png"))
        


        self.ui.friendsContainer.setMaximumWidth(0)
        self.ui.testMessageFrame.close()
        self.ui.testMessageBtn.close()
        self.ui.chatFrame.close()

        self.ui.chatSA.resizeEvent = self.chatSAResizeEvent
        

        self.buttons = None

        # PROFILE
        self.profileUI = ProfileUI(self)

        # Animations
        self.loadingAnimation = LoadingAnimation(self.ui.loadingBox)


        # Connection
        self.connectionUI = ConnectionUI(self)

        self.register = Register(self)
        self.login = Login(self)

        self.friends = Friends(self)
        self.friendsSearch = FriendsSearch(self)
        
        
        # Overlays
        self.ui.changeUsernameOverlay = ChangeUsernameOverlay(self)
        self.ui.changeUsernameOverlay.setOffset(self.ui.titleBar)
        self.ui.changeUsernameOverlay.setOverlayOpacity(130)
        self.ui.changeUsernameOverlay.hide()

        self.ui.changeEmailOverlay = ChangeEmailOverlay(self)
        self.ui.changeEmailOverlay.setOffset(self.ui.titleBar)
        self.ui.changeEmailOverlay.setOverlayOpacity(130)
        self.ui.changeEmailOverlay.hide()

        self.ui.changePasswordOverlay = ChangePasswordOverlay(self)
        self.ui.changePasswordOverlay.setOffset(self.ui.titleBar)
        self.ui.changePasswordOverlay.setOverlayOpacity(130)
        self.ui.changePasswordOverlay.hide()


        
        # Other
        self.buttons = Buttons(self)
        self.sizeGrip = SizeGripUI(self)
        self.show()

    
    
    def chatSAResizeEvent(self, event):
        if self.chatManager.currentChat is not None:
            self.chatManager.currentChat.resizeMessages()



    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()
    


    def resizeEvent(self, event):
        windowWidth = self.width()
        windowHeight = self.height()

        if windowWidth != self._previousWindowWidth:   
            self._previousWindowWidth = windowWidth

        
        
        self.ui.transitionEffect.updateSize(windowWidth, windowHeight)
        self.ui.changeUsernameOverlay.updateSize(windowWidth, windowHeight)
        self.ui.changeEmailOverlay.updateSize(windowWidth, windowHeight)
        self.ui.changePasswordOverlay.updateSize(windowWidth, windowHeight)



    def __moveWindowEvent(self, event):
        if self.isMaximized() == False:
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                    self.dragPos = event.globalPosition().toPoint()
                    event.accept()



    def _framelessWindow(self, frameless: bool):
        if frameless:
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)


    def showEvent(self, event):
        super().showEvent(event)

        self.signals.windowSignal.windowVisible.emit(True)

        if not self.launched:
            self.__launchDelay = LaunchDelay(launchSignal=self.signals.windowSignal.launch,
                                    delay=0.5)
            self.__launchDelay.start()

            self.launched = True


    def hideEvent(self, event):
        super().hideEvent(event)

        if self.isHidden:
            self.signals.windowSignal.windowVisible.emit(False)


    def __onLaunch(self):
        print("Launched")
        self.loadingAnimation.load()

        




class LaunchDelay(QThread):
    def __init__(self, launchSignal, delay=0.5):
        super().__init__()

        self.launchSignal = launchSignal
        self.delay = delay


    
    def run(self):
        sleep(self.delay)
        self.launchSignal.emit()

    





if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())