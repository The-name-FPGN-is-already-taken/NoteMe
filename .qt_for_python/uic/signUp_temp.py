# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signUp_temp.ui'
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
        self.mainLayout = QFrame(self.frame)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setFocusPolicy(Qt.StrongFocus)
        self.mainLayout.setStyleSheet(u"background-color: rgb(255, 255, 244);")
        self.mainLayout.setFrameShape(QFrame.StyledPanel)
        self.mainLayout.setFrameShadow(QFrame.Raised)
        self.mainLayout.setLineWidth(0)
        self.verticalFrame = QFrame(self.mainLayout)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setGeometry(QRect(20, -11, 995, 491))
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy2)
        self.verticalFrame.setMaximumSize(QSize(16777215, 500))
        self.verticalFrame.setStyleSheet(u"")
        self.verticalFrame.setFrameShape(QFrame.NoFrame)
        self.widget = QWidget(self.verticalFrame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(330, 10, 371, 471))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.notaIconFrame = QFrame(self.widget)
        self.notaIconFrame.setObjectName(u"notaIconFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.notaIconFrame.sizePolicy().hasHeightForWidth())
        self.notaIconFrame.setSizePolicy(sizePolicy3)
        self.notaIconFrame.setMinimumSize(QSize(200, 200))
        self.notaIconFrame.setStyleSheet(u"image: url(D:/NotaProject/pics/notaKung.png);\n"
"border: none;\n"
"padding-right: 30px;")
        self.notaIconFrame.setFrameShape(QFrame.StyledPanel)
        self.notaIconFrame.setFrameShadow(QFrame.Raised)
        self.notaIconFrame.setLineWidth(0)

        self.verticalLayout.addWidget(self.notaIconFrame)

        self.nota = QLabel(self.widget)
        self.nota.setObjectName(u"nota")
        self.nota.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setFamily(u"Telugu MN")
        font.setPointSize(75)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.nota.setFont(font)
        self.nota.setStyleSheet(u"color: rgb(123, 160, 108);\n"
"")
        self.nota.setFrameShape(QFrame.NoFrame)
        self.nota.setTextFormat(Qt.AutoText)
        self.nota.setScaledContents(False)
        self.nota.setAlignment(Qt.AlignCenter)
        self.nota.setWordWrap(False)

        self.verticalLayout.addWidget(self.nota)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.username = QLineEdit(self.frame_3)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(20, 20, 220, 40))
        sizePolicy.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy)
        self.username.setMinimumSize(QSize(220, 40))
        self.username.setMaximumSize(QSize(220, 40))
        font1 = QFont()
        font1.setFamily(u"AvenirNext LT Pro Regular")
        font1.setPointSize(14)
        self.username.setFont(font1)
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
        self.userPassword = QLineEdit(self.frame_3)
        self.userPassword.setObjectName(u"userPassword")
        self.userPassword.setGeometry(QRect(20, 70, 220, 40))
        sizePolicy.setHeightForWidth(self.userPassword.sizePolicy().hasHeightForWidth())
        self.userPassword.setSizePolicy(sizePolicy)
        self.userPassword.setMinimumSize(QSize(220, 40))
        self.userPassword.setMaximumSize(QSize(220, 40))
        self.userPassword.setFont(font1)
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
        self.userPassword.setEchoMode(QLineEdit.Normal)
        self.signUpButton = QPushButton(self.frame_3)
        self.signUpButton.setObjectName(u"signUpButton")
        self.signUpButton.setGeometry(QRect(270, 50, 80, 40))
        sizePolicy1.setHeightForWidth(self.signUpButton.sizePolicy().hasHeightForWidth())
        self.signUpButton.setSizePolicy(sizePolicy1)
        self.signUpButton.setMinimumSize(QSize(0, 0))
        self.signUpButton.setMaximumSize(QSize(80, 40))
        font2 = QFont()
        font2.setFamily(u"AvenirNext LT Pro Regular")
        font2.setPointSize(10)
        self.signUpButton.setFont(font2)
        self.signUpButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.signUpButton.setStyleSheet(u"QPushButton#signUpButton{\n"
"   background-color: rgb(148, 194, 130);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover#signUpButton{\n"
"   background-color: rgb(148, 194, 130);\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 10pt \"AvenirNext LT Pro Bold\";\n"
"}")
        self.signUpButton.setIconSize(QSize(20, 20))
        self.signUpButton.setAutoDefault(False)

        self.verticalLayout.addWidget(self.frame_3)

        self.notaIconFrame.raise_()
        self.nota.raise_()
        self.widget1 = QWidget(self.mainLayout)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(380, 480, 321, 151))
        self.verticalLayout_3 = QVBoxLayout(self.widget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.warning = QLabel(self.widget1)
        self.warning.setObjectName(u"warning")
        self.warning.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.warning.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.warning)

        self.horizontalFrame_4 = QFrame(self.widget1)
        self.horizontalFrame_4.setObjectName(u"horizontalFrame_4")
        self.horizontalFrame_4.setMinimumSize(QSize(0, 120))
        self.horizontalFrame_4.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.dontHaveAnyAccountYet = QLabel(self.horizontalFrame_4)
        self.dontHaveAnyAccountYet.setObjectName(u"dontHaveAnyAccountYet")
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        self.dontHaveAnyAccountYet.setFont(font3)
        self.dontHaveAnyAccountYet.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.dontHaveAnyAccountYet)

        self.signInButton = QPushButton(self.horizontalFrame_4)
        self.signInButton.setObjectName(u"signInButton")
        sizePolicy1.setHeightForWidth(self.signInButton.sizePolicy().hasHeightForWidth())
        self.signInButton.setSizePolicy(sizePolicy1)
        self.signInButton.setMaximumSize(QSize(158, 55))
        font4 = QFont()
        font4.setFamily(u"AvenirNext LT Pro Bold")
        font4.setPointSize(15)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setUnderline(True)
        font4.setWeight(9)
        self.signInButton.setFont(font4)
        self.signInButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.signInButton.setStyleSheet(u"QPushButton#signInButton{\n"
"   background-color:rgb(255, 255, 244);\n"
"	text-decoration: underline;\n"
"	font: 75 15pt \"AvenirNext LT Pro Bold\";\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover#signInButton{\n"
"   background-color: rgb(255, 255, 244);\n"
"	border-radius: 20px;\n"
"	color: rgb(145, 191, 127);\n"
"	font: 75 15pt \"AvenirNext LT Pro Bold\";\n"
"}")
        self.signInButton.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.signInButton)


        self.verticalLayout_3.addWidget(self.horizontalFrame_4)


        self.horizontalLayout.addWidget(self.mainLayout)


        self.verticalLayout_2.addWidget(self.frame)

        self.widget2 = QWidget(loginWindowDialog)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout_4 = QVBoxLayout(self.widget2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.retranslateUi(loginWindowDialog)

        QMetaObject.connectSlotsByName(loginWindowDialog)
    # setupUi

    def retranslateUi(self, loginWindowDialog):
        loginWindowDialog.setWindowTitle(QCoreApplication.translate("loginWindowDialog", u"Nota", None))
        self.nota.setText(QCoreApplication.translate("loginWindowDialog", u"Nota", None))
        self.username.setPlaceholderText(QCoreApplication.translate("loginWindowDialog", u"Username", None))
        self.userPassword.setPlaceholderText(QCoreApplication.translate("loginWindowDialog", u"Password", None))
        self.signUpButton.setText(QCoreApplication.translate("loginWindowDialog", u"SIGN UP", None))
        self.warning.setText(QCoreApplication.translate("loginWindowDialog", u"Sign up failed. Already have this username.", None))
        self.dontHaveAnyAccountYet.setText(QCoreApplication.translate("loginWindowDialog", u"ALREADY HAVE AN ACCOUNT ?", None))
        self.signInButton.setText(QCoreApplication.translate("loginWindowDialog", u"SIGN IN", None))
    # retranslateUi

