from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QAbstractScrollArea, QPlainTextEdit
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont

from client.Window.UI.Animations.message_animation import MessageAnimation


class MessageUI:
    def __init__(self, text, userName, userPhoto, date, time, 
                    chatFrame, chatLayout, messageNumber, 
                    messageWidth):

        self.messageNumber = messageNumber
        self.userPhoto = userPhoto
        self.userName = userName
        self.date = date
        self.time = time

        self._heightIncrement = 18

        self._setupUI(text, chatFrame, chatLayout, 
                    messageWidth)

        

        self._animation = MessageAnimation(self.messageTextEdit, b"minimumSize")



    def _setupUI(self, text, chatFrame, chatLayout, 
                    messageWidth):

        objectNameSuffix = f"-{self.userName}-{self.messageNumber}"

        #############################
        font2 = QFont()
        font2.setFamily(u"Righteous")
        font2.setPointSize(10)

        font3 = QFont()
        font3.setFamily(u"Righteous")
        font3.setPointSize(11)

        font5 = QFont()
        font5.setFamily(u"Righteous")
        font5.setPointSize(8)
        #############################

        ### messageFrame = chat_frame
        
        self.messageFrame = QFrame(chatFrame)
        self.messageFrame.setObjectName(f"messageFrame{objectNameSuffix}")
        self.messageFrame.setFrameShape(QFrame.StyledPanel)
        self.messageFrame.setFrameShadow(QFrame.Raised)
        

        ### messageFrameLayout = head_vertical_layout
        
        self.messageFrameLayout = QVBoxLayout(self.messageFrame)
        self.messageFrameLayout.setSpacing(0)
        self.messageFrameLayout.setObjectName(f"messageFrameLayout{objectNameSuffix}")
        self.messageFrameLayout.setContentsMargins(0, 0, 0, 0)

        ### userInfoFrame = user_frame
        
        self._userInfoFrame = QFrame(self.messageFrame)
        self._userInfoFrame.setObjectName(f"userInfoFrame{objectNameSuffix}")
        self._userInfoFrame.setFrameShape(QFrame.StyledPanel)
        self._userInfoFrame.setFrameShadow(QFrame.Raised)

        ### userInfoFrameLayout = user_horizontal_layout
        self._userInfoFrameLayout = QHBoxLayout(self._userInfoFrame)
        self._userInfoFrameLayout.setSpacing(9)
        self._userInfoFrameLayout.setObjectName(f"userInfoFrameLayout{objectNameSuffix}")
        self._userInfoFrameLayout.setContentsMargins(5, 0, 0, 0)

        ### userPhoto = user_photo
        self._userPhoto = QLabel(self._userInfoFrame)
        self._userPhoto.setObjectName(f"userPhoto{objectNameSuffix}")
        self._userPhoto.setMinimumSize(QSize(40, 40))
        self._userPhoto.setMaximumSize(QSize(40, 40))
        self._userPhoto.setStyleSheet(u"border: none;\n"
        "background: gray;\n"
        "border-radius: 20px;")

        self._userInfoFrameLayout.addWidget(self._userPhoto)

        ### userNameNDateFrame = usernameNDate
        self._userNameNDateFrame = QFrame(self._userInfoFrame)
        self._userNameNDateFrame.setObjectName(f"userNameNDateFrame{objectNameSuffix}")
        self._userNameNDateFrame.setFrameShape(QFrame.StyledPanel)
        self._userNameNDateFrame.setFrameShadow(QFrame.Raised)
        
        ###################
        

        ### userNameNDateFrameLayout = und_layout
        self._userNameNDateFrameLayout = QHBoxLayout(self._userNameNDateFrame)
        self._userNameNDateFrameLayout.setSpacing(5)
        self._userNameNDateFrameLayout.setObjectName(f"userNameNDateFrameLayout{objectNameSuffix}")
        self._userNameNDateFrameLayout.setContentsMargins(0, 0, 0, 0)


        self._userName = QLabel(self._userNameNDateFrame)
        self._userName.setObjectName(f"userName{objectNameSuffix}")
        self._userName.setFont(font3)
        self._userName.setStyleSheet(u"border:none")
        self._userName.setText(self.userName)

        self._userNameNDateFrameLayout.addWidget(self._userName)

        self._date = QLabel(self._userNameNDateFrame)
        self._date.setObjectName(f"date{objectNameSuffix}")
        self._date.setStyleSheet(u"border: none")
        self._date.setText(self.date)

        self._userNameNDateFrameLayout.addWidget(self._date)

        ################### ################
        self._userInfoFrameLayout.addWidget(self._userNameNDateFrame, 0, Qt.AlignLeft)
        self.messageFrameLayout.addWidget(self._userInfoFrame)

        ### messageTextFrame = message_frame
        self._messageTextFrame = QFrame(self.messageFrame)
        self._messageTextFrame.setObjectName(f"messageTextFrame{objectNameSuffix}")
        self._messageTextFrame.setFrameShape(QFrame.StyledPanel)
        self._messageTextFrame.setFrameShadow(QFrame.Raised)

        ### messageTextFrameLayout = msg_horizontal_layout
        self._messageTextFrameLayout = QHBoxLayout(self._messageTextFrame)
        self._messageTextFrameLayout.setSpacing(7)
        self._messageTextFrameLayout.setObjectName(f"messageTextFrameLayout{objectNameSuffix}")
        self._messageTextFrameLayout.setContentsMargins(8, 0, 0, -1)

        ### timeFrame = time_frame
        self._timeFrame = QFrame(self._messageTextFrame)
        self._timeFrame.setObjectName(f"timeFrame{objectNameSuffix}")
        self._timeFrame.setFrameShape(QFrame.StyledPanel)
        self._timeFrame.setFrameShadow(QFrame.Raised)
        self._timeFrame.setStyleSheet(u"border: none;\n"
        "margin-top: 3px")

        ### timeFrameLayout = time_vertical_layout
        self._timeFrameLayout = QVBoxLayout(self._timeFrame)
        self._timeFrameLayout.setSpacing(0)
        self._timeFrameLayout.setObjectName(f"timeFrameLayout{objectNameSuffix}")
        self._timeFrameLayout.setContentsMargins(0, 0, 0, 0)

        ### timeLabel = time_1_label
        self._timeLabel = QLabel(self._timeFrame)
        self._timeLabel.setObjectName(f"timeLabel{objectNameSuffix}")
        self._timeLabel.setFont(font5)
        self._timeLabel.setText(self.time)

        self._timeFrameLayout.addWidget(self._timeLabel)

        self._messageTextFrameLayout.addWidget(self._timeFrame, 0, Qt.AlignTop)

        ### messageTextEdit = message_text
        self.messageTextEdit = QPlainTextEdit(self._messageTextFrame)
        self.messageTextEdit.setObjectName(f"messageTextEdit{objectNameSuffix}")
        self.messageTextEdit.setFont(font2)
        self.messageTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.messageTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.messageTextEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.messageTextEdit.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        self.messageTextEdit.setReadOnly(True)
        self.messageTextEdit.setTabStopDistance(20)
        self.messageTextEdit.setPlainText(text)
        self.messageTextEdit.setMinimumWidth(messageWidth)
        self.messageTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
            "	border: none;\n"
            "}\n"
            "\n"
            "QScrollBar:vertical {\n"
            "	background-color: #27282D;\n"
            "	border: none;\n"
            "	width: 4px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:vertical {\n"
            "	background: none;\n"
            "	min-height: 10px;\n"
            "	border-radius: 2px;\n"
            "}\n"
            "\n"
            "QScrollBar::sub-line:vertical {\n"
            "	border: none;\n"
            "	background: none;\n"
            "	height: 0px;\n"
            "	subcontrol-position: top;\n"
            "    subcontrol-origin: margin;\n"
            "	\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:vertical {\n"
            "	border: none;\n"
            "	background: none;\n"
            "	height: 0px;\n"
            "	subcontrol-position: bottom;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "\n"
            "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "	background: none;\n"
            "}\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "	background: none;\n"
            "}\n"
            "")

        self.messageTextEdit.wheelEvent = lambda event: None
        self._messageTextFrameLayout.addWidget(self.messageTextEdit, 0, Qt.AlignTop)


        self.messageFrameLayout.addWidget(self._messageTextFrame)
        
        chatLayout.addWidget(self.messageFrame, 0, Qt.AlignLeft|Qt.AlignBottom)
    
   
   
    
    
    def resize(self, width):
        height = self.messageTextEdit.document().lineCount() * self._heightIncrement
        self.messageTextEdit.setMinimumSize(QSize(width, height))
    
    
    
    def setMinimumSize(self, width, height=None):
        if height is None:
            height = self.messageTextEdit.document().lineCount() * self._heightIncrement

        self.messageTextEdit.setMinimumSize(QSize(width, height))


    def hide(self):
        self.messageFrame.hide()

    def show(self):
        self.messageFrame.show()
    
    def startAnimation(self, friendsContainerClosed, duration):
        self._animation.slide(friendsContainerClosed, duration)

