# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nut.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import imageteest_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(974, 604)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftLayout = QFrame(self.frame)
        self.leftLayout.setObjectName(u"leftLayout")
        sizePolicy.setHeightForWidth(self.leftLayout.sizePolicy().hasHeightForWidth())
        self.leftLayout.setSizePolicy(sizePolicy)
        self.leftLayout.setMinimumSize(QSize(320, 0))
        self.leftLayout.setMaximumSize(QSize(320, 16777215))
        self.leftLayout.setStyleSheet(u"background-color: rgb(130, 164, 118);")
        self.leftLayout.setFrameShape(QFrame.StyledPanel)
        self.leftLayout.setFrameShadow(QFrame.Raised)
        self.leftLayout.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.leftLayout)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.leftLayout)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(200, 200))
        self.frame_2.setStyleSheet(u"image: url(:/test/imageStartmenu/notaKung.png);\n"
"border: none;\n"
"padding-right: 30px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)

        self.horizontalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.busyText = QLabel(self.leftLayout)
        self.busyText.setObjectName(u"busyText")
        sizePolicy1.setHeightForWidth(self.busyText.sizePolicy().hasHeightForWidth())
        self.busyText.setSizePolicy(sizePolicy1)
        self.busyText.setMaximumSize(QSize(700, 16777215))
        font = QFont()
        font.setFamilies([u"Telugu MN"])
        font.setPointSize(21)
        self.busyText.setFont(font)
        self.busyText.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left: 35px;\n"
"padding-top: 150px;\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.busyText)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


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
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy2)
        self.verticalFrame.setMaximumSize(QSize(16777215, 140))
        self.verticalFrame.setStyleSheet(u"")
        self.verticalFrame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.nota = QLabel(self.verticalFrame)
        self.nota.setObjectName(u"nota")
        self.nota.setMaximumSize(QSize(16777215, 100))
        font1 = QFont()
        font1.setFamilies([u"Telugu MN"])
        font1.setPointSize(100)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
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
        font2.setFamilies([u"Avenir Next"])
        font2.setPointSize(18)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
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
        self.horizontalLayout_12 = QHBoxLayout(self.verticalFrame_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(100, -1, -1, -1)
        self.verticalFrame_3 = QFrame(self.verticalFrame_2)
        self.verticalFrame_3.setObjectName(u"verticalFrame_3")
        self.verticalLayout_9 = QVBoxLayout(self.verticalFrame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(220, -1, 1, -1)
        self.username = QLineEdit(self.verticalFrame_3)
        self.username.setObjectName(u"username")
        sizePolicy.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy)
        self.username.setMaximumSize(QSize(200, 40))
        font3 = QFont()
        font3.setPointSize(14)
        self.username.setFont(font3)
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

        self.verticalLayout_9.addWidget(self.username)

        self.userPassword = QLineEdit(self.verticalFrame_3)
        self.userPassword.setObjectName(u"userPassword")
        sizePolicy.setHeightForWidth(self.userPassword.sizePolicy().hasHeightForWidth())
        self.userPassword.setSizePolicy(sizePolicy)
        self.userPassword.setMaximumSize(QSize(200, 40))
        self.userPassword.setFont(font3)
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
        self.userPassword.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.verticalLayout_9.addWidget(self.userPassword)


        self.horizontalLayout_12.addWidget(self.verticalFrame_3)

        self.loginButton = QPushButton(self.verticalFrame_2)
        self.loginButton.setObjectName(u"loginButton")
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setMinimumSize(QSize(0, 0))
        self.loginButton.setMaximumSize(QSize(80, 40))
        font4 = QFont()
        font4.setFamilies([u"Avenir Next"])
        font4.setPointSize(13)
        self.loginButton.setFont(font4)
        self.loginButton.setStyleSheet(u"QPushButton#loginButton{\n"
"   background-color: rgb(148, 194, 130);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover#loginButton{\n"
"   background-color: rgb(148, 194, 130);\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
" 	font: 14pt\n"
"}")
        self.loginButton.setAutoDefault(False)

        self.horizontalLayout_12.addWidget(self.loginButton)


        self.verticalLayout_3.addWidget(self.verticalFrame_2)

        self.horizontalFrame_3 = QFrame(self.rightLayout)
        self.horizontalFrame_3.setObjectName(u"horizontalFrame_3")
        self.horizontalFrame_3.setMinimumSize(QSize(0, 120))
        self.horizontalFrame_3.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(1, 20, -1, -1)
        self.powerful_2 = QLabel(self.horizontalFrame_3)
        self.powerful_2.setObjectName(u"powerful_2")
        self.powerful_2.setMinimumSize(QSize(0, 100))
        font5 = QFont()
        font5.setFamilies([u"Avenir Next"])
        font5.setPointSize(18)
        font5.setBold(False)
        font5.setItalic(True)
        font5.setUnderline(False)
        font5.setStrikeOut(False)
        font5.setKerning(True)
        self.powerful_2.setFont(font5)
        self.powerful_2.setStyleSheet(u"color: rgb(150, 195, 131);")
        self.powerful_2.setTextFormat(Qt.AutoText)
        self.powerful_2.setScaledContents(False)
        self.powerful_2.setWordWrap(False)

        self.horizontalLayout_7.addWidget(self.powerful_2)

        self.signupButton = QPushButton(self.horizontalFrame_3)
        self.signupButton.setObjectName(u"signupButton")
        sizePolicy.setHeightForWidth(self.signupButton.sizePolicy().hasHeightForWidth())
        self.signupButton.setSizePolicy(sizePolicy)
        self.signupButton.setMaximumSize(QSize(80, 40))
        font6 = QFont()
        font6.setFamilies([u"Avenir Next"])
        self.signupButton.setFont(font6)
        self.signupButton.setStyleSheet(u"QPushButton#signupButton{\n"
"   background-color: rgb(148, 194, 130);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover#signupButton{\n"
"   background-color: rgb(148, 194, 130);\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
" 	font: 14pt\n"
"}")
        self.signupButton.setAutoDefault(False)

        self.horizontalLayout_7.addWidget(self.signupButton)


        self.verticalLayout_3.addWidget(self.horizontalFrame_3)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.rightLayout)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Nota", None))
        self.busyText.setText(QCoreApplication.translate("MainWindow", u"DON'T BE BUSY \n"
"BE PRODUCTIVE", None))
        self.nota.setText(QCoreApplication.translate("MainWindow", u"Nota", None))
        self.powerful.setText(QCoreApplication.translate("MainWindow", u"        powerful assistant to help you better manage your time.", None))
        self.username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.userPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.powerful_2.setText(QCoreApplication.translate("MainWindow", u"2021, FPGN team. CE KMITL 59", None))
        self.signupButton.setText(QCoreApplication.translate("MainWindow", u"SIGN UP", None))
    # retranslateUi

