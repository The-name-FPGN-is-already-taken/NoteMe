# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nota.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_loginWindowDialog(object):
    def setupUi(self, loginWindowDialog):
        if not loginWindowDialog.objectName():
            loginWindowDialog.setObjectName(u"loginWindowDialog")
        loginWindowDialog.resize(1024, 640)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginWindowDialog.sizePolicy().hasHeightForWidth())
        loginWindowDialog.setSizePolicy(sizePolicy)
        loginWindowDialog.setMinimumSize(QSize(1024, 640))
        loginWindowDialog.setMaximumSize(QSize(1920, 1080))
        self.centralwidget = QWidget(loginWindowDialog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setGeometry(QRect(0, 0, 1031, 641))
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftLayout = QFrame(self.frame)
        self.leftLayout.setObjectName(u"leftLayout")
        sizePolicy1.setHeightForWidth(self.leftLayout.sizePolicy().hasHeightForWidth())
        self.leftLayout.setSizePolicy(sizePolicy1)
        self.leftLayout.setMinimumSize(QSize(320, 0))
        self.leftLayout.setMaximumSize(QSize(320, 16777215))
        self.leftLayout.setStyleSheet(u"background-color: rgb(130, 164, 118);")
        self.leftLayout.setFrameShape(QFrame.StyledPanel)
        self.leftLayout.setFrameShadow(QFrame.Raised)
        self.leftLayout.setLineWidth(0)
        self.frame_2 = QFrame(self.leftLayout)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(40, 0, 241, 251))
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMinimumSize(QSize(200, 200))
        self.frame_2.setStyleSheet(u"image: url(D:/NotaProject/pics/notaKung.png);\n"
"border: none;\n"
"padding-right: 30px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.busyText = QLabel(self.leftLayout)
        self.busyText.setObjectName(u"busyText")
        self.busyText.setGeometry(QRect(10, 500, 271, 101))
        sizePolicy2.setHeightForWidth(self.busyText.sizePolicy().hasHeightForWidth())
        self.busyText.setSizePolicy(sizePolicy2)
        self.busyText.setMaximumSize(QSize(700, 16777215))
        font = QFont()
        font.setFamily(u"Telugu MN")
        font.setPointSize(16)
        self.busyText.setFont(font)
        self.busyText.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 35px;\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.leftLayout)

        self.rightLayout = QFrame(self.frame)
        self.rightLayout.setObjectName(u"rightLayout")
        self.rightLayout.setFocusPolicy(Qt.StrongFocus)
        self.rightLayout.setStyleSheet(u"background-color: rgb(255, 255, 244);")
        self.rightLayout.setFrameShape(QFrame.StyledPanel)
        self.rightLayout.setFrameShadow(QFrame.Raised)
        self.rightLayout.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.rightLayout)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 0, 15, 0)
        self.verticalFrame = QFrame(self.rightLayout)
        self.verticalFrame.setObjectName(u"verticalFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy3)
        self.verticalFrame.setMaximumSize(QSize(16777215, 140))
        self.verticalFrame.setStyleSheet(u"")
        self.verticalFrame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.nota = QLabel(self.verticalFrame)
        self.nota.setObjectName(u"nota")
        self.nota.setMaximumSize(QSize(16777215, 100))
        font1 = QFont()
        font1.setFamily(u"Telugu MN")
        font1.setPointSize(75)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(50)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.nota.setFont(font1)
        self.nota.setStyleSheet(u"color: rgb(123, 160, 108);\n"
"padding-left: 5px;")
        self.nota.setFrameShape(QFrame.NoFrame)
        self.nota.setTextFormat(Qt.AutoText)
        self.nota.setScaledContents(False)
        self.nota.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.nota.setWordWrap(False)

        self.verticalLayout_5.addWidget(self.nota)

        self.powerful = QLabel(self.verticalFrame)
        self.powerful.setObjectName(u"powerful")
        self.powerful.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamily(u"AvenirNext LT Pro Regular")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(50)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.powerful.setFont(font2)
        self.powerful.setStyleSheet(u"color: rgb(97, 97, 97);\n"
"padding-top: 0px;\n"
"")
        self.powerful.setFrameShape(QFrame.NoFrame)
        self.powerful.setTextFormat(Qt.AutoText)
        self.powerful.setScaledContents(False)
        self.powerful.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.powerful.setWordWrap(False)

        self.verticalLayout_5.addWidget(self.powerful)


        self.verticalLayout_3.addWidget(self.verticalFrame)

        self.verticalFrame_2 = QFrame(self.rightLayout)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalFrame_2.setMaximumSize(QSize(9999, 150))
        self.frame_3 = QFrame(self.verticalFrame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 562, 111))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.loginButton = QPushButton(self.frame_3)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(270, 30, 80, 40))
        sizePolicy1.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy1)
        self.loginButton.setMinimumSize(QSize(0, 0))
        self.loginButton.setMaximumSize(QSize(80, 40))
        font3 = QFont()
        font3.setFamily(u"AvenirNext LT Pro Regular")
        font3.setPointSize(10)
        self.loginButton.setFont(font3)
        self.loginButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginButton.setStyleSheet(u"QPushButton#loginButton{\n"
"   background-color: rgb(148, 194, 130);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover#loginButton{\n"
"   background-color: rgb(148, 194, 130);\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 10pt \"AvenirNext LT Pro Bold\";\n"
"	\n"
"}")
        self.loginButton.setIconSize(QSize(20, 20))
        self.loginButton.setAutoDefault(False)
        self.widget = QWidget(self.frame_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 10, 222, 89))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.username = QLineEdit(self.widget)
        self.username.setObjectName(u"username")
        sizePolicy.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy)
        self.username.setMinimumSize(QSize(220, 40))
        self.username.setMaximumSize(QSize(220, 40))
        font4 = QFont()
        font4.setFamily(u"AvenirNext LT Pro Regular")
        font4.setPointSize(14)
        self.username.setFont(font4)
        self.username.setFocusPolicy(Qt.StrongFocus)
        self.username.setStyleSheet(u"QLineEdit#username{\n"
"background-color: rgb(241, 241, 241);\n"
"border-radius: 20px;\n"
"border: none;\n"
"qproperty-frame: false;\n"
"padding: 0 12px;\n"
"selection-background-color: gray;\n"
"\n"
"\n"
"}\n"
"QLineEdit:focus#username{\n"
"background-color: rgb(241, 241, 241);\n"
"border-radius: 20px;\n"
"border: none;\n"
"qproperty-frame: false;\n"
"padding: 0 12px;\n"
"selection-background-color: gray;\n"
"outline: none;\n"
"\n"
"}")
        self.username.setMaxLength(16)
        self.username.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.username)

        self.userPassword = QLineEdit(self.widget)
        self.userPassword.setObjectName(u"userPassword")
        sizePolicy.setHeightForWidth(self.userPassword.sizePolicy().hasHeightForWidth())
        self.userPassword.setSizePolicy(sizePolicy)
        self.userPassword.setMinimumSize(QSize(220, 40))
        self.userPassword.setMaximumSize(QSize(220, 40))
        self.userPassword.setFont(font4)
        self.userPassword.setFocusPolicy(Qt.StrongFocus)
        self.userPassword.setStyleSheet(u"QLineEdit#userPassword{\n"
"background-color: rgb(241, 241, 241);\n"
"border-radius: 20px;\n"
"border: none;\n"
"qproperty-frame: false;\n"
"padding: 0 12px;\n"
"selection-background-color: gray;\n"
"\n"
"\n"
"}\n"
"QLineEdit:focus#userPassword{\n"
"background-color: rgb(241, 241, 241);\n"
"border-radius: 20px;\n"
"border: none;\n"
"qproperty-frame: false;\n"
"padding: 0 12px;\n"
"selection-background-color: gray;\n"
"outline: none;\n"
"\n"
"}")
        self.userPassword.setMaxLength(16)
        self.userPassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.userPassword)

        self.warning = QLabel(self.verticalFrame_2)
        self.warning.setObjectName(u"warning")
        self.warning.setEnabled(True)
        self.warning.setGeometry(QRect(30, 120, 551, 16))
        font5 = QFont()
        font5.setFamily(u"MS Shell Dlg 2")
        self.warning.setFont(font5)
        self.warning.setStyleSheet(u"color: rgb(255, 0, 0)")

        self.verticalLayout_3.addWidget(self.verticalFrame_2)

        self.horizontalFrame_3 = QFrame(self.rightLayout)
        self.horizontalFrame_3.setObjectName(u"horizontalFrame_3")
        self.horizontalFrame_3.setMinimumSize(QSize(0, 120))
        self.horizontalFrame_3.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(1, 20, -1, -1)
        self.dontHaveAnyAccountYet = QLabel(self.horizontalFrame_3)
        self.dontHaveAnyAccountYet.setObjectName(u"dontHaveAnyAccountYet")
        self.dontHaveAnyAccountYet.setFont(font5)
        self.dontHaveAnyAccountYet.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.dontHaveAnyAccountYet)

        self.signupButton = QPushButton(self.horizontalFrame_3)
        self.signupButton.setObjectName(u"signupButton")
        sizePolicy1.setHeightForWidth(self.signupButton.sizePolicy().hasHeightForWidth())
        self.signupButton.setSizePolicy(sizePolicy1)
        self.signupButton.setMaximumSize(QSize(130, 55))
        font6 = QFont()
        font6.setFamily(u"AvenirNext LT Pro Bold")
        font6.setPointSize(15)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setUnderline(True)
        font6.setWeight(9)
        self.signupButton.setFont(font6)
        self.signupButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.signupButton.setStyleSheet(u"QPushButton#signupButton{\n"
"   background-color:rgb(255, 255, 244);\n"
"	text-decoration: underline;\n"
"	font: 75 15pt \"AvenirNext LT Pro Bold\";\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover#signupButton{\n"
"   background-color: rgb(255, 255, 244);\n"
"	border-radius: 20px;\n"
"	color: rgb(145, 191, 127);\n"
"	font: 75 15pt \"AvenirNext LT Pro Bold\";\n"
"}")
        self.signupButton.setAutoDefault(False)

        self.horizontalLayout_7.addWidget(self.signupButton)


        self.verticalLayout_3.addWidget(self.horizontalFrame_3)


        self.horizontalLayout.addWidget(self.rightLayout)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(loginWindowDialog)

        QMetaObject.connectSlotsByName(loginWindowDialog)
    # setupUi

    def retranslateUi(self, loginWindowDialog):
        loginWindowDialog.setWindowTitle(QCoreApplication.translate("loginWindowDialog", u"Nota", None))
        self.busyText.setText(QCoreApplication.translate("loginWindowDialog", u"DON'T BE BUSY \n"
"BE PRODUCTIVE", None))
        self.nota.setText(QCoreApplication.translate("loginWindowDialog", u"Nota", None))
        self.powerful.setText(QCoreApplication.translate("loginWindowDialog", u"        powerful assistant to help you better manage your time.", None))
        self.loginButton.setText(QCoreApplication.translate("loginWindowDialog", u"SIGN IN", None))
        self.username.setPlaceholderText(QCoreApplication.translate("loginWindowDialog", u"Username", None))
        self.userPassword.setPlaceholderText(QCoreApplication.translate("loginWindowDialog", u"Password", None))
        self.warning.setText(QCoreApplication.translate("loginWindowDialog", u"Sign in failed. The username or password you entered is incorrect. Please try again.", None))
        self.dontHaveAnyAccountYet.setText(QCoreApplication.translate("loginWindowDialog", u"DON'T HAVE ANY ACCOUNT YET ?", None))
        self.signupButton.setText(QCoreApplication.translate("loginWindowDialog", u"SIGN UP", None))
    # retranslateUi

