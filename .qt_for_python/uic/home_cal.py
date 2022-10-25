# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_cal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import source_rc

class Ui_homeCal(object):
    def setupUi(self, homeCal):
        if not homeCal.objectName():
            homeCal.setObjectName(u"homeCal")
        homeCal.resize(1024, 640)
        homeCal.setMinimumSize(QSize(1024, 640))
        homeCal.setMaximumSize(QSize(1024, 640))
        self.backFrame = QFrame(homeCal)
        self.backFrame.setObjectName(u"backFrame")
        self.backFrame.setGeometry(QRect(0, 0, 1024, 640))
        self.backFrame.setFrameShape(QFrame.StyledPanel)
        self.backFrame.setFrameShadow(QFrame.Raised)
        self.topBar = QFrame(self.backFrame)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setGeometry(QRect(0, 0, 1024, 101))
        self.topBar.setStyleSheet(u"position: absolute;\n"
"width: 1024px;\n"
"height: 100px;\n"
"left: 0px;\n"
"top: 0px;\n"
"text-align: center;\n"
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
"      \n"
"border-radius: 35px;\n"
"")
        self.app_icon.setFrameShape(QFrame.StyledPanel)
        self.app_icon.setFrameShadow(QFrame.Raised)
        self.week_cal_switching_tab = QFrame(self.topBar)
        self.week_cal_switching_tab.setObjectName(u"week_cal_switching_tab")
        self.week_cal_switching_tab.setGeometry(QRect(820, 20, 181, 51))
        self.week_cal_switching_tab.setStyleSheet(u"\n"
"position: absolute;\n"
"width: 90px;\n"
"height: 50px;\n"
"left: 896px;\n"
"top: 31px;\n"
"\n"
"background: #E4E2C7;\n"
"border-radius: 15px;")
        self.week_cal_switching_tab.setFrameShape(QFrame.StyledPanel)
        self.week_cal_switching_tab.setFrameShadow(QFrame.Raised)
        self.weekView_tab = QPushButton(self.week_cal_switching_tab)
        self.weekView_tab.setObjectName(u"weekView_tab")
        self.weekView_tab.setGeometry(QRect(0, 0, 101, 51))
        self.weekView_tab.setCursor(QCursor(Qt.PointingHandCursor))
        self.weekView_tab.setStyleSheet(u"\n"
"\n"
"position: absolute;\n"
"width: 90px;\n"
"height: 50px;\n"
"left: 896px;\n"
"top: 31px;\n"
"\n"
"background: #E4E2C7;\n"
"border-radius: 15px;")
        self.calendar_tab = QLabel(self.week_cal_switching_tab)
        self.calendar_tab.setObjectName(u"calendar_tab")
        self.calendar_tab.setGeometry(QRect(90, 0, 91, 51))
        self.calendar_tab.setCursor(QCursor(Qt.ArrowCursor))
        self.calendar_tab.setStyleSheet(u"position: absolute;\n"
"width: 90px;\n"
"height: 50px;\n"
"left: 806px;\n"
"top: 31px;\n"
"text-align: center;\n"
"background: #84B289;\n"
"border-radius: 15px;")
        self.layoutWidget = QWidget(self.topBar)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 20, 551, 53))
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

        self.leftBar = QFrame(self.backFrame)
        self.leftBar.setObjectName(u"leftBar")
        self.leftBar.setGeometry(QRect(0, 100, 91, 551))
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
"background: #ECF39E;\n"
"      \n"
"border-radius: 10px;\n"
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
"background: #C4C4C4;\n"
"border: 1px solid #000000;\n"
"\n"
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
"\n"
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
"\n"
"border-radius: 10px;")

        self.verticalLayout_5.addWidget(self.taskButton)

        self.task_label = QLabel(self.leftBar)
        self.task_label.setObjectName(u"task_label")

        self.verticalLayout_5.addWidget(self.task_label)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.emptyFrameInLeftBar = QFrame(self.leftBar)
        self.emptyFrameInLeftBar.setObjectName(u"emptyFrameInLeftBar")
        self.emptyFrameInLeftBar.setFrameShape(QFrame.StyledPanel)
        self.emptyFrameInLeftBar.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.emptyFrameInLeftBar)

        self.signOutButton = QPushButton(self.leftBar)
        self.signOutButton.setObjectName(u"signOutButton")
        self.signOutButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.signOutButton.setStyleSheet(u"position: absolute;\n"
"width: 65px;\n"
"height: 40px;\n"
"left: 29px;\n"
"top: 346px;\n"
"background: #EC8E65;\n"
"border-radius: 15px;\n"
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

        self.frame_5 = QFrame(self.backFrame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(90, 100, 941, 541))
        self.frame_5.setStyleSheet(u"position: absolute;\n"
"width: 1024px;\n"
"height: 640px;\n"
"left: 0px;\n"
"top: 0px;\n"
"\n"
"background: #84B289;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(30, 10, 871, 61))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.layoutWidget1 = QWidget(self.frame_7)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 871, 45))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.previous_button = QPushButton(self.layoutWidget1)
        self.previous_button.setObjectName(u"previous_button")
        self.previous_button.setMaximumSize(QSize(51, 31))
        self.previous_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.previous_button.setStyleSheet(u"image: url(D:/NotaProject/pics/left-arrow.png);\n"
"position: absolute;\n"
"width: 90px;\n"
"height: 50px;\n"
"left: 806px;\n"
"top: 31px;\n"
"text-align: center;\n"
"background: #84B289;\n"
"border-radius: 15px;\n"
"")

        self.horizontalLayout_3.addWidget(self.previous_button)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.month1_button = QPushButton(self.layoutWidget1)
        self.month1_button.setObjectName(u"month1_button")
        self.month1_button.setMaximumSize(QSize(93, 41))
        self.month1_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.month1_button.setStyleSheet(u";\n"
"        \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_2.addWidget(self.month1_button)

        self.month2_button = QPushButton(self.layoutWidget1)
        self.month2_button.setObjectName(u"month2_button")
        self.month2_button.setMaximumSize(QSize(93, 41))
        self.month2_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.month2_button.setStyleSheet(u";\n"
"        \n"
" \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.month2_button)

        self.month3_button = QPushButton(self.layoutWidget1)
        self.month3_button.setObjectName(u"month3_button")
        self.month3_button.setMaximumSize(QSize(93, 41))
        self.month3_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.month3_button.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_2.addWidget(self.month3_button)

        self.month4_button = QPushButton(self.layoutWidget1)
        self.month4_button.setObjectName(u"month4_button")
        self.month4_button.setMaximumSize(QSize(93, 41))
        self.month4_button.setCursor(QCursor(Qt.ArrowCursor))
        self.month4_button.setStyleSheet(u";\n"
"        \n"
"    \n"
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

        self.horizontalLayout_2.addWidget(self.month4_button)

        self.month5_button = QPushButton(self.layoutWidget1)
        self.month5_button.setObjectName(u"month5_button")
        self.month5_button.setMaximumSize(QSize(93, 41))
        self.month5_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.month5_button.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_2.addWidget(self.month5_button)

        self.month6_button = QPushButton(self.layoutWidget1)
        self.month6_button.setObjectName(u"month6_button")
        self.month6_button.setMaximumSize(QSize(93, 41))
        self.month6_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.month6_button.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_2.addWidget(self.month6_button)

        self.month7_button = QPushButton(self.layoutWidget1)
        self.month7_button.setObjectName(u"month7_button")
        self.month7_button.setMaximumSize(QSize(93, 41))
        self.month7_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.month7_button.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_2.addWidget(self.month7_button)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.next_button = QPushButton(self.layoutWidget1)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setMaximumSize(QSize(51, 31))
        self.next_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_button.setStyleSheet(u"image: url(D:/NotaProject/pics/right-arrow.png);\n"
"position: absolute;\n"
"width: 90px;\n"
"height: 50px;\n"
"left: 806px;\n"
"top: 31px;\n"
"text-align: center;\n"
"background: #84B289;\n"
"border-radius: 15px;")

        self.horizontalLayout_3.addWidget(self.next_button)

        self.task_tray = QScrollArea(self.frame_5)
        self.task_tray.setObjectName(u"task_tray")
        self.task_tray.setGeometry(QRect(30, 310, 871, 191))
        self.task_tray.setStyleSheet(u"\n"
"position: absolute;\n"
"width: 120px;\n"
"height: 37px;\n"
"left: 7px;\n"
"top: 16px;\n"
"\n"
"background: #00FFFFFF;\n"
"      \n"
"border-radius: 10px;")
        self.task_tray.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 871, 191))
        self.today_container = QFrame(self.scrollAreaWidgetContents)
        self.today_container.setObjectName(u"today_container")
        self.today_container.setGeometry(QRect(0, 40, 871, 31))
        self.today_container.setFrameShape(QFrame.StyledPanel)
        self.today_container.setFrameShadow(QFrame.Raised)
        self.today_label = QLabel(self.today_container)
        self.today_label.setObjectName(u"today_label")
        self.today_label.setGeometry(QRect(10, 0, 61, 21))
        font1 = QFont()
        font1.setFamily(u"AvenirNext LT Pro Bold")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.today_label.setFont(font1)
        self.task_tray.setWidget(self.scrollAreaWidgetContents)
        self.layoutWidget2 = QWidget(self.frame_5)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(110, 60, 704, 355))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(70)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tuesday_button_3 = QPushButton(self.layoutWidget2)
        self.tuesday_button_3.setObjectName(u"tuesday_button_3")
        self.tuesday_button_3.setMaximumSize(QSize(93, 41))
        self.tuesday_button_3.setCursor(QCursor(Qt.ArrowCursor))
        self.tuesday_button_3.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199,0);\n"
"border-radius: 8px;\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.tuesday_button_3)

        self.monday_button_3 = QPushButton(self.layoutWidget2)
        self.monday_button_3.setObjectName(u"monday_button_3")
        self.monday_button_3.setMaximumSize(QSize(93, 41))
        self.monday_button_3.setCursor(QCursor(Qt.ArrowCursor))
        self.monday_button_3.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199,0);\n"
"border-radius: 8px;\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.monday_button_3)

        self.wednesday_button_3 = QPushButton(self.layoutWidget2)
        self.wednesday_button_3.setObjectName(u"wednesday_button_3")
        self.wednesday_button_3.setMaximumSize(QSize(93, 41))
        self.wednesday_button_3.setCursor(QCursor(Qt.ArrowCursor))
        self.wednesday_button_3.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199,0);\n"
"border-radius: 8px;\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.wednesday_button_3)

        self.thursday_button_3 = QPushButton(self.layoutWidget2)
        self.thursday_button_3.setObjectName(u"thursday_button_3")
        self.thursday_button_3.setMaximumSize(QSize(93, 41))
        self.thursday_button_3.setCursor(QCursor(Qt.ArrowCursor))
        self.thursday_button_3.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199,0);\n"
"border-radius: 8px;\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.thursday_button_3)

        self.friday_button_3 = QPushButton(self.layoutWidget2)
        self.friday_button_3.setObjectName(u"friday_button_3")
        self.friday_button_3.setMaximumSize(QSize(93, 41))
        self.friday_button_3.setCursor(QCursor(Qt.ArrowCursor))
        self.friday_button_3.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199,0);\n"
"border-radius: 8px;\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.friday_button_3)

        self.saturday_button_3 = QPushButton(self.layoutWidget2)
        self.saturday_button_3.setObjectName(u"saturday_button_3")
        self.saturday_button_3.setMaximumSize(QSize(93, 41))
        self.saturday_button_3.setCursor(QCursor(Qt.ArrowCursor))
        self.saturday_button_3.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199,0);\n"
"border-radius: 8px;\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.saturday_button_3)

        self.sunday_button_3 = QPushButton(self.layoutWidget2)
        self.sunday_button_3.setObjectName(u"sunday_button_3")
        self.sunday_button_3.setMaximumSize(QSize(93, 41))
        self.sunday_button_3.setCursor(QCursor(Qt.ArrowCursor))
        self.sunday_button_3.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199,0);\n"
"border-radius: 8px;\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.sunday_button_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.line = QFrame(self.layoutWidget2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(70)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tuesday_button_4 = QPushButton(self.layoutWidget2)
        self.tuesday_button_4.setObjectName(u"tuesday_button_4")
        self.tuesday_button_4.setMaximumSize(QSize(93, 41))
        self.tuesday_button_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.tuesday_button_4.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.tuesday_button_4)

        self.monday_button_4 = QPushButton(self.layoutWidget2)
        self.monday_button_4.setObjectName(u"monday_button_4")
        self.monday_button_4.setMaximumSize(QSize(93, 41))
        self.monday_button_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.monday_button_4.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_6.addWidget(self.monday_button_4)

        self.wednesday_button_4 = QPushButton(self.layoutWidget2)
        self.wednesday_button_4.setObjectName(u"wednesday_button_4")
        self.wednesday_button_4.setMaximumSize(QSize(93, 41))
        self.wednesday_button_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.wednesday_button_4.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_6.addWidget(self.wednesday_button_4)

        self.thursday_button_4 = QPushButton(self.layoutWidget2)
        self.thursday_button_4.setObjectName(u"thursday_button_4")
        self.thursday_button_4.setMaximumSize(QSize(93, 41))
        self.thursday_button_4.setCursor(QCursor(Qt.ArrowCursor))
        self.thursday_button_4.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_6.addWidget(self.thursday_button_4)

        self.friday_button_4 = QPushButton(self.layoutWidget2)
        self.friday_button_4.setObjectName(u"friday_button_4")
        self.friday_button_4.setMaximumSize(QSize(93, 41))
        self.friday_button_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.friday_button_4.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_6.addWidget(self.friday_button_4)

        self.saturday_button_4 = QPushButton(self.layoutWidget2)
        self.saturday_button_4.setObjectName(u"saturday_button_4")
        self.saturday_button_4.setMaximumSize(QSize(93, 41))
        self.saturday_button_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.saturday_button_4.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_6.addWidget(self.saturday_button_4)

        self.sunday_button_4 = QPushButton(self.layoutWidget2)
        self.sunday_button_4.setObjectName(u"sunday_button_4")
        self.sunday_button_4.setMaximumSize(QSize(93, 41))
        self.sunday_button_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.sunday_button_4.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_6.addWidget(self.sunday_button_4)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(70)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tuesday_button_5 = QPushButton(self.layoutWidget2)
        self.tuesday_button_5.setObjectName(u"tuesday_button_5")
        self.tuesday_button_5.setMaximumSize(QSize(93, 41))
        self.tuesday_button_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.tuesday_button_5.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.tuesday_button_5)

        self.monday_button_5 = QPushButton(self.layoutWidget2)
        self.monday_button_5.setObjectName(u"monday_button_5")
        self.monday_button_5.setMaximumSize(QSize(93, 41))
        self.monday_button_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.monday_button_5.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_7.addWidget(self.monday_button_5)

        self.wednesday_button_5 = QPushButton(self.layoutWidget2)
        self.wednesday_button_5.setObjectName(u"wednesday_button_5")
        self.wednesday_button_5.setMaximumSize(QSize(93, 41))
        self.wednesday_button_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.wednesday_button_5.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_7.addWidget(self.wednesday_button_5)

        self.thursday_button_5 = QPushButton(self.layoutWidget2)
        self.thursday_button_5.setObjectName(u"thursday_button_5")
        self.thursday_button_5.setMaximumSize(QSize(93, 41))
        self.thursday_button_5.setCursor(QCursor(Qt.ArrowCursor))
        self.thursday_button_5.setStyleSheet(u";\n"
"        \n"
"    \n"
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

        self.horizontalLayout_7.addWidget(self.thursday_button_5)

        self.friday_button_5 = QPushButton(self.layoutWidget2)
        self.friday_button_5.setObjectName(u"friday_button_5")
        self.friday_button_5.setMaximumSize(QSize(93, 41))
        self.friday_button_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.friday_button_5.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_7.addWidget(self.friday_button_5)

        self.saturday_button_5 = QPushButton(self.layoutWidget2)
        self.saturday_button_5.setObjectName(u"saturday_button_5")
        self.saturday_button_5.setMaximumSize(QSize(93, 41))
        self.saturday_button_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.saturday_button_5.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_7.addWidget(self.saturday_button_5)

        self.sunday_button_5 = QPushButton(self.layoutWidget2)
        self.sunday_button_5.setObjectName(u"sunday_button_5")
        self.sunday_button_5.setMaximumSize(QSize(93, 41))
        self.sunday_button_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.sunday_button_5.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_7.addWidget(self.sunday_button_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(70)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tuesday_button_6 = QPushButton(self.layoutWidget2)
        self.tuesday_button_6.setObjectName(u"tuesday_button_6")
        self.tuesday_button_6.setMaximumSize(QSize(93, 41))
        self.tuesday_button_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.tuesday_button_6.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;\n"
"\n"
"")

        self.horizontalLayout_8.addWidget(self.tuesday_button_6)

        self.monday_button_6 = QPushButton(self.layoutWidget2)
        self.monday_button_6.setObjectName(u"monday_button_6")
        self.monday_button_6.setMaximumSize(QSize(93, 41))
        self.monday_button_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.monday_button_6.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_8.addWidget(self.monday_button_6)

        self.wednesday_button_6 = QPushButton(self.layoutWidget2)
        self.wednesday_button_6.setObjectName(u"wednesday_button_6")
        self.wednesday_button_6.setMaximumSize(QSize(93, 41))
        self.wednesday_button_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.wednesday_button_6.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_8.addWidget(self.wednesday_button_6)

        self.thursday_button_6 = QPushButton(self.layoutWidget2)
        self.thursday_button_6.setObjectName(u"thursday_button_6")
        self.thursday_button_6.setMaximumSize(QSize(93, 41))
        self.thursday_button_6.setCursor(QCursor(Qt.ArrowCursor))
        self.thursday_button_6.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_8.addWidget(self.thursday_button_6)

        self.friday_button_6 = QPushButton(self.layoutWidget2)
        self.friday_button_6.setObjectName(u"friday_button_6")
        self.friday_button_6.setMaximumSize(QSize(93, 41))
        self.friday_button_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.friday_button_6.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_8.addWidget(self.friday_button_6)

        self.saturday_button_6 = QPushButton(self.layoutWidget2)
        self.saturday_button_6.setObjectName(u"saturday_button_6")
        self.saturday_button_6.setMaximumSize(QSize(93, 41))
        self.saturday_button_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.saturday_button_6.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_8.addWidget(self.saturday_button_6)

        self.sunday_button_6 = QPushButton(self.layoutWidget2)
        self.sunday_button_6.setObjectName(u"sunday_button_6")
        self.sunday_button_6.setMaximumSize(QSize(93, 41))
        self.sunday_button_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.sunday_button_6.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_8.addWidget(self.sunday_button_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(70)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.tuesday_button_8 = QPushButton(self.layoutWidget2)
        self.tuesday_button_8.setObjectName(u"tuesday_button_8")
        self.tuesday_button_8.setMaximumSize(QSize(93, 41))
        self.tuesday_button_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.tuesday_button_8.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;\n"
"\n"
"")

        self.horizontalLayout_10.addWidget(self.tuesday_button_8)

        self.monday_button_8 = QPushButton(self.layoutWidget2)
        self.monday_button_8.setObjectName(u"monday_button_8")
        self.monday_button_8.setMaximumSize(QSize(93, 41))
        self.monday_button_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.monday_button_8.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_10.addWidget(self.monday_button_8)

        self.wednesday_button_8 = QPushButton(self.layoutWidget2)
        self.wednesday_button_8.setObjectName(u"wednesday_button_8")
        self.wednesday_button_8.setMaximumSize(QSize(93, 41))
        self.wednesday_button_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.wednesday_button_8.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_10.addWidget(self.wednesday_button_8)

        self.thursday_button_8 = QPushButton(self.layoutWidget2)
        self.thursday_button_8.setObjectName(u"thursday_button_8")
        self.thursday_button_8.setMaximumSize(QSize(93, 41))
        self.thursday_button_8.setCursor(QCursor(Qt.ArrowCursor))
        self.thursday_button_8.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_10.addWidget(self.thursday_button_8)

        self.friday_button_8 = QPushButton(self.layoutWidget2)
        self.friday_button_8.setObjectName(u"friday_button_8")
        self.friday_button_8.setMaximumSize(QSize(93, 41))
        self.friday_button_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.friday_button_8.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_10.addWidget(self.friday_button_8)

        self.saturday_button_8 = QPushButton(self.layoutWidget2)
        self.saturday_button_8.setObjectName(u"saturday_button_8")
        self.saturday_button_8.setMaximumSize(QSize(93, 41))
        self.saturday_button_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.saturday_button_8.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_10.addWidget(self.saturday_button_8)

        self.sunday_button_8 = QPushButton(self.layoutWidget2)
        self.sunday_button_8.setObjectName(u"sunday_button_8")
        self.sunday_button_8.setMaximumSize(QSize(93, 41))
        self.sunday_button_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.sunday_button_8.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_10.addWidget(self.sunday_button_8)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(70)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.tuesday_button_10 = QPushButton(self.layoutWidget2)
        self.tuesday_button_10.setObjectName(u"tuesday_button_10")
        self.tuesday_button_10.setMaximumSize(QSize(93, 41))
        self.tuesday_button_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.tuesday_button_10.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;\n"
"\n"
"")

        self.horizontalLayout_12.addWidget(self.tuesday_button_10)

        self.monday_button_10 = QPushButton(self.layoutWidget2)
        self.monday_button_10.setObjectName(u"monday_button_10")
        self.monday_button_10.setMaximumSize(QSize(93, 41))
        self.monday_button_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.monday_button_10.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_12.addWidget(self.monday_button_10)

        self.wednesday_button_10 = QPushButton(self.layoutWidget2)
        self.wednesday_button_10.setObjectName(u"wednesday_button_10")
        self.wednesday_button_10.setMaximumSize(QSize(93, 41))
        self.wednesday_button_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.wednesday_button_10.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_12.addWidget(self.wednesday_button_10)

        self.thursday_button_10 = QPushButton(self.layoutWidget2)
        self.thursday_button_10.setObjectName(u"thursday_button_10")
        self.thursday_button_10.setMaximumSize(QSize(93, 41))
        self.thursday_button_10.setCursor(QCursor(Qt.ArrowCursor))
        self.thursday_button_10.setStyleSheet(u";\n"
"        \n"
"    \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_12.addWidget(self.thursday_button_10)

        self.friday_button_10 = QPushButton(self.layoutWidget2)
        self.friday_button_10.setObjectName(u"friday_button_10")
        self.friday_button_10.setMaximumSize(QSize(93, 41))
        self.friday_button_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.friday_button_10.setStyleSheet(u";\n"
"        \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_12.addWidget(self.friday_button_10)

        self.saturday_button_10 = QPushButton(self.layoutWidget2)
        self.saturday_button_10.setObjectName(u"saturday_button_10")
        self.saturday_button_10.setMaximumSize(QSize(93, 41))
        self.saturday_button_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.saturday_button_10.setStyleSheet(u";\n"
"        \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_12.addWidget(self.saturday_button_10)

        self.sunday_button_10 = QPushButton(self.layoutWidget2)
        self.sunday_button_10.setObjectName(u"sunday_button_10")
        self.sunday_button_10.setMaximumSize(QSize(93, 41))
        self.sunday_button_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.sunday_button_10.setStyleSheet(u";\n"
"        \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_12.addWidget(self.sunday_button_10)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(70)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tuesday_button_9 = QPushButton(self.layoutWidget2)
        self.tuesday_button_9.setObjectName(u"tuesday_button_9")
        self.tuesday_button_9.setMaximumSize(QSize(93, 41))
        self.tuesday_button_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.tuesday_button_9.setStyleSheet(u";\n"
"        \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;\n"
"\n"
"")

        self.horizontalLayout_11.addWidget(self.tuesday_button_9)

        self.monday_button_9 = QPushButton(self.layoutWidget2)
        self.monday_button_9.setObjectName(u"monday_button_9")
        self.monday_button_9.setMaximumSize(QSize(93, 41))
        self.monday_button_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.monday_button_9.setStyleSheet(u";\n"
"        \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_11.addWidget(self.monday_button_9)

        self.wednesday_button_9 = QPushButton(self.layoutWidget2)
        self.wednesday_button_9.setObjectName(u"wednesday_button_9")
        self.wednesday_button_9.setMaximumSize(QSize(93, 41))
        self.wednesday_button_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.wednesday_button_9.setStyleSheet(u";\n"
"        \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_11.addWidget(self.wednesday_button_9)

        self.thursday_button_9 = QPushButton(self.layoutWidget2)
        self.thursday_button_9.setObjectName(u"thursday_button_9")
        self.thursday_button_9.setMaximumSize(QSize(93, 41))
        self.thursday_button_9.setCursor(QCursor(Qt.ArrowCursor))
        self.thursday_button_9.setStyleSheet(u";\n"
"        \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_11.addWidget(self.thursday_button_9)

        self.friday_button_9 = QPushButton(self.layoutWidget2)
        self.friday_button_9.setObjectName(u"friday_button_9")
        self.friday_button_9.setMaximumSize(QSize(93, 41))
        self.friday_button_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.friday_button_9.setStyleSheet(u";\n"
"        \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_11.addWidget(self.friday_button_9)

        self.saturday_button_9 = QPushButton(self.layoutWidget2)
        self.saturday_button_9.setObjectName(u"saturday_button_9")
        self.saturday_button_9.setMaximumSize(QSize(93, 41))
        self.saturday_button_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.saturday_button_9.setStyleSheet(u";\n"
"        \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_11.addWidget(self.saturday_button_9)

        self.sunday_button_9 = QPushButton(self.layoutWidget2)
        self.sunday_button_9.setObjectName(u"sunday_button_9")
        self.sunday_button_9.setMaximumSize(QSize(93, 41))
        self.sunday_button_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.sunday_button_9.setStyleSheet(u";\n"
"        \n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_11.addWidget(self.sunday_button_9)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.layoutWidget3 = QWidget(homeCal)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.retranslateUi(homeCal)

        QMetaObject.connectSlotsByName(homeCal)
    # setupUi

    def retranslateUi(self, homeCal):
        homeCal.setWindowTitle(QCoreApplication.translate("homeCal", u"Form", None))
        self.weekView_tab.setText(QCoreApplication.translate("homeCal", u"  WEEK", None))
        self.calendar_tab.setText(QCoreApplication.translate("homeCal", u"    CALENDAR", None))
        self.welcomeUser.setText(QCoreApplication.translate("homeCal", u"Welcome,", None))
        self.date.setText(QCoreApplication.translate("homeCal", u"November 21, 2021", None))
#if QT_CONFIG(tooltip)
        self.homeButton.setToolTip(QCoreApplication.translate("homeCal", u"<html><head/><body><p><br/>home</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.homeButton.setWhatsThis(QCoreApplication.translate("homeCal", u"<html><head/><body><p>home</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.homeButton.setText("")
        self.home_label.setText(QCoreApplication.translate("homeCal", u"     HOME", None))
        self.timeTableButton.setText("")
        self.timeTable_label.setText(QCoreApplication.translate("homeCal", u"TIMETABLE", None))
        self.noteButton.setText("")
        self.note_label.setText(QCoreApplication.translate("homeCal", u"    NOTE", None))
        self.taskButton.setText("")
        self.task_label.setText(QCoreApplication.translate("homeCal", u"    TASK", None))
        self.signOutButton.setText(QCoreApplication.translate("homeCal", u"SIGN OUT", None))
        self.previous_button.setText("")
        self.month1_button.setText(QCoreApplication.translate("homeCal", u"AUG", None))
        self.month2_button.setText(QCoreApplication.translate("homeCal", u"SEP", None))
        self.month3_button.setText(QCoreApplication.translate("homeCal", u"OCT", None))
        self.month4_button.setText(QCoreApplication.translate("homeCal", u"NOV", None))
        self.month5_button.setText(QCoreApplication.translate("homeCal", u"DEC", None))
        self.month6_button.setText(QCoreApplication.translate("homeCal", u"JAN", None))
        self.month7_button.setText(QCoreApplication.translate("homeCal", u"FEB", None))
        self.next_button.setText("")
        self.today_label.setText(QCoreApplication.translate("homeCal", u"Today", None))
        self.tuesday_button_3.setText(QCoreApplication.translate("homeCal", u"M", None))
        self.monday_button_3.setText(QCoreApplication.translate("homeCal", u"T", None))
        self.wednesday_button_3.setText(QCoreApplication.translate("homeCal", u"W", None))
        self.thursday_button_3.setText(QCoreApplication.translate("homeCal", u"T", None))
        self.friday_button_3.setText(QCoreApplication.translate("homeCal", u"F", None))
        self.saturday_button_3.setText(QCoreApplication.translate("homeCal", u"S", None))
        self.sunday_button_3.setText(QCoreApplication.translate("homeCal", u"S", None))
        self.tuesday_button_4.setText(QCoreApplication.translate("homeCal", u"26", None))
        self.monday_button_4.setText(QCoreApplication.translate("homeCal", u"27", None))
        self.wednesday_button_4.setText(QCoreApplication.translate("homeCal", u"28", None))
        self.thursday_button_4.setText(QCoreApplication.translate("homeCal", u"29", None))
        self.friday_button_4.setText(QCoreApplication.translate("homeCal", u"30", None))
        self.saturday_button_4.setText(QCoreApplication.translate("homeCal", u"31", None))
        self.sunday_button_4.setText(QCoreApplication.translate("homeCal", u"1", None))
        self.tuesday_button_5.setText(QCoreApplication.translate("homeCal", u"26", None))
        self.monday_button_5.setText(QCoreApplication.translate("homeCal", u"27", None))
        self.wednesday_button_5.setText(QCoreApplication.translate("homeCal", u"28", None))
        self.thursday_button_5.setText(QCoreApplication.translate("homeCal", u"29", None))
        self.friday_button_5.setText(QCoreApplication.translate("homeCal", u"30", None))
        self.saturday_button_5.setText(QCoreApplication.translate("homeCal", u"31", None))
        self.sunday_button_5.setText(QCoreApplication.translate("homeCal", u"1", None))
        self.tuesday_button_6.setText(QCoreApplication.translate("homeCal", u"26", None))
        self.monday_button_6.setText(QCoreApplication.translate("homeCal", u"27", None))
        self.wednesday_button_6.setText(QCoreApplication.translate("homeCal", u"28", None))
        self.thursday_button_6.setText(QCoreApplication.translate("homeCal", u"29", None))
        self.friday_button_6.setText(QCoreApplication.translate("homeCal", u"30", None))
        self.saturday_button_6.setText(QCoreApplication.translate("homeCal", u"31", None))
        self.sunday_button_6.setText(QCoreApplication.translate("homeCal", u"1", None))
        self.tuesday_button_8.setText(QCoreApplication.translate("homeCal", u"26", None))
        self.monday_button_8.setText(QCoreApplication.translate("homeCal", u"27", None))
        self.wednesday_button_8.setText(QCoreApplication.translate("homeCal", u"28", None))
        self.thursday_button_8.setText(QCoreApplication.translate("homeCal", u"29", None))
        self.friday_button_8.setText(QCoreApplication.translate("homeCal", u"30", None))
        self.saturday_button_8.setText(QCoreApplication.translate("homeCal", u"31", None))
        self.sunday_button_8.setText(QCoreApplication.translate("homeCal", u"1", None))
        self.tuesday_button_10.setText(QCoreApplication.translate("homeCal", u"26", None))
        self.monday_button_10.setText(QCoreApplication.translate("homeCal", u"27", None))
        self.wednesday_button_10.setText(QCoreApplication.translate("homeCal", u"28", None))
        self.thursday_button_10.setText(QCoreApplication.translate("homeCal", u"29", None))
        self.friday_button_10.setText(QCoreApplication.translate("homeCal", u"30", None))
        self.saturday_button_10.setText(QCoreApplication.translate("homeCal", u"31", None))
        self.sunday_button_10.setText(QCoreApplication.translate("homeCal", u"1", None))
        self.tuesday_button_9.setText(QCoreApplication.translate("homeCal", u"26", None))
        self.monday_button_9.setText(QCoreApplication.translate("homeCal", u"27", None))
        self.wednesday_button_9.setText(QCoreApplication.translate("homeCal", u"28", None))
        self.thursday_button_9.setText(QCoreApplication.translate("homeCal", u"29", None))
        self.friday_button_9.setText(QCoreApplication.translate("homeCal", u"30", None))
        self.saturday_button_9.setText(QCoreApplication.translate("homeCal", u"31", None))
        self.sunday_button_9.setText(QCoreApplication.translate("homeCal", u"1", None))
    # retranslateUi

