# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
import client.Window.UI.icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1252, 765)
        MainWindow.setMinimumSize(QSize(1070, 650))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setStyleSheet(u"background-color: #27282D;\n"
"color: #63646B;\n"
"font-family: \"Righteous\";")
        self.centralWidgetLayout = QVBoxLayout(self.centralWidget)
        self.centralWidgetLayout.setSpacing(0)
        self.centralWidgetLayout.setObjectName(u"centralWidgetLayout")
        self.centralWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.titleBar = QFrame(self.centralWidget)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setStyleSheet(u"background-color: #17181c;")
        self.titleBar.setFrameShape(QFrame.StyledPanel)
        self.titleBar.setFrameShadow(QFrame.Raised)
        self.titleBarLayout = QHBoxLayout(self.titleBar)
        self.titleBarLayout.setSpacing(0)
        self.titleBarLayout.setObjectName(u"titleBarLayout")
        self.titleBarLayout.setContentsMargins(0, 0, 0, 0)
        self.appName = QLabel(self.titleBar)
        self.appName.setObjectName(u"appName")
        font = QFont()
        font.setFamilies([u"Righteous"])
        font.setPointSize(9)
        self.appName.setFont(font)
        self.appName.setStyleSheet(u"padding-left: 3px;\n"
"color: white;\n"
"")
        self.appName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.appName.setMargin(0)

        self.titleBarLayout.addWidget(self.appName, 0, Qt.AlignLeft|Qt.AlignTop)

        self.command = QFrame(self.titleBar)
        self.command.setObjectName(u"command")
        self.command.setMinimumSize(QSize(100, 0))
        self.command.setStyleSheet(u"")
        self.command.setFrameShape(QFrame.StyledPanel)
        self.command.setFrameShadow(QFrame.Raised)
        self.commandLayout = QHBoxLayout(self.command)
        self.commandLayout.setSpacing(0)
        self.commandLayout.setObjectName(u"commandLayout")
        self.commandLayout.setContentsMargins(0, 0, 0, 0)
        self.line = QFrame(self.command)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.commandLayout.addWidget(self.line)

        self.appMinimize = QPushButton(self.command)
        self.appMinimize.setObjectName(u"appMinimize")
        self.appMinimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.appMinimize.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: #1E1F23;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/minimize_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.appMinimize.setIcon(icon)

        self.commandLayout.addWidget(self.appMinimize, 0, Qt.AlignTop)

        self.appFullscreenToggle = QPushButton(self.command)
        self.appFullscreenToggle.setObjectName(u"appFullscreenToggle")
        self.appFullscreenToggle.setCursor(QCursor(Qt.PointingHandCursor))
        self.appFullscreenToggle.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: #1E1F23;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/stop_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.appFullscreenToggle.setIcon(icon1)

        self.commandLayout.addWidget(self.appFullscreenToggle, 0, Qt.AlignTop)

        self.appExit = QPushButton(self.command)
        self.appExit.setObjectName(u"appExit")
        self.appExit.setCursor(QCursor(Qt.PointingHandCursor))
        self.appExit.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: #2B0758;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Icons/close_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.appExit.setIcon(icon2)

        self.commandLayout.addWidget(self.appExit)


        self.titleBarLayout.addWidget(self.command, 0, Qt.AlignRight|Qt.AlignTop)


        self.centralWidgetLayout.addWidget(self.titleBar)

        self.application = QStackedWidget(self.centralWidget)
        self.application.setObjectName(u"application")
        self.application.setStyleSheet(u"QStackedWidget {\n"
"	border: none;\n"
"}\n"
"\n"
"")
        self.loginScreen = QWidget()
        self.loginScreen.setObjectName(u"loginScreen")
        self.loginScreenLayout = QHBoxLayout(self.loginScreen)
        self.loginScreenLayout.setSpacing(0)
        self.loginScreenLayout.setObjectName(u"loginScreenLayout")
        self.loginScreenLayout.setContentsMargins(0, 0, 0, 0)
        self.loginForm = QFrame(self.loginScreen)
        self.loginForm.setObjectName(u"loginForm")
        self.loginForm.setMinimumSize(QSize(350, 245))
        self.loginForm.setFrameShape(QFrame.StyledPanel)
        self.loginForm.setFrameShadow(QFrame.Raised)
        self.loginFormLayout = QVBoxLayout(self.loginForm)
        self.loginFormLayout.setSpacing(0)
        self.loginFormLayout.setObjectName(u"loginFormLayout")
        self.loginFormLayout.setContentsMargins(0, 0, 0, 0)
        self.emailBox = QFrame(self.loginForm)
        self.emailBox.setObjectName(u"emailBox")
        self.emailBox.setFrameShape(QFrame.StyledPanel)
        self.emailBox.setFrameShadow(QFrame.Raised)
        self.emailBoxLayout = QVBoxLayout(self.emailBox)
        self.emailBoxLayout.setSpacing(3)
        self.emailBoxLayout.setObjectName(u"emailBoxLayout")
        self.emailBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.emailLabel = QLabel(self.emailBox)
        self.emailLabel.setObjectName(u"emailLabel")
        font1 = QFont()
        font1.setFamilies([u"Righteous"])
        font1.setPointSize(12)
        self.emailLabel.setFont(font1)
        self.emailLabel.setStyleSheet(u"padding-left: 5px")

        self.emailBoxLayout.addWidget(self.emailLabel, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.emailInput = QLineEdit(self.emailBox)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setStyleSheet(u"QLineEdit {\n"
"	background: #18181A;\n"
"	border-style: outset;\n"
"	border-radius : 13px;\n"
"	border : 2px solid transparent;\n"
"	padding-top: 4px;\n"
"	padding-bottom: 4px;\n"
"	padding-left: 8px;\n"
"	color: white;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"	background: #212123;\n"
"}")

        self.emailBoxLayout.addWidget(self.emailInput)


        self.loginFormLayout.addWidget(self.emailBox, 0, Qt.AlignVCenter)

        self.passwordBox = QFrame(self.loginForm)
        self.passwordBox.setObjectName(u"passwordBox")
        self.passwordBox.setFrameShape(QFrame.StyledPanel)
        self.passwordBox.setFrameShadow(QFrame.Raised)
        self.passwordBoxLayout = QVBoxLayout(self.passwordBox)
        self.passwordBoxLayout.setSpacing(3)
        self.passwordBoxLayout.setObjectName(u"passwordBoxLayout")
        self.passwordBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.passwordLabel = QLabel(self.passwordBox)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setFont(font1)
        self.passwordLabel.setStyleSheet(u"padding-left: 5px")

        self.passwordBoxLayout.addWidget(self.passwordLabel, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.passwordInput = QLineEdit(self.passwordBox)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setStyleSheet(u"QLineEdit {\n"
"	background: #18181A;\n"
"	border-style: outset;\n"
"	border-radius : 13px;\n"
"	border : 2px solid transparent;\n"
"	padding-top: 4px;\n"
"	padding-bottom: 4px;\n"
"	padding-left: 8px;\n"
"	color: white;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"	background: #212123;\n"
"}")
        self.passwordInput.setFrame(True)
        self.passwordInput.setEchoMode(QLineEdit.Password)

        self.passwordBoxLayout.addWidget(self.passwordInput)

        self.forgotYourPasswordBtn = QPushButton(self.passwordBox)
        self.forgotYourPasswordBtn.setObjectName(u"forgotYourPasswordBtn")
        self.forgotYourPasswordBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.forgotYourPasswordBtn.setStyleSheet(u"QPushButton  {\n"
"	background: transparent;\n"
"	color: #0066FF;\n"
"	padding-left: 7px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	color: #3484FD;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none\n"
"}")

        self.passwordBoxLayout.addWidget(self.forgotYourPasswordBtn, 0, Qt.AlignLeft)


        self.loginFormLayout.addWidget(self.passwordBox, 0, Qt.AlignTop)

        self.loginBox = QFrame(self.loginForm)
        self.loginBox.setObjectName(u"loginBox")
        self.loginBox.setFrameShape(QFrame.StyledPanel)
        self.loginBox.setFrameShadow(QFrame.Raised)
        self.loginBoxLayout = QVBoxLayout(self.loginBox)
        self.loginBoxLayout.setSpacing(3)
        self.loginBoxLayout.setObjectName(u"loginBoxLayout")
        self.loginBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.loginCredentialsStatusLabel = QLabel(self.loginBox)
        self.loginCredentialsStatusLabel.setObjectName(u"loginCredentialsStatusLabel")
        font2 = QFont()
        font2.setFamilies([u"Righteous"])
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setItalic(True)
        font2.setKerning(True)
        self.loginCredentialsStatusLabel.setFont(font2)
        self.loginCredentialsStatusLabel.setStyleSheet(u"padding-left: 5px;\n"
"color: #B12323")

        self.loginBoxLayout.addWidget(self.loginCredentialsStatusLabel)

        self.loginBtn = QPushButton(self.loginBox)
        self.loginBtn.setObjectName(u"loginBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginBtn.sizePolicy().hasHeightForWidth())
        self.loginBtn.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Righteous"])
        font3.setPointSize(10)
        self.loginBtn.setFont(font3)
        self.loginBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginBtn.setLayoutDirection(Qt.LeftToRight)
        self.loginBtn.setStyleSheet(u"QPushButton {\n"
"background: #420096;\n"
"border-radius : 12px;\n"
"border : 2px solid transparent;\n"
"padding-top: 3px;\n"
"padding-bottom: 3px;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: #5A0DBC;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	background: #420096;\n"
"	border: 1px solid #3E008C;\n"
"	border-style: inset;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none\n"
"}")

        self.loginBoxLayout.addWidget(self.loginBtn)

        self.toRegisterBox = QFrame(self.loginBox)
        self.toRegisterBox.setObjectName(u"toRegisterBox")
        self.toRegisterBox.setFrameShape(QFrame.StyledPanel)
        self.toRegisterBox.setFrameShadow(QFrame.Raised)
        self.toRegisterBoxLayout = QHBoxLayout(self.toRegisterBox)
        self.toRegisterBoxLayout.setSpacing(0)
        self.toRegisterBoxLayout.setObjectName(u"toRegisterBoxLayout")
        self.toRegisterBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.needAnAccountlabel = QLabel(self.toRegisterBox)
        self.needAnAccountlabel.setObjectName(u"needAnAccountlabel")
        self.needAnAccountlabel.setFont(font)
        self.needAnAccountlabel.setStyleSheet(u"padding-left: 5px")

        self.toRegisterBoxLayout.addWidget(self.needAnAccountlabel, 0, Qt.AlignRight)

        self.toRegisterScreenBtn = QPushButton(self.toRegisterBox)
        self.toRegisterScreenBtn.setObjectName(u"toRegisterScreenBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toRegisterScreenBtn.sizePolicy().hasHeightForWidth())
        self.toRegisterScreenBtn.setSizePolicy(sizePolicy1)
        self.toRegisterScreenBtn.setMaximumSize(QSize(50, 16777215))
        self.toRegisterScreenBtn.setFont(font)
        self.toRegisterScreenBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.toRegisterScreenBtn.setStyleSheet(u"QPushButton  {\n"
"	background: transparent;\n"
"	color: #0066FF;\n"
"	text-align: left\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	color: #3484FD;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none\n"
"}")

        self.toRegisterBoxLayout.addWidget(self.toRegisterScreenBtn, 0, Qt.AlignLeft)


        self.loginBoxLayout.addWidget(self.toRegisterBox, 0, Qt.AlignLeft)


        self.loginFormLayout.addWidget(self.loginBox, 0, Qt.AlignVCenter)


        self.loginScreenLayout.addWidget(self.loginForm, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.application.addWidget(self.loginScreen)
        self.loadingScreen = QWidget()
        self.loadingScreen.setObjectName(u"loadingScreen")
        self.verticalLayout_13 = QVBoxLayout(self.loadingScreen)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.loadingBox = QFrame(self.loadingScreen)
        self.loadingBox.setObjectName(u"loadingBox")
        self.loadingBox.setMaximumSize(QSize(326, 75))
        self.loadingBox.setFrameShape(QFrame.StyledPanel)
        self.loadingBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.loadingBox)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.loadingLabel = QLabel(self.loadingBox)
        self.loadingLabel.setObjectName(u"loadingLabel")
        font4 = QFont()
        font4.setFamilies([u"Righteous"])
        font4.setPointSize(72)
        self.loadingLabel.setFont(font4)
        self.loadingLabel.setStyleSheet(u"")
        self.loadingLabel.setPixmap(QPixmap(u"../../../../res/logo.png"))
        self.loadingLabel.setScaledContents(True)

        self.verticalLayout_12.addWidget(self.loadingLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_13.addWidget(self.loadingBox, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.application.addWidget(self.loadingScreen)
        self.registerScreen = QWidget()
        self.registerScreen.setObjectName(u"registerScreen")
        self.registerScreenLayout = QHBoxLayout(self.registerScreen)
        self.registerScreenLayout.setSpacing(0)
        self.registerScreenLayout.setObjectName(u"registerScreenLayout")
        self.registerScreenLayout.setContentsMargins(0, 0, 0, 0)
        self.registerForm = QFrame(self.registerScreen)
        self.registerForm.setObjectName(u"registerForm")
        self.registerForm.setMinimumSize(QSize(350, 450))
        self.registerForm.setFrameShape(QFrame.StyledPanel)
        self.registerForm.setFrameShadow(QFrame.Raised)
        self.registerFormLayout = QVBoxLayout(self.registerForm)
        self.registerFormLayout.setSpacing(0)
        self.registerFormLayout.setObjectName(u"registerFormLayout")
        self.registerFormLayout.setContentsMargins(0, 0, 0, 0)
        self.emailBoxR = QFrame(self.registerForm)
        self.emailBoxR.setObjectName(u"emailBoxR")
        self.emailBoxR.setFrameShape(QFrame.StyledPanel)
        self.emailBoxR.setFrameShadow(QFrame.Raised)
        self.emailBoxRLayout = QVBoxLayout(self.emailBoxR)
        self.emailBoxRLayout.setSpacing(1)
        self.emailBoxRLayout.setObjectName(u"emailBoxRLayout")
        self.emailBoxRLayout.setContentsMargins(0, 0, 0, 0)
        self.emailBoxLabel = QFrame(self.emailBoxR)
        self.emailBoxLabel.setObjectName(u"emailBoxLabel")
        self.emailBoxLabel.setFrameShape(QFrame.StyledPanel)
        self.emailBoxLabel.setFrameShadow(QFrame.Raised)
        self.emailBoxLabelLayout = QHBoxLayout(self.emailBoxLabel)
        self.emailBoxLabelLayout.setSpacing(0)
        self.emailBoxLabelLayout.setObjectName(u"emailBoxLabelLayout")
        self.emailBoxLabelLayout.setContentsMargins(0, 0, 0, 0)
        self.emailLabelR = QLabel(self.emailBoxLabel)
        self.emailLabelR.setObjectName(u"emailLabelR")
        self.emailLabelR.setFont(font1)
        self.emailLabelR.setStyleSheet(u"padding-left: 5px")

        self.emailBoxLabelLayout.addWidget(self.emailLabelR, 0, Qt.AlignRight)

        self.emailStatusLabel = QLabel(self.emailBoxLabel)
        self.emailStatusLabel.setObjectName(u"emailStatusLabel")
        self.emailStatusLabel.setFont(font3)
        self.emailStatusLabel.setStyleSheet(u"font-size: 10;\n"
"color: #B12323")

        self.emailBoxLabelLayout.addWidget(self.emailStatusLabel, 0, Qt.AlignLeft)


        self.emailBoxRLayout.addWidget(self.emailBoxLabel, 0, Qt.AlignLeft)

        self.emailInputR = QLineEdit(self.emailBoxR)
        self.emailInputR.setObjectName(u"emailInputR")
        font5 = QFont()
        font5.setFamilies([u"Righteous"])
        font5.setPointSize(11)
        self.emailInputR.setFont(font5)
        self.emailInputR.setStyleSheet(u"QLineEdit {\n"
"	background: #18181A;\n"
"	border-style: outset;\n"
"	border-radius : 13px;\n"
"	border : 2px solid transparent;\n"
"	padding-top: 3px;\n"
"	padding-bottom: 3px;\n"
"	padding-left: 8px;\n"
"	color: white;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"	background: #212123;\n"
"}")

        self.emailBoxRLayout.addWidget(self.emailInputR)


        self.registerFormLayout.addWidget(self.emailBoxR, 0, Qt.AlignTop)

        self.usernameBox = QFrame(self.registerForm)
        self.usernameBox.setObjectName(u"usernameBox")
        self.usernameBox.setFrameShape(QFrame.StyledPanel)
        self.usernameBox.setFrameShadow(QFrame.Raised)
        self.usernameBoxLayout = QVBoxLayout(self.usernameBox)
        self.usernameBoxLayout.setSpacing(1)
        self.usernameBoxLayout.setObjectName(u"usernameBoxLayout")
        self.usernameBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.usernameBoxLabel = QFrame(self.usernameBox)
        self.usernameBoxLabel.setObjectName(u"usernameBoxLabel")
        self.usernameBoxLabel.setFrameShape(QFrame.StyledPanel)
        self.usernameBoxLabel.setFrameShadow(QFrame.Raised)
        self.usernameBoxLabelLayout = QHBoxLayout(self.usernameBoxLabel)
        self.usernameBoxLabelLayout.setSpacing(0)
        self.usernameBoxLabelLayout.setObjectName(u"usernameBoxLabelLayout")
        self.usernameBoxLabelLayout.setContentsMargins(0, 0, 0, 0)
        self.usernameLabel = QLabel(self.usernameBoxLabel)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setFont(font1)
        self.usernameLabel.setStyleSheet(u"padding-left: 5px")

        self.usernameBoxLabelLayout.addWidget(self.usernameLabel, 0, Qt.AlignRight)

        self.usernameStatusLabel = QLabel(self.usernameBoxLabel)
        self.usernameStatusLabel.setObjectName(u"usernameStatusLabel")
        self.usernameStatusLabel.setFont(font3)
        self.usernameStatusLabel.setStyleSheet(u"color: #B12323")

        self.usernameBoxLabelLayout.addWidget(self.usernameStatusLabel, 0, Qt.AlignLeft)


        self.usernameBoxLayout.addWidget(self.usernameBoxLabel, 0, Qt.AlignLeft)

        self.usernameInput = QLineEdit(self.usernameBox)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setFont(font5)
        self.usernameInput.setStyleSheet(u"QLineEdit {\n"
"	background: #18181A;\n"
"	border-style: outset;\n"
"	border-radius : 13px;\n"
"	border : 2px solid transparent;\n"
"	padding-top: 3px;\n"
"	padding-bottom: 3px;\n"
"	padding-left: 8px;\n"
"	color: white;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"	background: #212123;\n"
"}")

        self.usernameBoxLayout.addWidget(self.usernameInput)


        self.registerFormLayout.addWidget(self.usernameBox, 0, Qt.AlignTop)

        self.passwordBoxR = QFrame(self.registerForm)
        self.passwordBoxR.setObjectName(u"passwordBoxR")
        self.passwordBoxR.setFrameShape(QFrame.StyledPanel)
        self.passwordBoxR.setFrameShadow(QFrame.Raised)
        self.passwordBoxRLayout = QVBoxLayout(self.passwordBoxR)
        self.passwordBoxRLayout.setSpacing(1)
        self.passwordBoxRLayout.setObjectName(u"passwordBoxRLayout")
        self.passwordBoxRLayout.setContentsMargins(0, 0, 0, 0)
        self.passwordBoxLabel = QFrame(self.passwordBoxR)
        self.passwordBoxLabel.setObjectName(u"passwordBoxLabel")
        self.passwordBoxLabel.setFrameShape(QFrame.StyledPanel)
        self.passwordBoxLabel.setFrameShadow(QFrame.Raised)
        self.passwordBoxLabelLayout = QHBoxLayout(self.passwordBoxLabel)
        self.passwordBoxLabelLayout.setSpacing(0)
        self.passwordBoxLabelLayout.setObjectName(u"passwordBoxLabelLayout")
        self.passwordBoxLabelLayout.setContentsMargins(0, 0, 0, 0)
        self.passwordLabelR = QLabel(self.passwordBoxLabel)
        self.passwordLabelR.setObjectName(u"passwordLabelR")
        self.passwordLabelR.setFont(font1)
        self.passwordLabelR.setStyleSheet(u"padding-left: 5px")

        self.passwordBoxLabelLayout.addWidget(self.passwordLabelR, 0, Qt.AlignRight)

        self.passwordStatus = QLabel(self.passwordBoxLabel)
        self.passwordStatus.setObjectName(u"passwordStatus")
        self.passwordStatus.setFont(font3)
        self.passwordStatus.setStyleSheet(u"color: #B12323")

        self.passwordBoxLabelLayout.addWidget(self.passwordStatus, 0, Qt.AlignLeft)


        self.passwordBoxRLayout.addWidget(self.passwordBoxLabel, 0, Qt.AlignLeft)

        self.passwordInputR = QLineEdit(self.passwordBoxR)
        self.passwordInputR.setObjectName(u"passwordInputR")
        self.passwordInputR.setFont(font5)
        self.passwordInputR.setStyleSheet(u"QLineEdit {\n"
"	background: #18181A;\n"
"	border-style: outset;\n"
"	border-radius : 13px;\n"
"	border : 2px solid transparent;\n"
"	padding-top: 3px;\n"
"	padding-bottom: 3px;\n"
"	padding-left: 8px;\n"
"	color: white;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"	background: #212123;\n"
"}")
        self.passwordInputR.setEchoMode(QLineEdit.Password)

        self.passwordBoxRLayout.addWidget(self.passwordInputR)


        self.registerFormLayout.addWidget(self.passwordBoxR, 0, Qt.AlignTop)

        self.confirmPasswordBox = QFrame(self.registerForm)
        self.confirmPasswordBox.setObjectName(u"confirmPasswordBox")
        self.confirmPasswordBox.setFrameShape(QFrame.StyledPanel)
        self.confirmPasswordBox.setFrameShadow(QFrame.Raised)
        self.confirmPasswordBoxLayout = QVBoxLayout(self.confirmPasswordBox)
        self.confirmPasswordBoxLayout.setSpacing(1)
        self.confirmPasswordBoxLayout.setObjectName(u"confirmPasswordBoxLayout")
        self.confirmPasswordBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.confirmBoxLabel = QFrame(self.confirmPasswordBox)
        self.confirmBoxLabel.setObjectName(u"confirmBoxLabel")
        self.confirmBoxLabel.setFrameShape(QFrame.StyledPanel)
        self.confirmBoxLabel.setFrameShadow(QFrame.Raised)
        self.confirmBoxLabelLayout = QHBoxLayout(self.confirmBoxLabel)
        self.confirmBoxLabelLayout.setSpacing(0)
        self.confirmBoxLabelLayout.setObjectName(u"confirmBoxLabelLayout")
        self.confirmBoxLabelLayout.setContentsMargins(0, 0, 0, 0)
        self.confirmPasswordLabel = QLabel(self.confirmBoxLabel)
        self.confirmPasswordLabel.setObjectName(u"confirmPasswordLabel")
        self.confirmPasswordLabel.setFont(font1)
        self.confirmPasswordLabel.setStyleSheet(u"padding-left: 5px")

        self.confirmBoxLabelLayout.addWidget(self.confirmPasswordLabel, 0, Qt.AlignRight)

        self.confirmPasswordStatusLabel = QLabel(self.confirmBoxLabel)
        self.confirmPasswordStatusLabel.setObjectName(u"confirmPasswordStatusLabel")
        self.confirmPasswordStatusLabel.setFont(font3)
        self.confirmPasswordStatusLabel.setStyleSheet(u"color: #B12323")

        self.confirmBoxLabelLayout.addWidget(self.confirmPasswordStatusLabel, 0, Qt.AlignLeft)


        self.confirmPasswordBoxLayout.addWidget(self.confirmBoxLabel, 0, Qt.AlignLeft)

        self.confirmPasswordInput = QLineEdit(self.confirmPasswordBox)
        self.confirmPasswordInput.setObjectName(u"confirmPasswordInput")
        self.confirmPasswordInput.setFont(font5)
        self.confirmPasswordInput.setStyleSheet(u"QLineEdit {\n"
"	background: #18181A;\n"
"	border-style: outset;\n"
"	border-radius : 13px;\n"
"	border : 2px solid transparent;\n"
"	padding-top: 3px;\n"
"	padding-bottom: 3px;\n"
"	padding-left: 8px;\n"
"	color: white;\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"	background: #212123;\n"
"}")
        self.confirmPasswordInput.setEchoMode(QLineEdit.Password)

        self.confirmPasswordBoxLayout.addWidget(self.confirmPasswordInput)


        self.registerFormLayout.addWidget(self.confirmPasswordBox, 0, Qt.AlignTop)

        self.dateOfBirthBox = QFrame(self.registerForm)
        self.dateOfBirthBox.setObjectName(u"dateOfBirthBox")
        self.dateOfBirthBox.setStyleSheet(u"QComboBox QAbstractScrollArea {\n"
"	padding-left: 5px;\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"    border: 1px solid transparent;\n"
"	background: #1E1E22;\n"
"	selection-background-color: #212125;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::selection {\n"
"	background: red\n"
"}")
        self.dateOfBirthBox.setFrameShape(QFrame.StyledPanel)
        self.dateOfBirthBox.setFrameShadow(QFrame.Raised)
        self.dateOfBirthBoxLayout = QVBoxLayout(self.dateOfBirthBox)
        self.dateOfBirthBoxLayout.setSpacing(2)
        self.dateOfBirthBoxLayout.setObjectName(u"dateOfBirthBoxLayout")
        self.dateOfBirthBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.dateOfBirthLabel = QLabel(self.dateOfBirthBox)
        self.dateOfBirthLabel.setObjectName(u"dateOfBirthLabel")
        self.dateOfBirthLabel.setFont(font1)
        self.dateOfBirthLabel.setStyleSheet(u"padding-left: 5px")

        self.dateOfBirthBoxLayout.addWidget(self.dateOfBirthLabel, 0, Qt.AlignLeft)

        self.dateOfBirthBoxCB = QFrame(self.dateOfBirthBox)
        self.dateOfBirthBoxCB.setObjectName(u"dateOfBirthBoxCB")
        self.dateOfBirthBoxCB.setFrameShape(QFrame.StyledPanel)
        self.dateOfBirthBoxCB.setFrameShadow(QFrame.Raised)
        self.dateOfBirthBoxCBLayout = QHBoxLayout(self.dateOfBirthBoxCB)
        self.dateOfBirthBoxCBLayout.setObjectName(u"dateOfBirthBoxCBLayout")
        self.dateOfBirthBoxCBLayout.setContentsMargins(0, 0, 0, 0)
        self.monthCB = QComboBox(self.dateOfBirthBoxCB)
        self.monthCB.addItem("")
        self.monthCB.addItem("")
        self.monthCB.addItem("")
        self.monthCB.addItem("")
        self.monthCB.addItem("")
        self.monthCB.setObjectName(u"monthCB")
        self.monthCB.setFont(font5)
        self.monthCB.setCursor(QCursor(Qt.PointingHandCursor))
        self.monthCB.setFocusPolicy(Qt.WheelFocus)
        self.monthCB.setStyleSheet(u"QComboBox {\n"
"	background-color: #1E1E22;\n"
"	padding-top: 3px;\n"
"	padding-bottom: 3px;\n"
"	padding-left: 20px;\n"
"	border: 2px solid #1E1E22;\n"
"	border-radius: 13px;\n"
"	color: white\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	border: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(E:/Programming/Icons/expand_more_FILL0_wght100_GRAD0_opsz24.png);\n"
"	margin-right: 10px\n"
"}\n"
"\n"
"\n"
"QComboBox::on {\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QComboBox::editable {\n"
"	background-color: #27282D;\n"
"	outline: 0px;\n"
"	padding-left: 7px;\n"
"	padding-right: 7px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.monthCB.setEditable(False)
        self.monthCB.setCurrentText(u"")
        self.monthCB.setFrame(False)

        self.dateOfBirthBoxCBLayout.addWidget(self.monthCB)

        self.dayCB = QComboBox(self.dateOfBirthBoxCB)
        self.dayCB.addItem("")
        self.dayCB.setObjectName(u"dayCB")
        self.dayCB.setFont(font5)
        self.dayCB.setCursor(QCursor(Qt.PointingHandCursor))
        self.dayCB.setStyleSheet(u"QComboBox {\n"
"	background-color: #1E1E22;\n"
"	padding-top: 3px;\n"
"	padding-bottom: 3px;\n"
"	padding-left: 20px;\n"
"	border: 2px solid #1E1E22;\n"
"	border-radius: 13px;\n"
"	color: white\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	border: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(E:/Programming/Icons/expand_more_FILL0_wght100_GRAD0_opsz24.png);\n"
"	margin-right: 10px\n"
"}\n"
"\n"
"\n"
"QComboBox::on {\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QComboBox::editable {\n"
"	background-color: #27282D;\n"
"	outline: 0px;\n"
"	padding-left: 7px;\n"
"	padding-right: 7px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.dateOfBirthBoxCBLayout.addWidget(self.dayCB)

        self.yearCB = QComboBox(self.dateOfBirthBoxCB)
        self.yearCB.addItem("")
        self.yearCB.addItem("")
        self.yearCB.addItem("")
        self.yearCB.addItem("")
        self.yearCB.setObjectName(u"yearCB")
        self.yearCB.setFont(font5)
        self.yearCB.setCursor(QCursor(Qt.PointingHandCursor))
        self.yearCB.setStyleSheet(u"QComboBox {\n"
"	background-color: #1E1E22;\n"
"	padding-top: 3px;\n"
"	padding-bottom: 3px;\n"
"	padding-left: 20px;\n"
"	border: 2px solid #1E1E22;\n"
"	border-radius: 13px;\n"
"	color: white\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	border: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(E:/Programming/Icons/expand_more_FILL0_wght100_GRAD0_opsz24.png);\n"
"	margin-right: 10px\n"
"}\n"
"\n"
"\n"
"QComboBox::on {\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QComboBox::editable {\n"
"	background-color: #27282D;\n"
"	outline: 0px;\n"
"	padding-left: 7px;\n"
"	padding-right: 7px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.dateOfBirthBoxCBLayout.addWidget(self.yearCB, 0, Qt.AlignVCenter)

        self.dateOfBirthBoxCBLayout.setStretch(0, 2)
        self.dateOfBirthBoxCBLayout.setStretch(1, 1)
        self.dateOfBirthBoxCBLayout.setStretch(2, 1)

        self.dateOfBirthBoxLayout.addWidget(self.dateOfBirthBoxCB)


        self.registerFormLayout.addWidget(self.dateOfBirthBox, 0, Qt.AlignTop)

        self.registerBox = QFrame(self.registerForm)
        self.registerBox.setObjectName(u"registerBox")
        self.registerBox.setFrameShape(QFrame.StyledPanel)
        self.registerBox.setFrameShadow(QFrame.Raised)
        self.registerBoxLayout = QVBoxLayout(self.registerBox)
        self.registerBoxLayout.setSpacing(3)
        self.registerBoxLayout.setObjectName(u"registerBoxLayout")
        self.registerBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.registerBtn = QPushButton(self.registerBox)
        self.registerBtn.setObjectName(u"registerBtn")
        self.registerBtn.setFont(font5)
        self.registerBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.registerBtn.setStyleSheet(u"QPushButton {\n"
"background: #420096;\n"
"border-radius : 12px;\n"
"border : 2px solid transparent;\n"
"padding-top: 3px;\n"
"padding-bottom: 3px;\n"
"color: white\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: #5A0DBC;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	background: #420096;\n"
"	border: 1px solid #3E008C;\n"
"	border-style: inset;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none\n"
"}")

        self.registerBoxLayout.addWidget(self.registerBtn)

        self.signInBox = QFrame(self.registerBox)
        self.signInBox.setObjectName(u"signInBox")
        self.signInBox.setFrameShape(QFrame.StyledPanel)
        self.signInBox.setFrameShadow(QFrame.Raised)
        self.signInBoxLayout = QHBoxLayout(self.signInBox)
        self.signInBoxLayout.setSpacing(0)
        self.signInBoxLayout.setObjectName(u"signInBoxLayout")
        self.signInBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.ahaaLabel = QLabel(self.signInBox)
        self.ahaaLabel.setObjectName(u"ahaaLabel")
        self.ahaaLabel.setFont(font)
        self.ahaaLabel.setStyleSheet(u"padding-left: 5px")

        self.signInBoxLayout.addWidget(self.ahaaLabel, 0, Qt.AlignRight)

        self.signInBtn = QPushButton(self.signInBox)
        self.signInBtn.setObjectName(u"signInBtn")
        self.signInBtn.setFont(font)
        self.signInBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.signInBtn.setStyleSheet(u"QPushButton  {\n"
"	background: transparent;\n"
"	color: #0066FF;\n"
"	text-align: left\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	color: #3484FD;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none\n"
"}")

        self.signInBoxLayout.addWidget(self.signInBtn, 0, Qt.AlignLeft)


        self.registerBoxLayout.addWidget(self.signInBox, 0, Qt.AlignLeft)


        self.registerFormLayout.addWidget(self.registerBox, 0, Qt.AlignBottom)


        self.registerScreenLayout.addWidget(self.registerForm, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.application.addWidget(self.registerScreen)
        self.mainScreen = QWidget()
        self.mainScreen.setObjectName(u"mainScreen")
        self.mainScreen.setStyleSheet(u"QFrame {\n"
"	background-color: #1E1F23;\n"
"}")
        self.mainScreenLayout = QHBoxLayout(self.mainScreen)
        self.mainScreenLayout.setSpacing(0)
        self.mainScreenLayout.setObjectName(u"mainScreenLayout")
        self.mainScreenLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QFrame(self.mainScreen)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setStyleSheet(u"")
        self.leftMenuContainer.setFrameShape(QFrame.StyledPanel)
        self.leftMenuContainer.setFrameShadow(QFrame.Raised)
        self.leftMenuContainerLayout = QVBoxLayout(self.leftMenuContainer)
        self.leftMenuContainerLayout.setSpacing(0)
        self.leftMenuContainerLayout.setObjectName(u"leftMenuContainerLayout")
        self.leftMenuContainerLayout.setContentsMargins(0, 0, 0, 0)
        self.userLMBox = QFrame(self.leftMenuContainer)
        self.userLMBox.setObjectName(u"userLMBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.userLMBox.sizePolicy().hasHeightForWidth())
        self.userLMBox.setSizePolicy(sizePolicy2)
        self.userLMBox.setMinimumSize(QSize(229, 131))
        self.userLMBox.setStyleSheet(u"")
        self.userLMBox.setFrameShape(QFrame.StyledPanel)
        self.userLMBox.setFrameShadow(QFrame.Raised)
        self.userLMBoxLayout = QVBoxLayout(self.userLMBox)
        self.userLMBoxLayout.setSpacing(8)
        self.userLMBoxLayout.setObjectName(u"userLMBoxLayout")
        self.userLMBoxLayout.setContentsMargins(0, 15, 0, 0)
        self.userPhotoLMLabel = QLabel(self.userLMBox)
        self.userPhotoLMLabel.setObjectName(u"userPhotoLMLabel")
        self.userPhotoLMLabel.setMinimumSize(QSize(70, 70))
        self.userPhotoLMLabel.setMaximumSize(QSize(70, 70))
        self.userPhotoLMLabel.setStyleSheet(u"QLabel {\n"
"	background-color: gray;\n"
"	background-image: url();\n"
"	background-position: center;\n"
"	border: 0px solid transparent;\n"
"	border-radius: 35px\n"
"}\n"
"\n"
"QLabel::focus {\n"
"	outline: none\n"
"}")
        self.userPhotoLMLabel.setScaledContents(False)
        self.userPhotoLMLabel.setWordWrap(False)

        self.userLMBoxLayout.addWidget(self.userPhotoLMLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.userNameNFriendsLMBox = QFrame(self.userLMBox)
        self.userNameNFriendsLMBox.setObjectName(u"userNameNFriendsLMBox")
        self.userNameNFriendsLMBox.setStyleSheet(u"QFrame {\n"
"	margin-left: 18px;\n"
"}")
        self.userNameNFriendsLMBox.setFrameShape(QFrame.StyledPanel)
        self.userNameNFriendsLMBox.setFrameShadow(QFrame.Raised)
        self.userNameNFriendsLMBoxLayout = QHBoxLayout(self.userNameNFriendsLMBox)
        self.userNameNFriendsLMBoxLayout.setSpacing(0)
        self.userNameNFriendsLMBoxLayout.setObjectName(u"userNameNFriendsLMBoxLayout")
        self.userNameNFriendsLMBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.userNameLMLabel = QLabel(self.userNameNFriendsLMBox)
        self.userNameLMLabel.setObjectName(u"userNameLMLabel")
        font6 = QFont()
        font6.setFamilies([u"Righteous"])
        font6.setPointSize(14)
        self.userNameLMLabel.setFont(font6)
        self.userNameLMLabel.setStyleSheet(u"")
        self.userNameLMLabel.setScaledContents(False)
        self.userNameLMLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.userNameNFriendsLMBoxLayout.addWidget(self.userNameLMLabel, 0, Qt.AlignHCenter)

        self.friendsLMBtn = QPushButton(self.userNameNFriendsLMBox)
        self.friendsLMBtn.setObjectName(u"friendsLMBtn")
        self.friendsLMBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.friendsLMBtn.setAutoFillBackground(False)
        self.friendsLMBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"	icon-size: 26px\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Icons/group_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.friendsLMBtn.setIcon(icon3)
        self.friendsLMBtn.setCheckable(False)

        self.userNameNFriendsLMBoxLayout.addWidget(self.friendsLMBtn, 0, Qt.AlignRight)

        self.userNameNFriendsLMBoxLayout.setStretch(0, 1)

        self.userLMBoxLayout.addWidget(self.userNameNFriendsLMBox)

        self.line_2 = QFrame(self.userLMBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"margin: 0px 10px 0px 10px;\n"
"border: 2px solid #1a1b1e")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.userLMBoxLayout.addWidget(self.line_2)


        self.leftMenuContainerLayout.addWidget(self.userLMBox, 0, Qt.AlignTop)

        self.recentChatLMSA = QScrollArea(self.leftMenuContainer)
        self.recentChatLMSA.setObjectName(u"recentChatLMSA")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.recentChatLMSA.sizePolicy().hasHeightForWidth())
        self.recentChatLMSA.setSizePolicy(sizePolicy3)
        self.recentChatLMSA.setStyleSheet(u"QScrollArea {\n"
"	padding: 5px;\n"
"	border: none;\n"
"}")
        self.recentChatLMSA.setWidgetResizable(True)
        self.leftMenuSAWC = QWidget()
        self.leftMenuSAWC.setObjectName(u"leftMenuSAWC")
        self.leftMenuSAWC.setGeometry(QRect(0, 0, 219, 461))
        self.leftMenuSAWC.setStyleSheet(u"background: transparent;")
        self.leftMenuSAWCLayout = QVBoxLayout(self.leftMenuSAWC)
        self.leftMenuSAWCLayout.setSpacing(0)
        self.leftMenuSAWCLayout.setObjectName(u"leftMenuSAWCLayout")
        self.leftMenuSAWCLayout.setContentsMargins(0, 0, 0, 0)
        self.recentChatLMBox = QFrame(self.leftMenuSAWC)
        self.recentChatLMBox.setObjectName(u"recentChatLMBox")
        self.recentChatLMBox.setFrameShape(QFrame.StyledPanel)
        self.recentChatLMBox.setFrameShadow(QFrame.Raised)
        self.recentChatLMBoxLayout = QVBoxLayout(self.recentChatLMBox)
        self.recentChatLMBoxLayout.setSpacing(0)
        self.recentChatLMBoxLayout.setObjectName(u"recentChatLMBoxLayout")
        self.recentChatLMBoxLayout.setContentsMargins(0, 5, 0, 0)
        self.chatFrame = QFrame(self.recentChatLMBox)
        self.chatFrame.setObjectName(u"chatFrame")
        self.chatFrame.setCursor(QCursor(Qt.PointingHandCursor))
        self.chatFrame.setStyleSheet(u"QFrame {\n"
"	padding: 7px 5px 7px 5px;\n"
"	background: #1E1F23;\n"
"	border: 2px solid transparent;\n"
"	border-bottom: 2px solid #0b0b0e;\n"
"    border-right: 2px solid #17171c;\n"
"	border-left: 2px  solid #cc00cc;\n"
"	border-radius: 7px\n"
"}")
        self.chatFrame.setFrameShape(QFrame.StyledPanel)
        self.chatFrame.setFrameShadow(QFrame.Raised)
        self.chatFrameLayout = QHBoxLayout(self.chatFrame)
        self.chatFrameLayout.setSpacing(0)
        self.chatFrameLayout.setObjectName(u"chatFrameLayout")
        self.chatFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.userNameNPhotoFrame = QFrame(self.chatFrame)
        self.userNameNPhotoFrame.setObjectName(u"userNameNPhotoFrame")
        self.userNameNPhotoFrame.setCursor(QCursor(Qt.PointingHandCursor))
        self.userNameNPhotoFrame.setStyleSheet(u"padding: 0px;\n"
"border: none")
        self.userNameNPhotoFrame.setFrameShape(QFrame.StyledPanel)
        self.userNameNPhotoFrame.setFrameShadow(QFrame.Raised)
        self.userNameNPhotoFrameLayout = QHBoxLayout(self.userNameNPhotoFrame)
        self.userNameNPhotoFrameLayout.setSpacing(7)
        self.userNameNPhotoFrameLayout.setObjectName(u"userNameNPhotoFrameLayout")
        self.userNameNPhotoFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.userPhotoLabelRC = QLabel(self.userNameNPhotoFrame)
        self.userPhotoLabelRC.setObjectName(u"userPhotoLabelRC")
        self.userPhotoLabelRC.setMinimumSize(QSize(40, 40))
        self.userPhotoLabelRC.setMaximumSize(QSize(40, 40))
        self.userPhotoLabelRC.setStyleSheet(u"border: none;\n"
"background: gray;\n"
"border-radius: 20px")

        self.userNameNPhotoFrameLayout.addWidget(self.userPhotoLabelRC)

        self.userNameLabelRC = QLabel(self.userNameNPhotoFrame)
        self.userNameLabelRC.setObjectName(u"userNameLabelRC")
        self.userNameLabelRC.setFont(font1)
        self.userNameLabelRC.setStyleSheet(u"padding: 0px;")

        self.userNameNPhotoFrameLayout.addWidget(self.userNameLabelRC)


        self.chatFrameLayout.addWidget(self.userNameNPhotoFrame, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.closeChatBtnFrame = QFrame(self.chatFrame)
        self.closeChatBtnFrame.setObjectName(u"closeChatBtnFrame")
        self.closeChatBtnFrame.setStyleSheet(u"padding: 0px;\n"
"border: none")
        self.closeChatBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.closeChatBtnFrame.setFrameShadow(QFrame.Raised)
        self.closeChatBtnFrameLayout = QHBoxLayout(self.closeChatBtnFrame)
        self.closeChatBtnFrameLayout.setSpacing(0)
        self.closeChatBtnFrameLayout.setObjectName(u"closeChatBtnFrameLayout")
        self.closeChatBtnFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.closeChatBtn = QPushButton(self.closeChatBtnFrame)
        self.closeChatBtn.setObjectName(u"closeChatBtn")
        self.closeChatBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeChatBtn.setStyleSheet(u"background: transparent;\n"
"padding: 0px;\n"
"icon-size: 24px")
        self.closeChatBtn.setIcon(icon2)

        self.closeChatBtnFrameLayout.addWidget(self.closeChatBtn)


        self.chatFrameLayout.addWidget(self.closeChatBtnFrame, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.recentChatLMBoxLayout.addWidget(self.chatFrame)


        self.leftMenuSAWCLayout.addWidget(self.recentChatLMBox, 0, Qt.AlignTop)

        self.recentChatLMSA.setWidget(self.leftMenuSAWC)

        self.leftMenuContainerLayout.addWidget(self.recentChatLMSA)

        self.settingsLMBox = QFrame(self.leftMenuContainer)
        self.settingsLMBox.setObjectName(u"settingsLMBox")
        self.settingsLMBox.setFrameShape(QFrame.StyledPanel)
        self.settingsLMBox.setFrameShadow(QFrame.Raised)
        self.settingsLMBoxLayout = QVBoxLayout(self.settingsLMBox)
        self.settingsLMBoxLayout.setSpacing(11)
        self.settingsLMBoxLayout.setObjectName(u"settingsLMBoxLayout")
        self.testMessageBtn = QPushButton(self.settingsLMBox)
        self.testMessageBtn.setObjectName(u"testMessageBtn")
        self.testMessageBtn.setStyleSheet(u"QPushButton::focus {\n"
"	outline: none\n"
"}")

        self.settingsLMBoxLayout.addWidget(self.testMessageBtn)

        self.testChatBtn = QPushButton(self.settingsLMBox)
        self.testChatBtn.setObjectName(u"testChatBtn")
        self.testChatBtn.setStyleSheet(u"QPushButton::focus {\n"
"	outline: none\n"
"}")

        self.settingsLMBoxLayout.addWidget(self.testChatBtn)

        self.settingsLMBtn = QPushButton(self.settingsLMBox)
        self.settingsLMBtn.setObjectName(u"settingsLMBtn")
        self.settingsLMBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.settingsLMBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"	icon-size: 26px\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Icons/settings_FILL1_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsLMBtn.setIcon(icon4)

        self.settingsLMBoxLayout.addWidget(self.settingsLMBtn, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.leftMenuContainerLayout.addWidget(self.settingsLMBox, 0, Qt.AlignBottom)


        self.mainScreenLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.friendsContainer = QFrame(self.mainScreen)
        self.friendsContainer.setObjectName(u"friendsContainer")
        self.friendsContainer.setEnabled(True)
        self.friendsContainer.setMinimumSize(QSize(0, 0))
        self.friendsContainer.setMaximumSize(QSize(300, 16777215))
        self.friendsContainer.setStyleSheet(u"QFrame {\n"
"	background-color: #212226;\n"
"}")
        self.friendsContainer.setFrameShape(QFrame.StyledPanel)
        self.friendsContainer.setFrameShadow(QFrame.Raised)
        self.friendsContainerLayout = QVBoxLayout(self.friendsContainer)
        self.friendsContainerLayout.setObjectName(u"friendsContainerLayout")
        self.nameNSearch = QFrame(self.friendsContainer)
        self.nameNSearch.setObjectName(u"nameNSearch")
        self.nameNSearch.setStyleSheet(u"QFrame {\n"
"	padding-top: 15px;\n"
"	border: none;\n"
"}")
        self.nameNSearch.setFrameShape(QFrame.StyledPanel)
        self.nameNSearch.setFrameShadow(QFrame.Raised)
        self.nameNSearchLayout = QVBoxLayout(self.nameNSearch)
        self.nameNSearchLayout.setSpacing(32)
        self.nameNSearchLayout.setObjectName(u"nameNSearchLayout")
        self.nameNSearchLayout.setContentsMargins(0, 0, 0, 0)
        self.friendsLabel = QLabel(self.nameNSearch)
        self.friendsLabel.setObjectName(u"friendsLabel")
        font7 = QFont()
        font7.setFamilies([u"Righteous"])
        font7.setPointSize(16)
        self.friendsLabel.setFont(font7)
        self.friendsLabel.setStyleSheet(u"QFrame {\n"
"	padding-top: 0px\n"
"}")

        self.nameNSearchLayout.addWidget(self.friendsLabel, 0, Qt.AlignHCenter)

        self.searchFrame = QFrame(self.nameNSearch)
        self.searchFrame.setObjectName(u"searchFrame")
        self.searchFrame.setEnabled(True)
        self.searchFrame.setStyleSheet(u"QFrame {\n"
"	background: #A298AE;\n"
"	border: 2px solid #420096;\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-right: 2px;\n"
"	padding-top: 0px\n"
"}")
        self.searchFrame.setFrameShape(QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QFrame.Raised)
        self.searchFrameLayout = QHBoxLayout(self.searchFrame)
        self.searchFrameLayout.setSpacing(0)
        self.searchFrameLayout.setObjectName(u"searchFrameLayout")
        self.searchFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.searchInput = QLineEdit(self.searchFrame)
        self.searchInput.setObjectName(u"searchInput")
        self.searchInput.setEnabled(True)
        self.searchInput.setFont(font3)
        self.searchInput.setStyleSheet(u"QLineEdit {\n"
"	background: transparent;\n"
"	border: none;\n"
"	color: white\n"
"}")

        self.searchFrameLayout.addWidget(self.searchInput)

        self.pushButton_3 = QPushButton(self.searchFrame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/Icons/search_FILL0_wght600_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon5)

        self.searchFrameLayout.addWidget(self.pushButton_3, 0, Qt.AlignRight)


        self.nameNSearchLayout.addWidget(self.searchFrame)


        self.friendsContainerLayout.addWidget(self.nameNSearch)

        self.friendsSA = QScrollArea(self.friendsContainer)
        self.friendsSA.setObjectName(u"friendsSA")
        self.friendsSA.setStyleSheet(u"QWidget {\n"
"	background: #212226;\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollArea {\n"
"	border: none;\n"
"}\n"
"")
        self.friendsSA.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.friendsSA.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.friendsSA.setWidgetResizable(True)
        self.friendsSAWC = QWidget()
        self.friendsSAWC.setObjectName(u"friendsSAWC")
        self.friendsSAWC.setGeometry(QRect(0, 0, 280, 575))
        self.verticalLayout_11 = QVBoxLayout(self.friendsSAWC)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.friendsSW = QStackedWidget(self.friendsSAWC)
        self.friendsSW.setObjectName(u"friendsSW")
        self.friendsSW.setStyleSheet(u"")
        self.friendsPage = QWidget()
        self.friendsPage.setObjectName(u"friendsPage")
        self.friendsPageLayout = QVBoxLayout(self.friendsPage)
        self.friendsPageLayout.setSpacing(0)
        self.friendsPageLayout.setObjectName(u"friendsPageLayout")
        self.friendsPageLayout.setContentsMargins(0, 0, 0, 0)
        self.friendsSW.addWidget(self.friendsPage)
        self.addFriendsPage = QWidget()
        self.addFriendsPage.setObjectName(u"addFriendsPage")
        self.addFriendsPage.setMinimumSize(QSize(0, 0))
        self.addFriendsPageLayout = QVBoxLayout(self.addFriendsPage)
        self.addFriendsPageLayout.setSpacing(0)
        self.addFriendsPageLayout.setObjectName(u"addFriendsPageLayout")
        self.addFriendsPageLayout.setContentsMargins(0, 0, 0, 0)
        self.friendsSW.addWidget(self.addFriendsPage)
        self.friendRequestPage = QWidget()
        self.friendRequestPage.setObjectName(u"friendRequestPage")
        self.friendRequestPage.setMinimumSize(QSize(0, 0))
        self.friendRequestPage.setStyleSheet(u"")
        self.friendRequestPageLayout = QVBoxLayout(self.friendRequestPage)
        self.friendRequestPageLayout.setObjectName(u"friendRequestPageLayout")
        self.friendsSW.addWidget(self.friendRequestPage)
        self.blockListPage = QWidget()
        self.blockListPage.setObjectName(u"blockListPage")
        self.blockListPage.setMinimumSize(QSize(0, 0))
        self.blockListPageLayout = QVBoxLayout(self.blockListPage)
        self.blockListPageLayout.setObjectName(u"blockListPageLayout")
        self.friendsSW.addWidget(self.blockListPage)

        self.verticalLayout_11.addWidget(self.friendsSW, 0, Qt.AlignTop)

        self.friendsSA.setWidget(self.friendsSAWC)

        self.friendsContainerLayout.addWidget(self.friendsSA)

        self.friendsButtonContainer = QFrame(self.friendsContainer)
        self.friendsButtonContainer.setObjectName(u"friendsButtonContainer")
        self.friendsButtonContainer.setEnabled(True)
        self.friendsButtonContainer.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}")
        self.friendsButtonContainer.setFrameShape(QFrame.StyledPanel)
        self.friendsButtonContainer.setFrameShadow(QFrame.Raised)
        self.friendsBtnsLayout = QHBoxLayout(self.friendsButtonContainer)
        self.friendsBtnsLayout.setSpacing(0)
        self.friendsBtnsLayout.setObjectName(u"friendsBtnsLayout")
        self.friendsBtnsLayout.setContentsMargins(0, 0, 0, 0)
        self.friendsButtons = QFrame(self.friendsButtonContainer)
        self.friendsButtons.setObjectName(u"friendsButtons")
        self.friendsButtons.setFrameShape(QFrame.StyledPanel)
        self.friendsButtons.setFrameShadow(QFrame.Raised)
        self.frameLayout = QHBoxLayout(self.friendsButtons)
        self.frameLayout.setSpacing(5)
        self.frameLayout.setObjectName(u"frameLayout")
        self.frameLayout.setContentsMargins(0, 0, 0, 0)
        self.friendsPageBtn = QPushButton(self.friendsButtons)
        self.friendsPageBtn.setObjectName(u"friendsPageBtn")
        self.friendsPageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.friendsPageBtn.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"	padding: 0px;\n"
"	icon-size: 26px;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none\n"
"}")
        self.friendsPageBtn.setIcon(icon3)

        self.frameLayout.addWidget(self.friendsPageBtn)

        self.addFriendsPageBtn = QPushButton(self.friendsButtons)
        self.addFriendsPageBtn.setObjectName(u"addFriendsPageBtn")
        self.addFriendsPageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addFriendsPageBtn.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"	padding: 0px;\n"
"	icon-size: 26px;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/Icons/person_add_FILL1_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addFriendsPageBtn.setIcon(icon6)

        self.frameLayout.addWidget(self.addFriendsPageBtn)

        self.friendRequestPageBtn = QPushButton(self.friendsButtons)
        self.friendRequestPageBtn.setObjectName(u"friendRequestPageBtn")
        self.friendRequestPageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.friendRequestPageBtn.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"	padding: 0px;\n"
"	icon-size: 26px;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/Icons/group_add_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.friendRequestPageBtn.setIcon(icon7)

        self.frameLayout.addWidget(self.friendRequestPageBtn, 0, Qt.AlignBottom)

        self.blockListPageBtn = QPushButton(self.friendsButtons)
        self.blockListPageBtn.setObjectName(u"blockListPageBtn")
        self.blockListPageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.blockListPageBtn.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"	padding: 0px;\n"
"	icon-size: 26px;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/Icons/no_accounts_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.blockListPageBtn.setIcon(icon8)

        self.frameLayout.addWidget(self.blockListPageBtn, 0, Qt.AlignBottom)


        self.friendsBtnsLayout.addWidget(self.friendsButtons, 0, Qt.AlignRight|Qt.AlignBottom)


        self.friendsContainerLayout.addWidget(self.friendsButtonContainer)


        self.mainScreenLayout.addWidget(self.friendsContainer)

        self.chatContainer = QFrame(self.mainScreen)
        self.chatContainer.setObjectName(u"chatContainer")
        sizePolicy3.setHeightForWidth(self.chatContainer.sizePolicy().hasHeightForWidth())
        self.chatContainer.setSizePolicy(sizePolicy3)
        self.chatContainer.setStyleSheet(u"background-color: #27282D;")
        self.chatContainer.setFrameShape(QFrame.StyledPanel)
        self.chatContainer.setFrameShadow(QFrame.Raised)
        self.chatContainerLayout = QVBoxLayout(self.chatContainer)
        self.chatContainerLayout.setSpacing(0)
        self.chatContainerLayout.setObjectName(u"chatContainerLayout")
        self.chatContainerLayout.setContentsMargins(0, 0, 0, 0)
        self.chatInfoBox = QFrame(self.chatContainer)
        self.chatInfoBox.setObjectName(u"chatInfoBox")
        sizePolicy2.setHeightForWidth(self.chatInfoBox.sizePolicy().hasHeightForWidth())
        self.chatInfoBox.setSizePolicy(sizePolicy2)
        self.chatInfoBox.setMinimumSize(QSize(0, 55))
        self.chatInfoBox.setStyleSheet(u"background-color: rgba(30, 31, 35, 0.79);\n"
"padding-right: 10px;")
        self.chatInfoBox.setFrameShape(QFrame.StyledPanel)
        self.chatInfoBox.setFrameShadow(QFrame.Raised)
        self.chatInfoBoxLayout = QHBoxLayout(self.chatInfoBox)
        self.chatInfoBoxLayout.setSpacing(0)
        self.chatInfoBoxLayout.setObjectName(u"chatInfoBoxLayout")
        self.chatInfoBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.userInfoBox = QFrame(self.chatInfoBox)
        self.userInfoBox.setObjectName(u"userInfoBox")
        self.userInfoBox.setMinimumSize(QSize(90, 41))
        self.userInfoBox.setStyleSheet(u"QFrame {\n"
"	margin-left: 15px\n"
"}")
        self.userInfoBox.setFrameShape(QFrame.StyledPanel)
        self.userInfoBox.setFrameShadow(QFrame.Raised)
        self.userInfoBoxLayout = QHBoxLayout(self.userInfoBox)
        self.userInfoBoxLayout.setSpacing(5)
        self.userInfoBoxLayout.setObjectName(u"userInfoBoxLayout")
        self.userInfoBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.userChatPhotoLabel = QLabel(self.userInfoBox)
        self.userChatPhotoLabel.setObjectName(u"userChatPhotoLabel")
        self.userChatPhotoLabel.setMinimumSize(QSize(40, 40))
        self.userChatPhotoLabel.setStyleSheet(u"background: gray;\n"
"border: 0px solid transparent;\n"
"border-radius: 20px;\n"
"margin-left: 0px;")

        self.userInfoBoxLayout.addWidget(self.userChatPhotoLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.userNameNStatusBox = QFrame(self.userInfoBox)
        self.userNameNStatusBox.setObjectName(u"userNameNStatusBox")
        self.userNameNStatusBox.setStyleSheet(u"margin-left: 0px")
        self.userNameNStatusBox.setFrameShape(QFrame.StyledPanel)
        self.userNameNStatusBox.setFrameShadow(QFrame.Raised)
        self.userNameNStatusBoxLayout = QVBoxLayout(self.userNameNStatusBox)
        self.userNameNStatusBoxLayout.setSpacing(0)
        self.userNameNStatusBoxLayout.setObjectName(u"userNameNStatusBoxLayout")
        self.userNameNStatusBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.chatUserNameLabel = QLabel(self.userNameNStatusBox)
        self.chatUserNameLabel.setObjectName(u"chatUserNameLabel")
        self.chatUserNameLabel.setFont(font5)

        self.userNameNStatusBoxLayout.addWidget(self.chatUserNameLabel)

        self.chatUserStatusLabel = QLabel(self.userNameNStatusBox)
        self.chatUserStatusLabel.setObjectName(u"chatUserStatusLabel")

        self.userNameNStatusBoxLayout.addWidget(self.chatUserStatusLabel, 0, Qt.AlignBottom)


        self.userInfoBoxLayout.addWidget(self.userNameNStatusBox, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.chatInfoBoxLayout.addWidget(self.userInfoBox, 0, Qt.AlignLeft)

        self.chatSettingsBtn = QPushButton(self.chatInfoBox)
        self.chatSettingsBtn.setObjectName(u"chatSettingsBtn")
        self.chatSettingsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.chatSettingsBtn.setStyleSheet(u"background-color: transparent;\n"
"outline: none")
        icon9 = QIcon()
        icon9.addFile(u":/Icons/Icons/more_horiz_FILL0_wght700_GRAD200_opsz40.png", QSize(), QIcon.Normal, QIcon.Off)
        self.chatSettingsBtn.setIcon(icon9)
        self.chatSettingsBtn.setIconSize(QSize(35, 43))

        self.chatInfoBoxLayout.addWidget(self.chatSettingsBtn, 0, Qt.AlignRight)


        self.chatContainerLayout.addWidget(self.chatInfoBox, 0, Qt.AlignTop)

        self.chatSA = QScrollArea(self.chatContainer)
        self.chatSA.setObjectName(u"chatSA")
        self.chatSA.setMinimumSize(QSize(40, 40))
        self.chatSA.setStyleSheet(u"QScrollArea {\n"
"border: none;\n"
"}")
        self.chatSA.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.chatSA.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.chatSA.setWidgetResizable(True)
        self.chatSAWC = QWidget()
        self.chatSAWC.setObjectName(u"chatSAWC")
        self.chatSAWC.setGeometry(QRect(0, 0, 987, 633))
        self.chatSAWCLayout = QVBoxLayout(self.chatSAWC)
        self.chatSAWCLayout.setSpacing(0)
        self.chatSAWCLayout.setObjectName(u"chatSAWCLayout")
        self.chatSAWCLayout.setContentsMargins(15, 25, 15, 25)
        self.chatBox = QFrame(self.chatSAWC)
        self.chatBox.setObjectName(u"chatBox")
        self.chatBox.setStyleSheet(u"")
        self.chatBox.setFrameShape(QFrame.StyledPanel)
        self.chatBox.setFrameShadow(QFrame.Raised)
        self.chatBoxLayout = QVBoxLayout(self.chatBox)
        self.chatBoxLayout.setSpacing(0)
        self.chatBoxLayout.setObjectName(u"chatBoxLayout")
        self.chatBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.testMessageFrame = QFrame(self.chatBox)
        self.testMessageFrame.setObjectName(u"testMessageFrame")
        self.testMessageFrame.setFrameShape(QFrame.StyledPanel)
        self.testMessageFrame.setFrameShadow(QFrame.Raised)
        self.testMessageFrameLayout = QVBoxLayout(self.testMessageFrame)
        self.testMessageFrameLayout.setSpacing(0)
        self.testMessageFrameLayout.setObjectName(u"testMessageFrameLayout")
        self.testMessageFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.testMessageFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2Layout = QHBoxLayout(self.frame_2)
        self.frame_2Layout.setSpacing(9)
        self.frame_2Layout.setObjectName(u"frame_2Layout")
        self.frame_2Layout.setContentsMargins(5, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setStyleSheet(u"border: none;\n"
"background: gray;\n"
"border-radius: 20px;")

        self.frame_2Layout.addWidget(self.label)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3Layout = QHBoxLayout(self.frame_3)
        self.frame_3Layout.setSpacing(5)
        self.frame_3Layout.setObjectName(u"frame_3Layout")
        self.frame_3Layout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"border:none")

        self.frame_3Layout.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"border: none")

        self.frame_3Layout.addWidget(self.label_3)


        self.frame_2Layout.addWidget(self.frame_3, 0, Qt.AlignLeft)


        self.testMessageFrameLayout.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.testMessageFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4Layout = QHBoxLayout(self.frame_4)
        self.frame_4Layout.setSpacing(7)
        self.frame_4Layout.setObjectName(u"frame_4Layout")
        self.frame_4Layout.setContentsMargins(8, 0, 0, -1)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"border: none;\n"
"margin-top: 3px")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6Layout = QVBoxLayout(self.frame_6)
        self.frame_6Layout.setSpacing(0)
        self.frame_6Layout.setObjectName(u"frame_6Layout")
        self.frame_6Layout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        font8 = QFont()
        font8.setFamilies([u"Righteous"])
        font8.setPointSize(8)
        self.label_4.setFont(font8)

        self.frame_6Layout.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font8)
        self.label_5.setStyleSheet(u"border: none")

        self.frame_6Layout.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font8)

        self.frame_6Layout.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")

        self.frame_6Layout.addWidget(self.label_7)


        self.frame_4Layout.addWidget(self.frame_6, 0, Qt.AlignLeft|Qt.AlignTop)

        self.plainTextEdit = QPlainTextEdit(self.frame_4)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(900, 87))
        self.plainTextEdit.setFont(font3)
        self.plainTextEdit.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	background-color: #27282D;;\n"
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
        self.plainTextEdit.setLineWidth(1)
        self.plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.plainTextEdit.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setOverwriteMode(False)
        self.plainTextEdit.setTabStopDistance(20.000000000000000)
        self.plainTextEdit.setCursorWidth(1)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setProperty("tabStopWidth", 20)

        self.frame_4Layout.addWidget(self.plainTextEdit, 0, Qt.AlignLeft|Qt.AlignTop)


        self.testMessageFrameLayout.addWidget(self.frame_4, 0, Qt.AlignLeft)


        self.chatBoxLayout.addWidget(self.testMessageFrame, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.chatSAWCLayout.addWidget(self.chatBox, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.chatSA.setWidget(self.chatSAWC)

        self.chatContainerLayout.addWidget(self.chatSA)

        self.chatInputContainer = QFrame(self.chatContainer)
        self.chatInputContainer.setObjectName(u"chatInputContainer")
        self.chatInputContainer.setMinimumSize(QSize(0, 0))
        self.chatInputContainer.setMaximumSize(QSize(16777215, 16777215))
        self.chatInputContainer.setStyleSheet(u"QFrame {\n"
"	padding: 0px 15px 10px 15px;\n"
"};")
        self.chatInputContainer.setFrameShape(QFrame.StyledPanel)
        self.chatInputContainer.setFrameShadow(QFrame.Raised)
        self.chatInputContainerLayout = QHBoxLayout(self.chatInputContainer)
        self.chatInputContainerLayout.setSpacing(0)
        self.chatInputContainerLayout.setObjectName(u"chatInputContainerLayout")
        self.chatInputContainerLayout.setContentsMargins(0, 0, 0, 0)
        self.chatInputBox = QFrame(self.chatInputContainer)
        self.chatInputBox.setObjectName(u"chatInputBox")
        self.chatInputBox.setMinimumSize(QSize(0, 35))
        self.chatInputBox.setMaximumSize(QSize(16777215, 35))
        self.chatInputBox.setStyleSheet(u"QFrame {\n"
"	margin: 0px;\n"
"	padding: 3px 7px 3px 7px;\n"
"	background-color: #A298AE;\n"
"	border-radius: 10px;\n"
"	border: 1px solid #420096;\n"
"}")
        self.chatInputBox.setFrameShape(QFrame.StyledPanel)
        self.chatInputBox.setFrameShadow(QFrame.Raised)
        self.chatInputBoxLayout = QHBoxLayout(self.chatInputBox)
        self.chatInputBoxLayout.setSpacing(0)
        self.chatInputBoxLayout.setObjectName(u"chatInputBoxLayout")
        self.chatInputBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.chatInput = QPlainTextEdit(self.chatInputBox)
        self.chatInput.setObjectName(u"chatInput")
        self.chatInput.setMinimumSize(QSize(0, 0))
        self.chatInput.setMaximumSize(QSize(16777215, 16777215))
        self.chatInput.setFont(font5)
        self.chatInput.setStyleSheet(u"QFrame {\n"
"	margin: 0px;\n"
"	padding: 0px;\n"
"}\n"
"\n"
"\n"
"QPlainTextEdit {\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	background: #A298AE;\n"
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
"}")
        self.chatInput.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.chatInput.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.chatInputBoxLayout.addWidget(self.chatInput)

        self.buttonBox = QFrame(self.chatInputBox)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStyleSheet(u"QFrame {\n"
"	background: transparent;\n"
"	margin: 0px;\n"
"	padding: 0px;\n"
"	border: none;	\n"
"}")
        self.buttonBox.setFrameShape(QFrame.StyledPanel)
        self.buttonBox.setFrameShadow(QFrame.Raised)
        self.buttonBoxLayout = QHBoxLayout(self.buttonBox)
        self.buttonBoxLayout.setSpacing(0)
        self.buttonBoxLayout.setObjectName(u"buttonBoxLayout")
        self.buttonBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.shareImageBtn = QPushButton(self.buttonBox)
        self.shareImageBtn.setObjectName(u"shareImageBtn")
        self.shareImageBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.shareImageBtn.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"	icon-size: 24px;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/Icons/Icons/panorama_FILL1_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.shareImageBtn.setIcon(icon10)

        self.buttonBoxLayout.addWidget(self.shareImageBtn, 0, Qt.AlignTop)


        self.chatInputBoxLayout.addWidget(self.buttonBox, 0, Qt.AlignLeft|Qt.AlignTop)


        self.chatInputContainerLayout.addWidget(self.chatInputBox)


        self.chatContainerLayout.addWidget(self.chatInputContainer, 0, Qt.AlignBottom)


        self.mainScreenLayout.addWidget(self.chatContainer)

        self.mainFrame = QFrame(self.mainScreen)
        self.mainFrame.setObjectName(u"mainFrame")
        sizePolicy3.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy3)
        self.mainFrame.setMinimumSize(QSize(0, 0))
        self.mainFrame.setMaximumSize(QSize(0, 16777215))
        self.mainFrame.setStyleSheet(u"QFrame {\n"
"	background-color: #27282D;\n"
"	padding-bottom: 28px;\n"
"}")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.mainFrameLayout = QVBoxLayout(self.mainFrame)
        self.mainFrameLayout.setSpacing(0)
        self.mainFrameLayout.setObjectName(u"mainFrameLayout")
        self.mainFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLabel = QLabel(self.mainFrame)
        self.mainLabel.setObjectName(u"mainLabel")
        font9 = QFont()
        font9.setFamilies([u"Righteous"])
        font9.setPointSize(48)
        self.mainLabel.setFont(font9)

        self.mainFrameLayout.addWidget(self.mainLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.mainScreenLayout.addWidget(self.mainFrame)

        self.chatSettingsContainer = QFrame(self.mainScreen)
        self.chatSettingsContainer.setObjectName(u"chatSettingsContainer")
        self.chatSettingsContainer.setEnabled(False)
        self.chatSettingsContainer.setMinimumSize(QSize(0, 0))
        self.chatSettingsContainer.setMaximumSize(QSize(0, 16777215))
        self.chatSettingsContainer.setFrameShape(QFrame.StyledPanel)
        self.chatSettingsContainer.setFrameShadow(QFrame.Raised)

        self.mainScreenLayout.addWidget(self.chatSettingsContainer)

        self.application.addWidget(self.mainScreen)
        self.settingsScreen = QWidget()
        self.settingsScreen.setObjectName(u"settingsScreen")
        self.settingsScreen.setStyleSheet(u"background: #1E1F23;")
        self.horizontalLayout = QHBoxLayout(self.settingsScreen)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.settingsMenuSA = QScrollArea(self.settingsScreen)
        self.settingsMenuSA.setObjectName(u"settingsMenuSA")
        self.settingsMenuSA.setMinimumSize(QSize(250, 0))
        self.settingsMenuSA.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}")
        self.settingsMenuSA.setWidgetResizable(True)
        self.settingsMenuSAWC = QWidget()
        self.settingsMenuSAWC.setObjectName(u"settingsMenuSAWC")
        self.settingsMenuSAWC.setGeometry(QRect(0, 0, 233, 189))
        self.verticalLayout_9 = QVBoxLayout(self.settingsMenuSAWC)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(15, 16, 15, 0)
        self.settingsMenuContainer = QFrame(self.settingsMenuSAWC)
        self.settingsMenuContainer.setObjectName(u"settingsMenuContainer")
        self.settingsMenuContainer.setFrameShape(QFrame.StyledPanel)
        self.settingsMenuContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.settingsMenuContainer)
        self.verticalLayout_10.setSpacing(12)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.myAccountBtn = QPushButton(self.settingsMenuContainer)
        self.myAccountBtn.setObjectName(u"myAccountBtn")
        self.myAccountBtn.setFont(font5)
        self.myAccountBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.myAccountBtn.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"	padding: 10px 0px 10px 15px;\n"
"	text-align: left;\n"
"	border-radius: 8px\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: #25262C;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none;\n"
"}")

        self.verticalLayout_10.addWidget(self.myAccountBtn)

        self.settingsMenuLine_1 = QFrame(self.settingsMenuContainer)
        self.settingsMenuLine_1.setObjectName(u"settingsMenuLine_1")
        self.settingsMenuLine_1.setFrameShape(QFrame.HLine)
        self.settingsMenuLine_1.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.settingsMenuLine_1)

        self.appearanceBtn = QPushButton(self.settingsMenuContainer)
        self.appearanceBtn.setObjectName(u"appearanceBtn")
        self.appearanceBtn.setFont(font5)
        self.appearanceBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.appearanceBtn.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"	padding: 10px 0px 10px 15px;\n"
"	text-align: left;\n"
"	border-radius: 8px\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: #25262C;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none;\n"
"}")

        self.verticalLayout_10.addWidget(self.appearanceBtn)

        self.settingsMenuLine_2 = QFrame(self.settingsMenuContainer)
        self.settingsMenuLine_2.setObjectName(u"settingsMenuLine_2")
        self.settingsMenuLine_2.setFrameShape(QFrame.HLine)
        self.settingsMenuLine_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.settingsMenuLine_2)

        self.logOutBtn = QPushButton(self.settingsMenuContainer)
        self.logOutBtn.setObjectName(u"logOutBtn")
        self.logOutBtn.setFont(font5)
        self.logOutBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.logOutBtn.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"	padding: 10px 0px 10px 15px;\n"
"	text-align: left;\n"
"	border-radius: 8px\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: #25262C;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/Icons/Icons/logout_FILL1_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logOutBtn.setIcon(icon11)

        self.verticalLayout_10.addWidget(self.logOutBtn)


        self.verticalLayout_9.addWidget(self.settingsMenuContainer, 0, Qt.AlignTop)

        self.settingsMenuSA.setWidget(self.settingsMenuSAWC)

        self.horizontalLayout.addWidget(self.settingsMenuSA, 0, Qt.AlignLeft)

        self.settingsContentsFrame = QFrame(self.settingsScreen)
        self.settingsContentsFrame.setObjectName(u"settingsContentsFrame")
        sizePolicy2.setHeightForWidth(self.settingsContentsFrame.sizePolicy().hasHeightForWidth())
        self.settingsContentsFrame.setSizePolicy(sizePolicy2)
        self.settingsContentsFrame.setStyleSheet(u"background: #232429;")
        self.settingsContentsFrame.setFrameShape(QFrame.StyledPanel)
        self.settingsContentsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.settingsContentsFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.settingsTitleAndButtonContainer = QFrame(self.settingsContentsFrame)
        self.settingsTitleAndButtonContainer.setObjectName(u"settingsTitleAndButtonContainer")
        self.settingsTitleAndButtonContainer.setFrameShape(QFrame.StyledPanel)
        self.settingsTitleAndButtonContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.settingsTitleAndButtonContainer)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(25, 17, 40, 10)
        self.settingsTitle = QLabel(self.settingsTitleAndButtonContainer)
        self.settingsTitle.setObjectName(u"settingsTitle")
        self.settingsTitle.setFont(font6)

        self.horizontalLayout_2.addWidget(self.settingsTitle, 0, Qt.AlignLeft)

        self.exitSettingsBtn = QPushButton(self.settingsTitleAndButtonContainer)
        self.exitSettingsBtn.setObjectName(u"exitSettingsBtn")
        self.exitSettingsBtn.setMinimumSize(QSize(32, 32))
        self.exitSettingsBtn.setMaximumSize(QSize(32, 32))
        self.exitSettingsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exitSettingsBtn.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"	icon-size: 22px;\n"
"	border: 2px solid #5d0cc4;\n"
"	border-radius: 16px;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none;\n"
"}")
        self.exitSettingsBtn.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.exitSettingsBtn, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.settingsTitleAndButtonContainer, 0, Qt.AlignTop)

        self.settingsContentsSA = QScrollArea(self.settingsContentsFrame)
        self.settingsContentsSA.setObjectName(u"settingsContentsSA")
        self.settingsContentsSA.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}")
        self.settingsContentsSA.setWidgetResizable(True)
        self.settingsContentsSAWC = QWidget()
        self.settingsContentsSAWC.setObjectName(u"settingsContentsSAWC")
        self.settingsContentsSAWC.setGeometry(QRect(0, 0, 423, 340))
        self.verticalLayout_3 = QVBoxLayout(self.settingsContentsSAWC)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.settingContentsFrame = QFrame(self.settingsContentsSAWC)
        self.settingContentsFrame.setObjectName(u"settingContentsFrame")
        self.settingContentsFrame.setFrameShape(QFrame.StyledPanel)
        self.settingContentsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.settingContentsFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsContents = QStackedWidget(self.settingContentsFrame)
        self.settingsContents.setObjectName(u"settingsContents")
        self.settingsContents.setStyleSheet(u"")
        self.profileSettings = QWidget()
        self.profileSettings.setObjectName(u"profileSettings")
        self.profileSettings.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.profileSettings)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(70, 50, 70, 0)
        self.profileSettingsContainer = QFrame(self.profileSettings)
        self.profileSettingsContainer.setObjectName(u"profileSettingsContainer")
        self.profileSettingsContainer.setMaximumSize(QSize(858, 288))
        self.profileSettingsContainer.setStyleSheet(u"QFrame {\n"
"	background: #1e1f23;\n"
"	border-radius: 10px\n"
"}")
        self.profileSettingsContainer.setFrameShape(QFrame.StyledPanel)
        self.profileSettingsContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.profileSettingsContainer)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(15, 15, 15, 15)
        self.userPhotoSettingsContainer = QFrame(self.profileSettingsContainer)
        self.userPhotoSettingsContainer.setObjectName(u"userPhotoSettingsContainer")
        self.userPhotoSettingsContainer.setFrameShape(QFrame.StyledPanel)
        self.userPhotoSettingsContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.userPhotoSettingsContainer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.userPhotoSettings = QFrame(self.userPhotoSettingsContainer)
        self.userPhotoSettings.setObjectName(u"userPhotoSettings")
        self.userPhotoSettings.setFrameShape(QFrame.StyledPanel)
        self.userPhotoSettings.setFrameShadow(QFrame.Raised)
        self.userPhotoSettingsLayout = QHBoxLayout(self.userPhotoSettings)
        self.userPhotoSettingsLayout.setSpacing(10)
        self.userPhotoSettingsLayout.setObjectName(u"userPhotoSettingsLayout")
        self.userPhotoSettingsLayout.setContentsMargins(0, 0, 0, 0)
        self.userPhotoSettingsLabel = QLabel(self.userPhotoSettings)
        self.userPhotoSettingsLabel.setObjectName(u"userPhotoSettingsLabel")
        self.userPhotoSettingsLabel.setMinimumSize(QSize(60, 60))
        self.userPhotoSettingsLabel.setMaximumSize(QSize(60, 60))
        self.userPhotoSettingsLabel.setStyleSheet(u"background: gray;\n"
"border-radius: 30px;")

        self.userPhotoSettingsLayout.addWidget(self.userPhotoSettingsLabel)

        self.userNameSettingsLabel = QLabel(self.userPhotoSettings)
        self.userNameSettingsLabel.setObjectName(u"userNameSettingsLabel")
        self.userNameSettingsLabel.setFont(font6)

        self.userPhotoSettingsLayout.addWidget(self.userNameSettingsLabel)


        self.horizontalLayout_4.addWidget(self.userPhotoSettings, 0, Qt.AlignLeft)

        self.changePhotoSettingsBtn = QPushButton(self.userPhotoSettingsContainer)
        self.changePhotoSettingsBtn.setObjectName(u"changePhotoSettingsBtn")
        self.changePhotoSettingsBtn.setFont(font3)
        self.changePhotoSettingsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.changePhotoSettingsBtn.setStyleSheet(u"QPushButton {\n"
"	background: #420096;\n"
"	color: white;\n"
"	padding: 5px 10px 5px 10px;\n"
"	border: 2px solid #420096;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: #4B00AB;\n"
"	border: 2px solid #4B00AB;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none;\n"
"}")

        self.horizontalLayout_4.addWidget(self.changePhotoSettingsBtn, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.userPhotoSettingsContainer)

        self.userSettingsContainer = QFrame(self.profileSettingsContainer)
        self.userSettingsContainer.setObjectName(u"userSettingsContainer")
        self.userSettingsContainer.setStyleSheet(u"QFrame {\n"
"	background: #28292F;\n"
"	border-radius: 10px\n"
"}")
        self.userSettingsContainer.setFrameShape(QFrame.StyledPanel)
        self.userSettingsContainer.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_8 = QVBoxLayout(self.userSettingsContainer)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(15, 15, 15, 15)
        self.usernameSettingsContainer = QFrame(self.userSettingsContainer)
        self.usernameSettingsContainer.setObjectName(u"usernameSettingsContainer")
        self.usernameSettingsContainer.setStyleSheet(u"")
        self.usernameSettingsContainer.setFrameShape(QFrame.StyledPanel)
        self.usernameSettingsContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.usernameSettingsContainer)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.usernameSettings = QFrame(self.usernameSettingsContainer)
        self.usernameSettings.setObjectName(u"usernameSettings")
        self.usernameSettings.setFrameShape(QFrame.StyledPanel)
        self.usernameSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.usernameSettings)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.settingsUsernameLabel = QLabel(self.usernameSettings)
        self.settingsUsernameLabel.setObjectName(u"settingsUsernameLabel")
        self.settingsUsernameLabel.setFont(font5)

        self.verticalLayout_5.addWidget(self.settingsUsernameLabel)

        self.usernameSettingsLabel = QLabel(self.usernameSettings)
        self.usernameSettingsLabel.setObjectName(u"usernameSettingsLabel")
        self.usernameSettingsLabel.setFont(font5)

        self.verticalLayout_5.addWidget(self.usernameSettingsLabel)


        self.horizontalLayout_5.addWidget(self.usernameSettings, 0, Qt.AlignLeft)

        self.usernameSettingsEditBtn = QPushButton(self.usernameSettingsContainer)
        self.usernameSettingsEditBtn.setObjectName(u"usernameSettingsEditBtn")
        self.usernameSettingsEditBtn.setFont(font3)
        self.usernameSettingsEditBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.usernameSettingsEditBtn.setStyleSheet(u"QPushButton {\n"
"	background: #3C3C3C;\n"
"	color: white;\n"
"	padding: 5px 10px 5px 10px;\n"
"	border: 2px solid #3C3C3C;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: #535353;\n"
"	border: 2px solid #535353;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none;\n"
"}")

        self.horizontalLayout_5.addWidget(self.usernameSettingsEditBtn, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.usernameSettingsContainer)

        self.emailSettingsContainer = QFrame(self.userSettingsContainer)
        self.emailSettingsContainer.setObjectName(u"emailSettingsContainer")
        self.emailSettingsContainer.setFrameShape(QFrame.StyledPanel)
        self.emailSettingsContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.emailSettingsContainer)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.emailSettings = QFrame(self.emailSettingsContainer)
        self.emailSettings.setObjectName(u"emailSettings")
        self.emailSettings.setFrameShape(QFrame.StyledPanel)
        self.emailSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.emailSettings)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.settingsEmailLabel = QLabel(self.emailSettings)
        self.settingsEmailLabel.setObjectName(u"settingsEmailLabel")
        self.settingsEmailLabel.setFont(font5)

        self.verticalLayout_6.addWidget(self.settingsEmailLabel)

        self.emailSettingsLabel = QLabel(self.emailSettings)
        self.emailSettingsLabel.setObjectName(u"emailSettingsLabel")
        self.emailSettingsLabel.setFont(font5)

        self.verticalLayout_6.addWidget(self.emailSettingsLabel)


        self.horizontalLayout_6.addWidget(self.emailSettings, 0, Qt.AlignLeft)

        self.emailSettingsEditBtn = QPushButton(self.emailSettingsContainer)
        self.emailSettingsEditBtn.setObjectName(u"emailSettingsEditBtn")
        self.emailSettingsEditBtn.setFont(font3)
        self.emailSettingsEditBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.emailSettingsEditBtn.setStyleSheet(u"QPushButton {\n"
"	background: #3C3C3C;\n"
"	color: white;\n"
"	padding: 5px 10px 5px 10px;\n"
"	border: 2px solid #3C3C3C;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: #535353;\n"
"	border: 2px solid #535353;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none;\n"
"}")

        self.horizontalLayout_6.addWidget(self.emailSettingsEditBtn, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.emailSettingsContainer)


        self.verticalLayout_7.addWidget(self.userSettingsContainer)

        self.passwordAndAccountSettingsContainer = QFrame(self.profileSettingsContainer)
        self.passwordAndAccountSettingsContainer.setObjectName(u"passwordAndAccountSettingsContainer")
        self.passwordAndAccountSettingsContainer.setFrameShape(QFrame.StyledPanel)
        self.passwordAndAccountSettingsContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.passwordAndAccountSettingsContainer)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 10, 0, 0)
        self.deleteAccountSettingsBtn = QPushButton(self.passwordAndAccountSettingsContainer)
        self.deleteAccountSettingsBtn.setObjectName(u"deleteAccountSettingsBtn")
        self.deleteAccountSettingsBtn.setFont(font3)
        self.deleteAccountSettingsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteAccountSettingsBtn.setStyleSheet(u"QPushButton {\n"
"	background: #25262C;\n"
"	color: white;\n"
"	padding: 5px 10px 5px 10px;\n"
"	border: 2px solid #BA2E2E;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: #BA2E2E;\n"
"	border: 2px solid #BA2E2E;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none;\n"
"}")

        self.horizontalLayout_7.addWidget(self.deleteAccountSettingsBtn, 0, Qt.AlignLeft)

        self.changePasswordSettingsBtn = QPushButton(self.passwordAndAccountSettingsContainer)
        self.changePasswordSettingsBtn.setObjectName(u"changePasswordSettingsBtn")
        self.changePasswordSettingsBtn.setFont(font3)
        self.changePasswordSettingsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.changePasswordSettingsBtn.setStyleSheet(u"QPushButton {\n"
"	background: #420096;\n"
"	color: white;\n"
"	padding: 5px 10px 5px 10px;\n"
"	border: 2px solid #420096;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background: #4B00AB;\n"
"	border: 2px solid #4B00AB;\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"	outline: none;\n"
"}")

        self.horizontalLayout_7.addWidget(self.changePasswordSettingsBtn, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.passwordAndAccountSettingsContainer)


        self.verticalLayout_4.addWidget(self.profileSettingsContainer, 0, Qt.AlignTop)

        self.settingsContents.addWidget(self.profileSettings)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.settingsContents.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.settingsContents)


        self.verticalLayout_3.addWidget(self.settingContentsFrame)

        self.settingsContentsSA.setWidget(self.settingsContentsSAWC)

        self.verticalLayout.addWidget(self.settingsContentsSA)


        self.horizontalLayout.addWidget(self.settingsContentsFrame)

        self.application.addWidget(self.settingsScreen)

        self.centralWidgetLayout.addWidget(self.application)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)

        self.application.setCurrentIndex(3)
        self.monthCB.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.appName.setText(QCoreApplication.translate("MainWindow", u"ChatApp", None))
        self.appMinimize.setText("")
        self.appFullscreenToggle.setText("")
        self.appExit.setText("")
        self.emailLabel.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.emailInput.setText("")
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.passwordInput.setText("")
        self.forgotYourPasswordBtn.setText(QCoreApplication.translate("MainWindow", u"Forgot your password?", None))
        self.loginCredentialsStatusLabel.setText(QCoreApplication.translate("MainWindow", u"Email or password is invalid", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.needAnAccountlabel.setText(QCoreApplication.translate("MainWindow", u"Need an account?", None))
        self.toRegisterScreenBtn.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.loadingLabel.setText("")
        self.emailLabelR.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.emailStatusLabel.setText("")
        self.emailInputR.setText("")
        self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.usernameStatusLabel.setText("")
        self.passwordLabelR.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.passwordStatus.setText("")
        self.confirmPasswordLabel.setText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.confirmPasswordStatusLabel.setText("")
        self.dateOfBirthLabel.setText(QCoreApplication.translate("MainWindow", u"Date Of Birth", None))
        self.monthCB.setItemText(0, QCoreApplication.translate("MainWindow", u"December", None))
        self.monthCB.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.monthCB.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.monthCB.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.monthCB.setItemText(4, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.monthCB.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.dayCB.setItemText(0, QCoreApplication.translate("MainWindow", u"July", None))

        self.yearCB.setItemText(0, QCoreApplication.translate("MainWindow", u"2022", None))
        self.yearCB.setItemText(1, QCoreApplication.translate("MainWindow", u"2021", None))
        self.yearCB.setItemText(2, QCoreApplication.translate("MainWindow", u"2020", None))
        self.yearCB.setItemText(3, QCoreApplication.translate("MainWindow", u"2019", None))

        self.registerBtn.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.ahaaLabel.setText(QCoreApplication.translate("MainWindow", u"Already have an account?", None))
        self.signInBtn.setText(QCoreApplication.translate("MainWindow", u"Sign In", None))
        self.userPhotoLMLabel.setText("")
        self.userNameLMLabel.setText(QCoreApplication.translate("MainWindow", u"Crasx", None))
        self.friendsLMBtn.setText("")
        self.userPhotoLabelRC.setText("")
        self.userNameLabelRC.setText(QCoreApplication.translate("MainWindow", u"Crasx", None))
        self.closeChatBtn.setText("")
        self.testMessageBtn.setText(QCoreApplication.translate("MainWindow", u"Test Message", None))
        self.testChatBtn.setText(QCoreApplication.translate("MainWindow", u"Test Chat", None))
        self.settingsLMBtn.setText("")
        self.friendsLabel.setText(QCoreApplication.translate("MainWindow", u"Friends", None))
        self.searchInput.setText("")
        self.pushButton_3.setText("")
        self.friendsPageBtn.setText("")
        self.addFriendsPageBtn.setText("")
        self.friendRequestPageBtn.setText("")
        self.blockListPageBtn.setText("")
        self.userChatPhotoLabel.setText("")
        self.chatUserNameLabel.setText(QCoreApplication.translate("MainWindow", u"Crasx", None))
        self.chatUserStatusLabel.setText(QCoreApplication.translate("MainWindow", u"online", None))
        self.chatSettingsBtn.setText("")
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Crasx", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"10/10/2021", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"10:24", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"10:24", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"10:24", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"10:24", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"Hello Hello Hello Hello Hello Hello Hello  Hello  Hello  Hello  Hello Hello Hello Hello Hello Hello Hello Hello  Hello  Hello  Hello  HelloHello Hello Hello Hello Hello Hello Hello  Hello  Hello  Hello  HelloHello Hello Hello Hello Hello Hello Hello  Hello  Hello  Hello  HelloHello Hello Hello Hello Hello Hello Hello  Hello  Hello  Hello  HelloHello Hello Hello Hello Hello Hello Hello  Hello  Hello  Hello  HelloHello Hello Hello Hello Hello Hello Hello  Hello  Hello  Hello  HelloHello Hello Hello Hello Hello Hello Hello  Hello  Hello  Hello  HelloHello Hello Hello Hello Hello Hello Hello  Hello  Hello  Hello  Hello\n"
"Maaaaan!", None))
        self.chatInput.setPlainText("")
        self.shareImageBtn.setText("")
        self.mainLabel.setText(QCoreApplication.translate("MainWindow", u"ChatApp", None))
        self.myAccountBtn.setText(QCoreApplication.translate("MainWindow", u"My Account", None))
        self.appearanceBtn.setText(QCoreApplication.translate("MainWindow", u"Appearance", None))
        self.logOutBtn.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.settingsTitle.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.exitSettingsBtn.setText("")
        self.userPhotoSettingsLabel.setText("")
        self.userNameSettingsLabel.setText(QCoreApplication.translate("MainWindow", u"Crasx", None))
        self.changePhotoSettingsBtn.setText(QCoreApplication.translate("MainWindow", u"Change Photo", None))
        self.settingsUsernameLabel.setText(QCoreApplication.translate("MainWindow", u"USERNAME", None))
        self.usernameSettingsLabel.setText(QCoreApplication.translate("MainWindow", u"Crasx", None))
        self.usernameSettingsEditBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.settingsEmailLabel.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None))
        self.emailSettingsLabel.setText(QCoreApplication.translate("MainWindow", u"myemail.com", None))
        self.emailSettingsEditBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.deleteAccountSettingsBtn.setText(QCoreApplication.translate("MainWindow", u"Delete Account", None))
        self.changePasswordSettingsBtn.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
    # retranslateUi

