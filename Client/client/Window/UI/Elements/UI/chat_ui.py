from PySide6.QtWidgets import QFrame, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QAbstractScrollArea, QPlainTextEdit
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QCursor, QFont, QIcon

from client.Window.UI.Elements.custom_signals import CustomSignal
from client.Window.UI.Elements.UI.photo_label_ui import PhotoLabel


class ChatUI:
    def __init__(self, mainWindow, userName, 
                    userPhoto, chatNumber, currentChatChanged: CustomSignal):

        self.window = mainWindow
        self.ui =self.window.ui

        self.userName = userName
        self.userPhoto = userPhoto
        self.chatNumber = chatNumber
        
        self.messageCount = 0
        self.messages = []
        self.theme = self.window.theme.theme


        self.pressed = False
        self.currentChatChanged = currentChatChanged
        self.__customSignal = CustomSignal()
        self.closeChatBtnPressed = self.__customSignal.closeChatBtnPressed
        
        ############ UI ############         
        self.__setupUI(self.ui.recentChatLMBox, self.ui.recentChatLMBoxLayout)

    

        


    def __setupUI(self, recentChatFrame, recentChatLayout): 
        objectNameSuffix = f"-{self.userName}-{self.chatNumber}"

        icon = QIcon()
        icon.addFile(u":/Icons/Icons/close_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        
        font = QFont()
        font.setFamily(u"Righteous")
        font.setPointSize(12)

        # Chat Frame
        self.chatFrame = QFrame(recentChatFrame)
        self.chatFrame.setObjectName(f"chatFrame{objectNameSuffix}")
        self.chatFrame.setFrameShape(QFrame.StyledPanel)
        self.chatFrame.setFrameShadow(QFrame.Raised)
        self.chatFrame.setStyleSheet(self.theme.recentChat.normal.stylesheet)
        self.chatFrame.setCursor(QCursor(Qt.PointingHandCursor))

        # Chat Frame Layout
        self.chatFrameLayout = QHBoxLayout(self.chatFrame)
        self.chatFrameLayout.setSpacing(0)
        self.chatFrameLayout.setObjectName(f"chatFrameLayout{objectNameSuffix}")
        self.chatFrameLayout.setContentsMargins(0, 0, 0, 0)

        # Username And Photo Frame
        self.userNameNPhotoFrame = QFrame(self.chatFrame)
        self.userNameNPhotoFrame.setObjectName(f"userNameNPhotoFrame{objectNameSuffix}")
        self.userNameNPhotoFrame.setFrameShape(QFrame.StyledPanel)
        self.userNameNPhotoFrame.setFrameShadow(QFrame.Raised)
        self.userNameNPhotoFrame.setStyleSheet(self.theme.recentChat.userNameNPhotoFrame.normal.stylesheet)
        self.userNameNPhotoFrame.setCursor(QCursor(Qt.PointingHandCursor))
        
        # Username And Photo Frame Layout
        self.userNameNPhotoFrameLayout = QHBoxLayout(self.userNameNPhotoFrame)
        self.userNameNPhotoFrameLayout.setSpacing(7)
        self.userNameNPhotoFrameLayout.setObjectName(f"userNameNPhotoFrameLayout{objectNameSuffix}")
        self.userNameNPhotoFrameLayout.setContentsMargins(0, 0, 0, 0)
        
        # Photo Label
        self.userPhotoLabel = PhotoLabel(self.userNameNPhotoFrame, size=40)
        self.userPhotoLabel.setObjectName(f"userPhotoLabel{objectNameSuffix}")

        if self.userPhoto:
            self.userPhotoLabel.loadImageFromHex(self.userPhoto)

        self.userNameNPhotoFrameLayout.addWidget(self.userPhotoLabel)

        # Username Label
        self.userNameLabel = QLabel(self.userNameNPhotoFrame)
        self.userNameLabel.setObjectName(f"userNameLabel{objectNameSuffix}")
        self.userNameLabel.setFont(font)
        self.userNameLabel.setText(self.userName)

        self.userNameNPhotoFrameLayout.addWidget(self.userNameLabel)
        self.chatFrameLayout.addWidget(self.userNameNPhotoFrame, 0, Qt.AlignLeft|Qt.AlignVCenter)

        # Chat Buttons Frame
        self.chatButtonsFrame = QFrame(self.chatFrame)
        self.chatButtonsFrame.setObjectName(f"chatButtonsFrame{objectNameSuffix}")
        self.chatButtonsFrame.setStyleSheet(u"")
        self.chatButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.chatButtonsFrame.setFrameShadow(QFrame.Raised)
        self.chatButtonsFrame.setStyleSheet(self.theme.recentChat.buttonFrame.normal.stylesheet)

        # Chat Buttons Frame Layout
        self.chatButtonsFrameLayout = QHBoxLayout(self.chatButtonsFrame)
        self.chatButtonsFrameLayout.setSpacing(0)
        self.chatButtonsFrameLayout.setObjectName(f"chatButtonsFrameLayout{objectNameSuffix}")
        self.chatButtonsFrameLayout.setContentsMargins(0, 0, 0, 0)
        
        # Close Button
        self.closeChatBtn = QPushButton(self.chatButtonsFrame)
        self.closeChatBtn.setObjectName(f"closeChatBtn{objectNameSuffix}")
        self.closeChatBtn.setIcon(icon)
        self.closeChatBtn.setStyleSheet(u"background: transparent;\n"
        "padding: 0px;\n"
        "icon-size: 24px;"
        "outline: none")
        self.closeChatBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.closeChatBtn.clicked.connect(lambda: self.closeChatBtnPressed.emit(self))

        self.chatButtonsFrameLayout.addWidget(self.closeChatBtn)
        self.chatFrameLayout.addWidget(self.chatButtonsFrame, 0, Qt.AlignRight|Qt.AlignVCenter)
        
        recentChatLayout.addWidget(self.chatFrame)
        self.chatFrame.setMouseTracking(True)
        self.chatFrame.mouseMoveEvent = self.__mouseMoveEvent
        self.chatFrame.mousePressEvent = self.__mousePressEvent
        self.chatFrame.leaveEvent = self.__leaveEvent
        

    def close(self):
        self.chatFrame.close()
    
    
    def setNormal(self):
        self.pressed = False
        self.__leaveEvent(None)


    
    
    ########## EVENTS ###########
    def __leaveEvent(self, event):
        if not self.pressed:
            self.chatFrame.setStyleSheet(self.theme.recentChat.normal.stylesheet)
            self.userNameNPhotoFrame.setStyleSheet(self.theme.recentChat.userNameNPhotoFrame.normal.stylesheet)
            self.chatButtonsFrame.setStyleSheet(self.theme.recentChat.buttonFrame.normal.stylesheet)
    
    
    def __mouseMoveEvent(self, event):
        if not self.pressed:
            self.chatFrame.setStyleSheet(self.theme.recentChat.hover.stylesheet)
            self.userNameNPhotoFrame.setStyleSheet(self.theme.recentChat.userNameNPhotoFrame.hover.stylesheet)
            self.chatButtonsFrame.setStyleSheet(self.theme.recentChat.buttonFrame.hover.stylesheet)


    def __mousePressEvent(self, event):
        if not self.pressed:
            self.pressed = True
                
            # Update current chat
            self.currentChatChanged.emit(self)

            self.chatFrame.setStyleSheet(self.theme.recentChat.pressed.stylesheet)
            self.userNameNPhotoFrame.setStyleSheet(self.theme.recentChat.userNameNPhotoFrame.pressed.stylesheet)
            self.chatButtonsFrame.setStyleSheet(self.theme.recentChat.buttonFrame.pressed.stylesheet)