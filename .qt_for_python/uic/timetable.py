# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timetable.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1024, 640)
        Dialog.setMinimumSize(QSize(1024, 640))
        Dialog.setMaximumSize(QSize(1024, 640))
        self.leftBar = QFrame(Dialog)
        self.leftBar.setObjectName(u"leftBar")
        self.leftBar.setGeometry(QRect(0, 90, 91, 551))
        self.leftBar.setStyleSheet(u"\n"
"\n"
"position: absolute;\n"
"width: 140px;\n"
"height: 540px;\n"
"left: 0px;\n"
"top: 100px;\n"
"\n"
"background: #A3C5A7;")
        self.leftBar.setFrameShape(QFrame.StyledPanel)
        self.leftBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.leftBar)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.homeButton = QPushButton(self.leftBar)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setCursor(QCursor(Qt.ArrowCursor))
        self.homeButton.setStyleSheet(u"position: absolute;\n"
"\n"
"image: url(D:/NotaProject/pics/home.png);\n"
"width: 120px;\n"
"height: 37px;\n"
"left: 7px;\n"
"top: 16px;\n"
"text-align: right;\n"
"background: #C4C4C4;\n"
"border: 1px solid #000000;\n"
"mix-blend-mode: normal;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 10px;\n"
"box-shadow: 0px 4px 4px 0px #00000040;\n"
"")

        self.verticalLayout_2.addWidget(self.homeButton)

        self.home_label = QLabel(self.leftBar)
        self.home_label.setObjectName(u"home_label")
        self.home_label.setStyleSheet(u"text-align: center;")

        self.verticalLayout_2.addWidget(self.home_label)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.timeTableButton = QPushButton(self.leftBar)
        self.timeTableButton.setObjectName(u"timeTableButton")
        self.timeTableButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.timeTableButton.setStyleSheet(u"image: url(D:/NotaProject/pics/timetable.png);\n"
"position: absolute;\n"
"width: 120px;\n"
"height: 37px;\n"
"left: 7px;\n"
"top: 160px;\n"
"text-align: right;\n"
"background: #ECF39E;\n"
"border: 1px solid #000000;\n"
"box-sizing: border-box;\n"
"box-shadow: inset 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 10px;\n"
"text-align: center;")

        self.verticalLayout_3.addWidget(self.timeTableButton)

        self.timeTable_label = QLabel(self.leftBar)
        self.timeTable_label.setObjectName(u"timeTable_label")

        self.verticalLayout_3.addWidget(self.timeTable_label)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.noteButton = QPushButton(self.leftBar)
        self.noteButton.setObjectName(u"noteButton")
        self.noteButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.noteButton.setStyleSheet(u"image: url(D:/NotaProject/pics/writing.png);\n"
"position: absolute;\n"
"width: 120px;\n"
"height: 37px;\n"
"left: 7px;\n"
"top: 160px;\n"
"text-align: right;\n"
"background: #C4C4C4;\n"
"border: 1px solid #000000;\n"
"box-sizing: border-box;\n"
"box-shadow: inset 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 10px;")

        self.verticalLayout_4.addWidget(self.noteButton)

        self.note_label = QLabel(self.leftBar)
        self.note_label.setObjectName(u"note_label")

        self.verticalLayout_4.addWidget(self.note_label)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.taskButton = QPushButton(self.leftBar)
        self.taskButton.setObjectName(u"taskButton")
        self.taskButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.taskButton.setStyleSheet(u"image: url(D:/NotaProject/pics/task.png);\n"
"position: absolute;\n"
"width: 120px;\n"
"height: 37px;\n"
"left: 7px;\n"
"top: 160px;\n"
"text-align: right;\n"
"background: #C4C4C4;\n"
"border: 1px solid #000000;\n"
"box-sizing: border-box;\n"
"box-shadow: inset 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 10px;")

        self.verticalLayout_5.addWidget(self.taskButton)

        self.task_label = QLabel(self.leftBar)
        self.task_label.setObjectName(u"task_label")

        self.verticalLayout_5.addWidget(self.task_label)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.addNote_button = QPushButton(self.leftBar)
        self.addNote_button.setObjectName(u"addNote_button")
        self.addNote_button.setMinimumSize(QSize(77, 81))
        self.addNote_button.setMaximumSize(QSize(77, 81))
        self.addNote_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.addNote_button.setFocusPolicy(Qt.ClickFocus)
        self.addNote_button.setStyleSheet(u"background: rgba(0,0,0,0);\n"
"image: url(D:/NotaProject/pics/add.png);")

        self.verticalLayout_7.addWidget(self.addNote_button)

        self.signOutButton = QPushButton(self.leftBar)
        self.signOutButton.setObjectName(u"signOutButton")
        self.signOutButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.signOutButton.setStyleSheet(u"position: absolute;\n"
"width: 65px;\n"
"height: 40px;\n"
"left: 29px;\n"
"top: 346px;\n"
"background: #EC8E65;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 15px;\n"
"box-shadow: 2px 2px 5px red;\n"
"\n"
"QPushButton:hover#signOutButton{\n"
"	background-color: rgb(148, 194, 130);\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 14pt;\n"
"                                       }")

        self.verticalLayout_7.addWidget(self.signOutButton)

        self.flower_frame = QFrame(self.leftBar)
        self.flower_frame.setObjectName(u"flower_frame")
        self.flower_frame.setStyleSheet(u"width: 126px;\n"
"image: url(D:/NotaProject/pics/sunlight.png);\n"
"height: 126px;\n"
"left: 7px;\n"
"top: 414px;\n"
"")
        self.flower_frame.setFrameShape(QFrame.StyledPanel)
        self.flower_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.flower_frame)

        self.topBar = QFrame(Dialog)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setGeometry(QRect(0, 0, 1024, 101))
        self.topBar.setStyleSheet(u"position: absolute;\n"
"width: 1024px;\n"
"height: 100px;\n"
"left: 0px;\n"
"top: 0px;\n"
"text-align: center;\n"
"box-shadow: 0px 4px 4px 0px #00000040;\n"
"\n"
"background: #FEFAE0;")
        self.topBar.setFrameShape(QFrame.StyledPanel)
        self.topBar.setFrameShadow(QFrame.Raised)
        self.app_icon = QFrame(self.topBar)
        self.app_icon.setObjectName(u"app_icon")
        self.app_icon.setGeometry(QRect(10, 10, 81, 81))
        self.app_icon.setStyleSheet(u"width: 85px;\n"
"height: 85px;\n"
"image: url(D:/NotaProject/pics/notaKung.png);\n"
"left: 3px;\n"
"top: 5px;\n"
"\n"
"background: #86B18B;\n"
"mix-blend-mode: normal;\n"
"border-radius: 35px;\n"
"")
        self.app_icon.setFrameShape(QFrame.StyledPanel)
        self.app_icon.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.topBar)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 20, 161, 53))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.welcomeUser = QLabel(self.layoutWidget)
        self.welcomeUser.setObjectName(u"welcomeUser")
        font = QFont()
        font.setFamily(u"Tenor Sans")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.welcomeUser.setFont(font)
        self.welcomeUser.setStyleSheet(u"position: absolute;\n"
"width: 190px;\n"
"height: 44px;\n"
"left: 103px;\n"
"top: 28px;\n"
"text-align: center;\n"
"font-family: Tenor Sans;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;\n"
"line-height: 21px;\n"
"\n"
"color: #000000;")

        self.verticalLayout.addWidget(self.welcomeUser)

        self.date = QLabel(self.layoutWidget)
        self.date.setObjectName(u"date")
        self.date.setStyleSheet(u"position: absolute;\n"
"width: 190px;\n"
"height: 44px;\n"
"left: 103px;\n"
"top: 28px;\n"
"\n"
"font-family: Tenor Sans;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 18px;\n"
"line-height: 21px;\n"
"\n"
"color: #000000;")

        self.verticalLayout.addWidget(self.date)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(90, 100, 931, 541))
        self.frame.setStyleSheet(u"background: #84B289;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.today_label = QLabel(self.frame)
        self.today_label.setObjectName(u"today_label")
        self.today_label.setGeometry(QRect(110, 90, 201, 51))
        font1 = QFont()
        font1.setFamily(u"AvenirNext LT Pro Bold")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.today_label.setFont(font1)
        self.today_label.setStyleSheet(u"display: flex;\n"
"flex-direction: column;\n"
"align-items: center;\n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")
        self.today_label.setAlignment(Qt.AlignCenter)
        self.layoutWidget_2 = QWidget(self.frame)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 20, 871, 45))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.previous_button = QPushButton(self.layoutWidget_2)
        self.previous_button.setObjectName(u"previous_button")
        self.previous_button.setMaximumSize(QSize(51, 31))
        self.previous_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.previous_button.setStyleSheet(u"image: url(:/leftArrow/pics/right-arrow.png);\n"
"image: url(:/leftArrow/pics/left-arrow.png);\n"
"position: absolute;\n"
"width: 90px;\n"
"height: 50px;\n"
"left: 806px;\n"
"top: 31px;\n"
"text-align: center;\n"
"background: #84B289;\n"
"border-radius: 15px;\n"
"transform: rotate(90deg);")

        self.horizontalLayout_3.addWidget(self.previous_button)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.monday_button_2 = QPushButton(self.layoutWidget_2)
        self.monday_button_2.setObjectName(u"monday_button_2")
        self.monday_button_2.setMaximumSize(QSize(93, 41))
        self.monday_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.monday_button_2.setStyleSheet(u"display: flex;\n"
"flex-direction: column;\n"
"align-items: center;\n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_4.addWidget(self.monday_button_2)

        self.tuesday_button_2 = QPushButton(self.layoutWidget_2)
        self.tuesday_button_2.setObjectName(u"tuesday_button_2")
        self.tuesday_button_2.setMaximumSize(QSize(93, 41))
        self.tuesday_button_2.setStyleSheet(u"display: flex;\n"
"flex-direction: column;\n"
"align-items: center;\n"
"padding: 8px 0px;\n"
"color: rgb(255, 255, 255);\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"\n"
"\n"
"background: #FFAC4B;\n"
"border-radius: 8px;")

        self.horizontalLayout_4.addWidget(self.tuesday_button_2)

        self.wednesday_button_2 = QPushButton(self.layoutWidget_2)
        self.wednesday_button_2.setObjectName(u"wednesday_button_2")
        self.wednesday_button_2.setMaximumSize(QSize(93, 41))
        self.wednesday_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.wednesday_button_2.setStyleSheet(u"display: flex;\n"
"flex-direction: column;\n"
"align-items: center;\n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_4.addWidget(self.wednesday_button_2)

        self.thursday_button_2 = QPushButton(self.layoutWidget_2)
        self.thursday_button_2.setObjectName(u"thursday_button_2")
        self.thursday_button_2.setMaximumSize(QSize(93, 41))
        self.thursday_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.thursday_button_2.setStyleSheet(u"display: flex;\n"
"flex-direction: column;\n"
"align-items: center;\n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_4.addWidget(self.thursday_button_2)

        self.friday_button_2 = QPushButton(self.layoutWidget_2)
        self.friday_button_2.setObjectName(u"friday_button_2")
        self.friday_button_2.setMaximumSize(QSize(93, 41))
        self.friday_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.friday_button_2.setStyleSheet(u"display: flex;\n"
"flex-direction: column;\n"
"align-items: center;\n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_4.addWidget(self.friday_button_2)

        self.saturday_button_2 = QPushButton(self.layoutWidget_2)
        self.saturday_button_2.setObjectName(u"saturday_button_2")
        self.saturday_button_2.setMaximumSize(QSize(93, 41))
        self.saturday_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.saturday_button_2.setStyleSheet(u"display: flex;\n"
"flex-direction: column;\n"
"align-items: center;\n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_4.addWidget(self.saturday_button_2)

        self.sunday_button_2 = QPushButton(self.layoutWidget_2)
        self.sunday_button_2.setObjectName(u"sunday_button_2")
        self.sunday_button_2.setMaximumSize(QSize(93, 41))
        self.sunday_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.sunday_button_2.setStyleSheet(u"display: flex;\n"
"flex-direction: column;\n"
"align-items: center;\n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_4.addWidget(self.sunday_button_2)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)

        self.next_button = QPushButton(self.layoutWidget_2)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setMaximumSize(QSize(51, 31))
        self.next_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_button.setStyleSheet(u"image: url(:/rightArrow/pics/right-arrow.png);\n"
"position: absolute;\n"
"width: 90px;\n"
"height: 50px;\n"
"left: 806px;\n"
"top: 31px;\n"
"text-align: center;\n"
"background: #84B289;\n"
"border-radius: 15px;")

        self.horizontalLayout_3.addWidget(self.next_button)

        self.today_label_2 = QLabel(self.frame)
        self.today_label_2.setObjectName(u"today_label_2")
        self.today_label_2.setGeometry(QRect(590, 90, 201, 51))
        self.today_label_2.setFont(font1)
        self.today_label_2.setStyleSheet(u"display: flex;\n"
"flex-direction: column;\n"
"align-items: center;\n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")
        self.today_label_2.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 160, 851, 331))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidget_2 = QListWidget(self.horizontalLayoutWidget)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setStyleSheet(u"background: #FEFAE0;")

        self.horizontalLayout.addWidget(self.listWidget_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, -1, 0, -1)
        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(81, 31))
        self.pushButton.setMaximumSize(QSize(81, 31))
        self.pushButton.setStyleSheet(u"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.verticalLayout_8.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(81, 31))
        self.pushButton_2.setMaximumSize(QSize(81, 31))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.verticalLayout_8.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(81, 31))
        self.pushButton_3.setMaximumSize(QSize(81, 31))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.verticalLayout_8.addWidget(self.pushButton_3)


        self.horizontalLayout.addLayout(self.verticalLayout_8)

        self.listWidget = QListWidget(self.horizontalLayoutWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"background: #FEFAE0;")

        self.horizontalLayout.addWidget(self.listWidget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.homeButton.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/>home</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.homeButton.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>home</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.homeButton.setText("")
        self.home_label.setText(QCoreApplication.translate("Dialog", u"     HOME", None))
        self.timeTableButton.setText("")
        self.timeTable_label.setText(QCoreApplication.translate("Dialog", u"TIMETABLE", None))
        self.noteButton.setText("")
        self.note_label.setText(QCoreApplication.translate("Dialog", u"    NOTE", None))
        self.taskButton.setText("")
        self.task_label.setText(QCoreApplication.translate("Dialog", u"    TASK", None))
        self.addNote_button.setText("")
        self.signOutButton.setText(QCoreApplication.translate("Dialog", u"SIGN OUT", None))
        self.welcomeUser.setText(QCoreApplication.translate("Dialog", u"Welcome,", None))
        self.date.setText(QCoreApplication.translate("Dialog", u"November 21, 2021", None))
#if QT_CONFIG(tooltip)
        self.today_label.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.today_label.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.today_label.setText(QCoreApplication.translate("Dialog", u"Daily Task", None))
        self.previous_button.setText("")
        self.monday_button_2.setText(QCoreApplication.translate("Dialog", u"MONDAY", None))
        self.tuesday_button_2.setText(QCoreApplication.translate("Dialog", u"TUESDAY", None))
        self.wednesday_button_2.setText(QCoreApplication.translate("Dialog", u"WEDNESDAY", None))
        self.thursday_button_2.setText(QCoreApplication.translate("Dialog", u"THURSDAY", None))
        self.friday_button_2.setText(QCoreApplication.translate("Dialog", u"FRIDAY", None))
        self.saturday_button_2.setText(QCoreApplication.translate("Dialog", u"SATURDAY", None))
        self.sunday_button_2.setText(QCoreApplication.translate("Dialog", u"SUNDAY", None))
        self.next_button.setText("")
#if QT_CONFIG(tooltip)
        self.today_label_2.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.today_label_2.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.today_label_2.setText(QCoreApplication.translate("Dialog", u"Finish Daily Task", None))

        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_2.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem1 = self.listWidget_2.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem2 = self.listWidget_2.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem3 = self.listWidget_2.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem4 = self.listWidget_2.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem5 = self.listWidget_2.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem6 = self.listWidget_2.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem7 = self.listWidget_2.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("Dialog", u"a", None));
        ___qlistwidgetitem8 = self.listWidget_2.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem9 = self.listWidget_2.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem10 = self.listWidget_2.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem11 = self.listWidget_2.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem12 = self.listWidget_2.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem13 = self.listWidget_2.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem14 = self.listWidget_2.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem15 = self.listWidget_2.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem16 = self.listWidget_2.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem17 = self.listWidget_2.item(17)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem18 = self.listWidget_2.item(18)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem19 = self.listWidget_2.item(19)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem20 = self.listWidget_2.item(20)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem21 = self.listWidget_2.item(21)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem22 = self.listWidget_2.item(22)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem23 = self.listWidget_2.item(23)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem24 = self.listWidget_2.item(24)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem25 = self.listWidget_2.item(25)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem26 = self.listWidget_2.item(26)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem27 = self.listWidget_2.item(27)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem28 = self.listWidget_2.item(28)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem29 = self.listWidget_2.item(29)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem30 = self.listWidget_2.item(30)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        self.listWidget_2.setSortingEnabled(__sortingEnabled)

        self.pushButton.setText(QCoreApplication.translate("Dialog", u"done", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"ReDo", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Reset", None))

        __sortingEnabled1 = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem31 = self.listWidget.item(0)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem32 = self.listWidget.item(1)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem33 = self.listWidget.item(2)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem34 = self.listWidget.item(3)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem35 = self.listWidget.item(4)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem36 = self.listWidget.item(5)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem37 = self.listWidget.item(6)
        ___qlistwidgetitem37.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem38 = self.listWidget.item(7)
        ___qlistwidgetitem38.setText(QCoreApplication.translate("Dialog", u"a", None));
        ___qlistwidgetitem39 = self.listWidget.item(8)
        ___qlistwidgetitem39.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem40 = self.listWidget.item(9)
        ___qlistwidgetitem40.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem41 = self.listWidget.item(10)
        ___qlistwidgetitem41.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem42 = self.listWidget.item(11)
        ___qlistwidgetitem42.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem43 = self.listWidget.item(12)
        ___qlistwidgetitem43.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem44 = self.listWidget.item(13)
        ___qlistwidgetitem44.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem45 = self.listWidget.item(14)
        ___qlistwidgetitem45.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem46 = self.listWidget.item(15)
        ___qlistwidgetitem46.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem47 = self.listWidget.item(16)
        ___qlistwidgetitem47.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem48 = self.listWidget.item(17)
        ___qlistwidgetitem48.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem49 = self.listWidget.item(18)
        ___qlistwidgetitem49.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem50 = self.listWidget.item(19)
        ___qlistwidgetitem50.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem51 = self.listWidget.item(20)
        ___qlistwidgetitem51.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem52 = self.listWidget.item(21)
        ___qlistwidgetitem52.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem53 = self.listWidget.item(22)
        ___qlistwidgetitem53.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem54 = self.listWidget.item(23)
        ___qlistwidgetitem54.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem55 = self.listWidget.item(24)
        ___qlistwidgetitem55.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem56 = self.listWidget.item(25)
        ___qlistwidgetitem56.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem57 = self.listWidget.item(26)
        ___qlistwidgetitem57.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem58 = self.listWidget.item(27)
        ___qlistwidgetitem58.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem59 = self.listWidget.item(28)
        ___qlistwidgetitem59.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem60 = self.listWidget.item(29)
        ___qlistwidgetitem60.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        ___qlistwidgetitem61 = self.listWidget.item(30)
        ___qlistwidgetitem61.setText(QCoreApplication.translate("Dialog", u"New Item", None));
        self.listWidget.setSortingEnabled(__sortingEnabled1)

    # retranslateUi

