# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notastartmenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import imageRE
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(974, 604)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftLayout = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.leftLayout.sizePolicy().hasHeightForWidth())
        self.leftLayout.setSizePolicy(sizePolicy)
        self.leftLayout.setMinimumSize(QtCore.QSize(320, 0))
        self.leftLayout.setMaximumSize(QtCore.QSize(320, 16777215))
        self.leftLayout.setStyleSheet("background-color: rgb(130, 164, 118);")
        self.leftLayout.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftLayout.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftLayout.setLineWidth(0)
        self.leftLayout.setObjectName("leftLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftLayout)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.leftLayout)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(200, 200))
        self.frame_2.setStyleSheet("image: url(:/test/imageStartmenu/notaKung.png);\n"
                                   "border: none;\n"
                                   "padding-right: 30px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.busyText = QtWidgets.QLabel(self.leftLayout)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.busyText.sizePolicy().hasHeightForWidth())
        self.busyText.setSizePolicy(sizePolicy)
        self.busyText.setMaximumSize(QtCore.QSize(700, 16777215))
        font = QtGui.QFont()
        font.setFamily("Telugu MN")
        font.setPointSize(21)
        self.busyText.setFont(font)
        self.busyText.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "padding-left: 35px;\n"
                                    "padding-top: 150px;\n"
                                    "\n"
                                    "")
        self.busyText.setObjectName("busyText")
        self.horizontalLayout_5.addWidget(self.busyText)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addWidget(self.leftLayout)
        self.rightLayout = QtWidgets.QFrame(self.frame)
        self.rightLayout.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.rightLayout.setStyleSheet("background-color: rgb(255, 255, 244);")
        self.rightLayout.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightLayout.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightLayout.setLineWidth(0)
        self.rightLayout.setObjectName("rightLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.rightLayout)
        self.verticalLayout_3.setContentsMargins(15, 0, 15, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalFrame = QtWidgets.QFrame(self.rightLayout)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy)
        self.verticalFrame.setMaximumSize(QtCore.QSize(16777215, 140))
        self.verticalFrame.setStyleSheet("")
        self.verticalFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.nota = QtWidgets.QLabel(self.verticalFrame)
        self.nota.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Telugu MN")
        font.setPointSize(100)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.nota.setFont(font)
        self.nota.setStyleSheet("color: rgb(123, 160, 108);\n"
                                "padding-left: 5px;")
        self.nota.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.nota.setTextFormat(QtCore.Qt.AutoText)
        self.nota.setScaledContents(False)
        self.nota.setAlignment(QtCore.Qt.AlignLeading |
                               QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.nota.setWordWrap(False)
        self.nota.setObjectName("nota")
        self.verticalLayout_5.addWidget(self.nota)
        self.powerful = QtWidgets.QLabel(self.verticalFrame)
        self.powerful.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Avenir Next")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.powerful.setFont(font)
        self.powerful.setStyleSheet("color: rgb(97, 97, 97);\n"
                                    "padding-top: 0px;\n"
                                    "")
        self.powerful.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.powerful.setTextFormat(QtCore.Qt.AutoText)
        self.powerful.setScaledContents(False)
        self.powerful.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.powerful.setWordWrap(False)
        self.powerful.setObjectName("powerful")
        self.verticalLayout_5.addWidget(self.powerful)
        self.verticalLayout_3.addWidget(self.verticalFrame)
        self.verticalFrame_2 = QtWidgets.QFrame(self.rightLayout)
        self.verticalFrame_2.setMaximumSize(QtCore.QSize(9999, 150))
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.verticalFrame_2)
        self.horizontalLayout_12.setContentsMargins(100, -1, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalFrame_3 = QtWidgets.QFrame(self.verticalFrame_2)
        self.verticalFrame_3.setObjectName("verticalFrame_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalFrame_3)
        self.verticalLayout_9.setContentsMargins(220, -1, 1, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.username = QtWidgets.QLineEdit(self.verticalFrame_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy)
        self.username.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.username.setFont(font)
        self.username.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.username.setStyleSheet("QLineEdit#username{\n"
                                    "background-color: rgb(241, 241, 241);\n"
                                    "border-radius: 20px;\n"
                                    "border: none;\n"
                                    "qproperty-frame: false;\n"
                                    "padding: 0 12px;\n"
                                    "selection-background-color: gray;\n"
                                    "WA_MacShowFocusRect: 0;\n"
                                    "PE_FrameFocusRect: 0;\n"
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
                                    "WA_MacShowFocusRect: 0;\n"
                                    "PE_FrameFocusRect: 0;\n"
                                    "}")
        self.username.setMaxLength(16)
        self.username.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.username.setObjectName("username")
        self.verticalLayout_9.addWidget(self.username)
        self.userPassword = QtWidgets.QLineEdit(self.verticalFrame_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.userPassword.sizePolicy().hasHeightForWidth())
        self.userPassword.setSizePolicy(sizePolicy)
        self.userPassword.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.userPassword.setFont(font)
        self.userPassword.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.userPassword.setStyleSheet("QLineEdit#userPassword{\n"
                                        "background-color: rgb(241, 241, 241);\n"
                                        "border-radius: 20px;\n"
                                        "border: none;\n"
                                        "qproperty-frame: false;\n"
                                        "padding: 0 12px;\n"
                                        "selection-background-color: gray;\n"
                                        "WA_MacShowFocusRect: 0;\n"
                                        "PE_FrameFocusRect: 0;\n"
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
                                        "WA_MacShowFocusRect: 0;\n"
                                        "PE_FrameFocusRect: 0;\n"
                                        "}")
        self.userPassword.setMaxLength(16)
        self.userPassword.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.userPassword.setObjectName("userPassword")
        self.verticalLayout_9.addWidget(self.userPassword)
        self.horizontalLayout_12.addWidget(self.verticalFrame_3)
        self.loginButton = QtWidgets.QPushButton(self.verticalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setMinimumSize(QtCore.QSize(0, 0))
        self.loginButton.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("Avenir Next")
        font.setPointSize(13)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("QPushButton#loginButton{\n"
                                       "   background-color: rgb(148, 194, 130);\n"
                                       "    border-radius: 20px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover#loginButton{\n"
                                       "   background-color: rgb(148, 194, 130);\n"
                                       "    border-radius: 20px;\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "     font: 14pt\n"
                                       "}")
        self.loginButton.setAutoDefault(False)
        self.loginButton.setObjectName("loginButton")
        self.horizontalLayout_12.addWidget(self.loginButton)
        self.verticalLayout_3.addWidget(self.verticalFrame_2)
        self.horizontalFrame_3 = QtWidgets.QFrame(self.rightLayout)
        self.horizontalFrame_3.setMinimumSize(QtCore.QSize(0, 120))
        self.horizontalFrame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.horizontalFrame_3.setObjectName("horizontalFrame_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_7.setContentsMargins(1, 20, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.powerful_2 = QtWidgets.QLabel(self.horizontalFrame_3)
        self.powerful_2.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("Avenir Next")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.powerful_2.setFont(font)
        self.powerful_2.setStyleSheet("color: rgb(150, 195, 131);")
        self.powerful_2.setTextFormat(QtCore.Qt.AutoText)
        self.powerful_2.setScaledContents(False)
        self.powerful_2.setWordWrap(False)
        self.powerful_2.setObjectName("powerful_2")
        self.horizontalLayout_7.addWidget(self.powerful_2)
        self.signupButton = QtWidgets.QPushButton(self.horizontalFrame_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.signupButton.sizePolicy().hasHeightForWidth())
        self.signupButton.setSizePolicy(sizePolicy)
        self.signupButton.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("Avenir Next")
        self.signupButton.setFont(font)
        self.signupButton.setStyleSheet("QPushButton#signupButton{\n"
                                        "   background-color: rgb(148, 194, 130);\n"
                                        "    border-radius: 20px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover#signupButton{\n"
                                        "   background-color: rgb(148, 194, 130);\n"
                                        "    border-radius: 20px;\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "     font: 14pt\n"
                                        "}")
        self.signupButton.setAutoDefault(False)
        self.signupButton.setObjectName("signupButton")
        self.horizontalLayout_7.addWidget(self.signupButton)
        self.verticalLayout_3.addWidget(self.horizontalFrame_3)
        self.horizontalLayout.addWidget(self.rightLayout)
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nota"))
        self.busyText.setText(_translate("MainWindow", "DON\'T BE BUSY \n"
                                         "BE PRODUCTIVE"))
        self.nota.setText(_translate("MainWindow", "Nota"))
        self.powerful.setText(_translate(
            "MainWindow", "        powerful assistant to help you better manage your time."))
        self.username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.userPassword.setPlaceholderText(
            _translate("MainWindow", "Password"))
        self.loginButton.setText(_translate("MainWindow", "LOGIN"))
        self.powerful_2.setText(_translate(
            "MainWindow", "2021, FPGN team. CE KMITL 59"))
        self.signupButton.setText(_translate("MainWindow", "SIGN UP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
