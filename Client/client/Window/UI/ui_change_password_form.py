# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_password.ui'
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

class Ui_ChangePasswordForm(object):
    def setupUi(self, ChangePasswordForm):
        if not ChangePasswordForm.objectName():
            ChangePasswordForm.setObjectName(u"ChangePasswordForm")
        ChangePasswordForm.resize(652, 376)
        ChangePasswordForm.setStyleSheet(u"background: #2f3137")
        self.passwordChangeContainer = QFrame(ChangePasswordForm)
        self.passwordChangeContainer.setObjectName(u"passwordChangeContainer")
        self.passwordChangeContainer.setGeometry(QRect(110, 30, 391, 251))
        self.passwordChangeContainer.setMinimumSize(QSize(391, 251))
        self.passwordChangeContainer.setStyleSheet(u"QFrame {\n"
"	background: #27282D;\n"
"	padding-bottom: 5px;\n"
"	border: 2px solid transparent;\n"
"	border-radius: 10px;\n"
"}")
        self.passwordChangeContainer.setFrameShape(QFrame.StyledPanel)
        self.passwordChangeContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.passwordChangeContainer)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 5, 10, 8)
        self.currentPasswordContainer = QFrame(self.passwordChangeContainer)
        self.currentPasswordContainer.setObjectName(u"currentPasswordContainer")
        self.currentPasswordContainer.setStyleSheet(u"QFrame {\n"
"	margin-top: 3px;\n"
"	padding: 0px;\n"
"	border: none;\n"
"}")
        self.currentPasswordContainer.setFrameShape(QFrame.StyledPanel)
        self.currentPasswordContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.currentPasswordContainer)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.currentPasswordLabelContainer = QFrame(self.currentPasswordContainer)
        self.currentPasswordLabelContainer.setObjectName(u"currentPasswordLabelContainer")
        self.currentPasswordLabelContainer.setStyleSheet(u"padding: 0px;")
        self.currentPasswordLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.currentPasswordLabelContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.currentPasswordLabelContainer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.currentPasswordLabel = QLabel(self.currentPasswordLabelContainer)
        self.currentPasswordLabel.setObjectName(u"currentPasswordLabel")
        font = QFont()
        font.setFamilies([u"Righteous"])
        font.setPointSize(12)
        self.currentPasswordLabel.setFont(font)
        self.currentPasswordLabel.setStyleSheet(u"padding: 0px;\n"
"padding-left: 5px;\n"
"color: #63646B;")

        self.horizontalLayout.addWidget(self.currentPasswordLabel, 0, Qt.AlignRight)

        self.currentPasswordStatusLabel = QLabel(self.currentPasswordLabelContainer)
        self.currentPasswordStatusLabel.setObjectName(u"currentPasswordStatusLabel")
        font1 = QFont()
        font1.setFamilies([u"Righteous"])
        font1.setPointSize(10)
        self.currentPasswordStatusLabel.setFont(font1)
        self.currentPasswordStatusLabel.setStyleSheet(u"font-size: 10;\n"
"color: #B12323")

        self.horizontalLayout.addWidget(self.currentPasswordStatusLabel, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.currentPasswordLabelContainer, 0, Qt.AlignLeft)

        self.currentPasswordInput = QLineEdit(self.currentPasswordContainer)
        self.currentPasswordInput.setObjectName(u"currentPasswordInput")
        font2 = QFont()
        font2.setFamilies([u"Righteous"])
        self.currentPasswordInput.setFont(font2)
        self.currentPasswordInput.setStyleSheet(u"QLineEdit {\n"
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
        self.currentPasswordInput.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.currentPasswordInput)


        self.verticalLayout_4.addWidget(self.currentPasswordContainer)

        self.newPasswordContainer = QFrame(self.passwordChangeContainer)
        self.newPasswordContainer.setObjectName(u"newPasswordContainer")
        self.newPasswordContainer.setStyleSheet(u"QFrame {\n"
"	margin-top: 3px;\n"
"	padding: 0px;\n"
"	border: none;\n"
"}")
        self.newPasswordContainer.setFrameShape(QFrame.StyledPanel)
        self.newPasswordContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.newPasswordContainer)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.newPasswordLabelContainer = QFrame(self.newPasswordContainer)
        self.newPasswordLabelContainer.setObjectName(u"newPasswordLabelContainer")
        self.newPasswordLabelContainer.setStyleSheet(u"padding: 0px;")
        self.newPasswordLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.newPasswordLabelContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.newPasswordLabelContainer)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.newPasswordLabel = QLabel(self.newPasswordLabelContainer)
        self.newPasswordLabel.setObjectName(u"newPasswordLabel")
        self.newPasswordLabel.setFont(font)
        self.newPasswordLabel.setStyleSheet(u"padding-left: 5px;\n"
"color: #63646B;")

        self.horizontalLayout_2.addWidget(self.newPasswordLabel, 0, Qt.AlignRight)

        self.newPasswordStatusLabel = QLabel(self.newPasswordLabelContainer)
        self.newPasswordStatusLabel.setObjectName(u"newPasswordStatusLabel")
        self.newPasswordStatusLabel.setFont(font1)
        self.newPasswordStatusLabel.setStyleSheet(u"font-size: 10;\n"
"color: #B12323")

        self.horizontalLayout_2.addWidget(self.newPasswordStatusLabel, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.newPasswordLabelContainer, 0, Qt.AlignLeft)

        self.newPasswordInput = QLineEdit(self.newPasswordContainer)
        self.newPasswordInput.setObjectName(u"newPasswordInput")
        self.newPasswordInput.setFont(font2)
        self.newPasswordInput.setStyleSheet(u"QLineEdit {\n"
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
        self.newPasswordInput.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.newPasswordInput)


        self.verticalLayout_4.addWidget(self.newPasswordContainer)

        self.confirmPasswordContainer = QFrame(self.passwordChangeContainer)
        self.confirmPasswordContainer.setObjectName(u"confirmPasswordContainer")
        self.confirmPasswordContainer.setStyleSheet(u"QFrame {\n"
"	margin-top: 3px;\n"
"	padding: 0px;\n"
"	border: none;\n"
"}")
        self.confirmPasswordContainer.setFrameShape(QFrame.StyledPanel)
        self.confirmPasswordContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.confirmPasswordContainer)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.confirmPasswordLabelContainer = QFrame(self.confirmPasswordContainer)
        self.confirmPasswordLabelContainer.setObjectName(u"confirmPasswordLabelContainer")
        self.confirmPasswordLabelContainer.setStyleSheet(u"padding: 0px;")
        self.confirmPasswordLabelContainer.setFrameShape(QFrame.StyledPanel)
        self.confirmPasswordLabelContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.confirmPasswordLabelContainer)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.confirmPasswordLabel = QLabel(self.confirmPasswordLabelContainer)
        self.confirmPasswordLabel.setObjectName(u"confirmPasswordLabel")
        self.confirmPasswordLabel.setFont(font)
        self.confirmPasswordLabel.setStyleSheet(u"padding-left: 5px;\n"
"color: #63646B;")

        self.horizontalLayout_3.addWidget(self.confirmPasswordLabel, 0, Qt.AlignRight)

        self.confirmPasswordStatusLabel = QLabel(self.confirmPasswordLabelContainer)
        self.confirmPasswordStatusLabel.setObjectName(u"confirmPasswordStatusLabel")
        self.confirmPasswordStatusLabel.setFont(font1)
        self.confirmPasswordStatusLabel.setStyleSheet(u"font-size: 10;\n"
"color: #B12323")

        self.horizontalLayout_3.addWidget(self.confirmPasswordStatusLabel, 0, Qt.AlignLeft)


        self.verticalLayout_3.addWidget(self.confirmPasswordLabelContainer, 0, Qt.AlignLeft)

        self.confirmPasswordInput = QLineEdit(self.confirmPasswordContainer)
        self.confirmPasswordInput.setObjectName(u"confirmPasswordInput")
        self.confirmPasswordInput.setFont(font2)
        self.confirmPasswordInput.setStyleSheet(u"QLineEdit {\n"
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
        self.confirmPasswordInput.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.confirmPasswordInput)


        self.verticalLayout_4.addWidget(self.confirmPasswordContainer)

        self.buttonsContainer = QFrame(self.passwordChangeContainer)
        self.buttonsContainer.setObjectName(u"buttonsContainer")
        self.buttonsContainer.setStyleSheet(u"padding: 0px 3px 0px 0px;\n"
"border: none;")
        self.buttonsContainer.setFrameShape(QFrame.StyledPanel)
        self.buttonsContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.buttonsContainer)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, -1, 0)
        self.cancelBtn = QPushButton(self.buttonsContainer)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setFont(font1)
        self.cancelBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelBtn.setStyleSheet(u"QPushButton {\n"
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


        self.verticalLayout_4.addWidget(self.buttonsContainer, 0, Qt.AlignRight|Qt.AlignBottom)


        self.retranslateUi(ChangePasswordForm)

        QMetaObject.connectSlotsByName(ChangePasswordForm)
    # setupUi

    def retranslateUi(self, ChangePasswordForm):
        ChangePasswordForm.setWindowTitle(QCoreApplication.translate("ChangePasswordForm", u"Form", None))
        self.currentPasswordLabel.setText(QCoreApplication.translate("ChangePasswordForm", u"Current Password", None))
        self.currentPasswordStatusLabel.setText("")
        self.newPasswordLabel.setText(QCoreApplication.translate("ChangePasswordForm", u"New Password", None))
        self.newPasswordStatusLabel.setText("")
        self.confirmPasswordLabel.setText(QCoreApplication.translate("ChangePasswordForm", u"Confirm Password", None))
        self.confirmPasswordStatusLabel.setText("")
        self.cancelBtn.setText(QCoreApplication.translate("ChangePasswordForm", u"Cancel", None))
        self.confirmBtn.setText(QCoreApplication.translate("ChangePasswordForm", u"Confirm", None))
    # retranslateUi

