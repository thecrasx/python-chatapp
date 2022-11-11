from PySide6.QtWidgets import QFrame, QPushButton, QLabel, QHBoxLayout
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont, QIcon, QCursor
from client.Window.UI.Elements.UI.photo_label_ui import PhotoLabel









class FriendUI:
    def __init__(self, mainWindow, friendId, userName, userPhoto, add: bool = False, request: bool = False, block: bool = False, requestSent = False):
        self.window = mainWindow
        self.ui = self.window.ui
        self.signals = self.window.signals

        self.friendId = friendId
        self.userName = userName
        self.userPhoto = userPhoto
        self.isRequest = request
        self.requestSent = requestSent

        self.__setParentWidgetAndLayout(add, request, block)
        self.__setupUI()



    def close(self):
        self.parentLayout.removeWidget(self.friendsFrame)
        self.friendsFrame.close()


    def __setParentWidgetAndLayout(self, add: bool = False, request: bool = False, block: bool = False):
        if add:
            self.parent = self.ui.addFriendsPage
            self.parentLayout = self.ui.addFriendsPageLayout

        elif request:
            self.parent = self.ui.friendRequestPage
            self.parentLayout = self.ui.friendRequestPageLayout

        elif block:
            self.parent = self.ui.blockListPage
            self.parentLayout = self.ui.blockListPageLayout

        else:
            self.parent = self.ui.friendsPage
            self.parentLayout = self.ui.friendsPageLayout
            




    def __setupUI(self):
        objectNameSuffix = f"-{self.userName}-"

        self.friendsFrame = QFrame(self.parent)
        self.friendsFrame.setObjectName(f"{objectNameSuffix}friendsFrame")
        self.friendsFrame.setStyleSheet(u"QFrame {\n"
"	padding: 12px 10px 12px 10px;\n"
"}")
        self.friendsFrame.setFrameShape(QFrame.StyledPanel)
        self.friendsFrame.setFrameShadow(QFrame.Raised)
        self.friendsFrameLayout = QHBoxLayout(self.friendsFrame)
        self.friendsFrameLayout.setSpacing(0)
        self.friendsFrameLayout.setObjectName(f"{objectNameSuffix}friendsFrameLayout")
        self.friendsFrameLayout.setContentsMargins(0, 0, 0, 0)
        
        self.userNameNPhotoContainer = QFrame(self.friendsFrame)
        self.userNameNPhotoContainer.setObjectName(f"{objectNameSuffix}userNameNPhotoContainer")
        self.userNameNPhotoContainer.setStyleSheet(u"QFrame {\n"
"	padding: 0px;\n"
"}")
        self.userNameNPhotoContainer.setFrameShape(QFrame.StyledPanel)
        self.userNameNPhotoContainer.setFrameShadow(QFrame.Raised)
        self.userNameNPhotoContainerLayout = QHBoxLayout(self.userNameNPhotoContainer)
        self.userNameNPhotoContainerLayout.setSpacing(6)
        self.userNameNPhotoContainerLayout.setObjectName(f"{objectNameSuffix}userNameNPhotoContainerLayout")
        self.userNameNPhotoContainerLayout.setContentsMargins(0, 0, 0, 0)

        self.userPhotoLabel = PhotoLabel(self.userNameNPhotoContainer, size=50)
        self.userPhotoLabel.setObjectName(u"userPhotoLabel")

        if self.userPhoto:
            self.userPhotoLabel.loadImageFromHex(self.userPhoto)

        self.userNameNPhotoContainerLayout.addWidget(self.userPhotoLabel)

        self.userNameLabel = QLabel(self.userNameNPhotoContainer)
        self.userNameLabel.setObjectName(f"{objectNameSuffix}userNameLabel")
        
        font = QFont()
        font.setFamilies([u"Righteous"])
        font.setPointSize(12)
        
        self.userNameLabel.setFont(font)
        self.userNameLabel.setText(self.userName)

        self.userNameNPhotoContainerLayout.addWidget(self.userNameLabel)


        self.friendsFrameLayout.addWidget(self.userNameNPhotoContainer, 0, Qt.AlignLeft)


        if self.parent is self.ui.addFriendsPage:
            self.__createAddButton()


        elif self.parent is self.ui.friendRequestPage:
            self.__createRequestButtons()

        elif self.parent is self.ui.friendsPage:
            self.__createFriendButtons()
            

        self.parentLayout.addWidget(self.friendsFrame)



    def __createButtonsFrame(self):
        objectNameSuffix = f"-{self.userName}-"
        
        self.userFriendsButtons = QFrame(self.friendsFrame)
        self.userFriendsButtons.setObjectName(f"{objectNameSuffix}userFriendsButtons")
        self.userFriendsButtons.setStyleSheet(u"QFrame { padding: 0px; }")

        self.userFriendsButtons.setFrameShape(QFrame.StyledPanel)
        self.userFriendsButtons.setFrameShadow(QFrame.Raised)

        self.userFriendsButtonsLayout = QHBoxLayout(self.userFriendsButtons)
        self.userFriendsButtonsLayout.setSpacing(10)
        self.userFriendsButtonsLayout.setObjectName(f"{objectNameSuffix}userFriendsButtonsLayout")
        self.userFriendsButtonsLayout.setContentsMargins(0, 0, 0, 0)

        self.friendsFrameLayout.addWidget(self.userFriendsButtons, 0, Qt.AlignRight)



    #######################################################
    #                       Buttons                       #
    #######################################################
    
    
    def __createAddButton(self):
        self.__createButtonsFrame()
        objectNameSuffix = f"-{self.userName}-"

        font = QFont()
        font.setFamilies([u"Righteous"])
        font.setPointSize(9)

        self.sendFriendRequestBtn = QPushButton(self.userFriendsButtons)
        self.sendFriendRequestBtn.setObjectName(f"{objectNameSuffix}sendFriendRequestBtn")
        self.sendFriendRequestBtn.setCursor(QCursor(Qt.PointingHandCursor))

        if self.requestSent:
            text = "SENT"
            btnFunc = lambda: self.signals.requestSignal.cancelFriendRequest.emit(self.friendId)
            self.sendFriendRequestBtn.setStyleSheet(self.__sendFriendRequestBtnStyleSheet(requestSent=True))
        else:
            text = "ADD"
            btnFunc = lambda: self.signals.requestSignal.sendFriendRequest.emit(self.friendId)
            self.sendFriendRequestBtn.setStyleSheet(self.__sendFriendRequestBtnStyleSheet())


        self.sendFriendRequestBtn.setText(text)
        self.sendFriendRequestBtn.setFont(font)
        self.sendFriendRequestBtn.clicked.connect(btnFunc)

        def onFriendRequestSent(friendId):
            if self.friendId == friendId:
                btnFunc = lambda: self.signals.requestSignal.cancelFriendRequest.emit(self.friendId)
                self.sendFriendRequestBtn.setText("SENT")
                self.sendFriendRequestBtn.setStyleSheet(self.__sendFriendRequestBtnStyleSheet(requestSent=True))
                self.sendFriendRequestBtn.clicked.disconnect()
                self.sendFriendRequestBtn.clicked.connect(btnFunc)


        def onFriendRequestCanceled(friendId):
            if self.friendId == friendId:
                btnFunc = lambda: self.signals.requestSignal.sendFriendRequest.emit(self.friendId)
                self.sendFriendRequestBtn.setText("ADD")
                self.sendFriendRequestBtn.setStyleSheet(self.__sendFriendRequestBtnStyleSheet())
                self.sendFriendRequestBtn.clicked.disconnect()
                self.sendFriendRequestBtn.clicked.connect(btnFunc)


        self.signals.responseSignal.friendRequestSent.connect(onFriendRequestSent)
        self.signals.responseSignal.friendRequestCanceled.connect(onFriendRequestCanceled)



        self.userFriendsButtonsLayout.addWidget(self.sendFriendRequestBtn) 
    


    def __createRequestButtons(self):
        self.__createButtonsFrame()
        objectNameSuffix = f"-{self.userName}-"
            
        self.acceptFriendRequstBtn = QPushButton(self.userFriendsButtons)
        self.acceptFriendRequstBtn.setObjectName(f"{objectNameSuffix}acceptFriendRequstBtn")
        self.acceptFriendRequstBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.acceptFriendRequstBtn.setStyleSheet(self.__requestBtnStyleSheet())
        
        acceptIcon = QIcon()
        acceptIcon.addFile(u":/Icons/Icons/done_FILL1_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.acceptFriendRequstBtn.setIcon(acceptIcon)

        acceptBtnFunc = lambda: self.signals.requestSignal.acceptFriendRequest.emit(self.friendId)
        self.acceptFriendRequstBtn.clicked.connect(acceptBtnFunc)


        self.userFriendsButtonsLayout.addWidget(self.acceptFriendRequstBtn)   
        self.declineFriendRequestBtn = QPushButton(self.userFriendsButtons)
        self.declineFriendRequestBtn.setObjectName(f"{objectNameSuffix}declineFriendRequestBtn")
        self.declineFriendRequestBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.declineFriendRequestBtn.setStyleSheet(self.__requestBtnStyleSheet())
        
        declineIcon = QIcon()
        declineIcon.addFile(u":/Icons/Icons/close_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.declineFriendRequestBtn.setIcon(declineIcon)

        declineBtnFunc = lambda: self.signals.requestSignal.declineFriendRequest.emit(self.friendId)
        self.declineFriendRequestBtn.clicked.connect(declineBtnFunc)

        self.userFriendsButtonsLayout.addWidget(self.declineFriendRequestBtn)


    def __createFriendButtons(self):
        self.__createButtonsFrame()

        objectNameSuffix = f"-{self.userName}-"
            
        self.chatBtn = QPushButton(self.userFriendsButtons)
        self.chatBtn.setObjectName(f"{objectNameSuffix}chatBtn")
        self.chatBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.chatBtn.setStyleSheet(self.__requestBtnStyleSheet())
        
        chatIcon = QIcon()
        chatIcon.addFile(u":/Icons/Icons/chat_bubble_FILL1_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.chatBtn.setIcon(chatIcon)

        self.chatBtn.clicked.connect(lambda: self.window.chatManager.addChat(self.userName, self.userPhoto))


        self.userFriendsButtonsLayout.addWidget(self.chatBtn)   
        self.deleteFriendBtn = QPushButton(self.userFriendsButtons)
        self.deleteFriendBtn.setObjectName(f"{objectNameSuffix}deleteFriendBtn")
        self.deleteFriendBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteFriendBtn.setStyleSheet(self.__requestBtnStyleSheet())
        
        deleteIcon = QIcon()
        deleteIcon.addFile(u":/Icons/Icons/close_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteFriendBtn.setIcon(deleteIcon)

        # declineBtnFunc = lambda: self.signals.requestSignal.declineFriendRequest.emit(self.friendId)
        # self.deleteFriendBtn.clicked.connect(declineBtnFunc)

        self.userFriendsButtonsLayout.addWidget(self.deleteFriendBtn)
    
    #######################################################
    #                     StyleSheets                     #
    #######################################################


    def __sendFriendRequestBtnStyleSheet(self, requestSent=False):
        if requestSent:
            return (u"QPushButton {\n"
                    "	color: #DDDDDD;\n"
                    "	background-color: #B30047;\n"
                    "	border: 2px solid #ff0066;\n"
                    "	border-radius: 7px;\n"
                    "	padding: 4px 13px 4px 13px;\n"
                    "}\n"
                    "\n"
                    "QPushButton::hover {\n"
                    "	background-color: #ff0066;\n"
                    "}\n"
                    "\n"
                    "QPushButton::pressed {\n"
                    "	background-color: #B30047;\n"
                    "	border: 2px solid transparent;\n"
                    "}\n"
                    "QPushButton::focus {\n"
                    "outline: none;\n"
                    "}\n")

        else:
            return (u"QPushButton {\n"
                    "	color: #DDDDDD;\n"
                    "	background-color: #5d0cc4;\n"
                    "	border: 2px solid transparent;\n"
                    "	border-radius: 7px;\n"
                    "	padding: 4px 13px 4px 13px;\n"
                    "}\n"
                    "\n"
                    "QPushButton::hover {\n"
                    "	background-color: #610dce;\n"
                    "}\n"
                    "\n"
                    "QPushButton::pressed {\n"
                    "	background-color: #580cbb;\n"
                    "}\n"
                    "QPushButton::focus {\n"
                    "outline: none;\n"
                    "}\n")


    def __requestBtnStyleSheet(self):
        return (u"QPushButton {\n"
                "	background: transparent;\n"
                "	padding: 0px;\n"
                "	icon-size: 26px;\n"
                "}\n"
                "QPushButton::focus {\n"
                "outline: none;\n"
                "}\n")


