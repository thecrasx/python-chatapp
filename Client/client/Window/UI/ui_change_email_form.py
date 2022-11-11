# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_email.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ChangeEmailForm(object):
    def setupUi(self, ChangeEmailForm):
        if not ChangeEmailForm.objectName():
            ChangeEmailForm.setObjectName(u"ChangeEmailForm")
        ChangeEmailForm.resize(473, 339)
        ChangeEmailForm.setStyleSheet(u"background: #2f3137")
        self.emailChangeContainer = QFrame(ChangeEmailForm)
        self.emailChangeContainer.setObjectName(u"emailChangeContainer")
        self.emailChangeContainer.setGeometry(QRect(60, 110, 371, 191))
        self.emailChangeContainer.setMinimumSize(QSize(371, 191))
        self.emailChangeContainer.setStyleSheet(u"QFrame {\n"
"	background: #27282D;\n"
"	padding-bottom: 5px;\n"
"	border: 2px solid transparent;\n"
"	border-radius: 10px;\n"
"}")
        self.emailChangeContainer.setFrameShape(QFrame.StyledPanel)
        self.emailChangeContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.emailChangeContainer)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 5, 10, 8)
        self.newEmailContainer = QFrame(self.emailChangeContainer)
        self.newEmailContainer.setObjectName(u"newEmailContainer")
        self.newEmailContainer.setStyleSheet(u"QFrame {\n"
"	margin-top: 3px;\n"
"	padding: 0px;\n"
"	border: none;\n"
"}")
        self.newEmailContainer.setFrameShape(QFrame.StyledPanel)
        self.newEmailContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.newEmailContainer)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.newEmailLabelContainer = QFrame(self.newEmailContainer)
        self.newEmailLabelContainer.setObjectName(u"newEmailLabelContainer")
        self.newEmailLabelContainer.setStyleSheet(u"")
        self.newEmailLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.newEmailLabelContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.newEmailLabelContainer)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.newEmailLabel = QLabel(self.newEmailLabelContainer)
        self.newEmailLabel.setObjectName(u"newEmailLabel")
        font = QFont()
        font.setFamilies([u"Righteous"])
        font.setPointSize(12)
        self.newEmailLabel.setFont(font)
        self.newEmailLabel.setStyleSheet(u"padding-left: 5px;\n"
"color: #63646B;")

        self.horizontalLayout.addWidget(self.newEmailLabel, 0, Qt.AlignRight)

        self.newEmailStatusLabel = QLabel(self.newEmailLabelContainer)
        self.newEmailStatusLabel.setObjectName(u"newEmailStatusLabel")
        font1 = QFont()
        font1.setFamilies([u"Righteous"])
        font1.setPointSize(10)
        self.newEmailStatusLabel.setFont(font1)
        self.newEmailStatusLabel.setStyleSheet(u"font-size: 10;\n"
"color: #B12323")

        self.horizontalLayout.addWidget(self.newEmailStatusLabel, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.newEmailLabelContainer, 0, Qt.AlignLeft)

        self.newEmailInput = QLineEdit(self.newEmailContainer)
        self.newEmailInput.setObjectName(u"newEmailInput")
        font2 = QFont()
        font2.setFamilies([u"Righteous"])
        self.newEmailInput.setFont(font2)
        self.newEmailInput.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout.addWidget(self.newEmailInput)


        self.verticalLayout_3.addWidget(self.newEmailContainer, 0, Qt.AlignTop)

        self.passwordContainer = QFrame(self.emailChangeContainer)
        self.passwordContainer.setObjectName(u"passwordContainer")
        self.passwordContainer.setStyleSheet(u"QFrame {\n"
"	margin-top: 3px;\n"
"	padding: 0px;\n"
"	border: none;\n"
"}")
        self.passwordContainer.setFrameShape(QFrame.StyledPanel)
        self.passwordContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.passwordContainer)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.passwordLabelContainer = QFrame(self.passwordContainer)
        self.passwordLabelContainer.setObjectName(u"passwordLabelContainer")
        self.passwordLabelContainer.setStyleSheet(u"padding: 0px;")
        self.passwordLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.passwordLabelContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.passwordLabelContainer)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.passwordLabel = QLabel(self.passwordLabelContainer)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setFont(font)
        self.passwordLabel.setStyleSheet(u"padding-left: 5px;\n"
"color: #63646B;")

        self.horizontalLayout_2.addWidget(self.passwordLabel, 0, Qt.AlignRight)

        self.passwordStatusLabel = QLabel(self.passwordLabelContainer)
        self.passwordStatusLabel.setObjectName(u"passwordStatusLabel")
        self.passwordStatusLabel.setFont(font1)
        self.passwordStatusLabel.setStyleSheet(u"font-size: 10;\n"
"color: #B12323")

        self.horizontalLayout_2.addWidget(self.passwordStatusLabel, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.passwordLabelContainer, 0, Qt.AlignLeft)

        self.passwordInput = QLineEdit(self.passwordContainer)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setFont(font2)
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
        self.passwordInput.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.passwordInput, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.passwordContainer, 0, Qt.AlignBottom)

        self.buttonsContainer = QFrame(self.emailChangeContainer)
        self.buttonsContainer.setObjectName(u"buttonsContainer")
        self.buttonsContainer.setStyleSheet(u"padding: 0px 3px 0px 0px;\n"
"border: none;")
        self.buttonsContainer.setFrameShape(QFrame.StyledPanel)
        self.buttonsContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.buttonsContainer)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.cancelBtn = QPushButton(self.buttonsContainer)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setFont(font1)
        self.cancelBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelBtn.setStyleSheet(u"QPushButton {\n"
"	background: #420096;\n"
"	border-radius : 12px;\n"
"	border : 2px solid transparent;\n"
"	padding: 5px 12px 5px 12px;\n"
"	color: white\n"
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

        self.horizontalLayout_4.addWidget(self.cancelBtn)

        self.confirmBtn = QPushButton(self.buttonsContainer)
        self.confirmBtn.setObjectName(u"confirmBtn")
        self.confirmBtn.setFont(font1)
        self.confirmBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.confirmBtn.setStyleSheet(u"QPushButton {\n"
"	background: #420096;\n"
"	border-radius : 12px;\n"
"	border : 2px solid transparent;\n"
"	padding: 5px 10px 5px 10px;\n"
"	color: white\n"
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

        self.horizontalLayout_4.addWidget(self.confirmBtn)


        self.verticalLayout_3.addWidget(self.buttonsContainer, 0, Qt.AlignRight|Qt.AlignBottom)


        self.retranslateUi(ChangeEmailForm)

        QMetaObject.connectSlotsByName(ChangeEmailForm)
    # setupUi

    def retranslateUi(self, ChangeEmailForm):
        ChangeEmailForm.setWindowTitle(QCoreApplication.translate("ChangeEmailForm", u"Form", None))
        self.newEmailLabel.setText(QCoreApplication.translate("ChangeEmailForm", u"New Email", None))
        self.newEmailStatusLabel.setText("")
        self.passwordLabel.setText(QCoreApplication.translate("ChangeEmailForm", u"Password", None))
        self.passwordStatusLabel.setText("")
        self.cancelBtn.setText(QCoreApplication.translate("ChangeEmailForm", u"Cancel", None))
        self.confirmBtn.setText(QCoreApplication.translate("ChangeEmailForm", u"Confirm", None))
    # retranslateUi

