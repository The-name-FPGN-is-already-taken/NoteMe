# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timetable.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1024, 640)
        Dialog.setMinimumSize(QSize(1024, 640))
        Dialog.setMaximumSize(QSize(1024, 640))
        self.topBar = QFrame(Dialog)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setGeometry(QRect(0, 0, 1024, 101))
        self.topBar.setStyleSheet(u"position: absolute;\n"
"width: 1024px;\n"
"height: 100px;\n"
"left: 0px;\n"
"top: 0px;\n"
"text-align: center;\n"
"\n"
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
"\n"
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
        font.setPointSize(1)

        font.setBold(False)
        font.setItalic(False)
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
        self.frame.setGeometry(QRect(90, 100, 941, 541))
        self.frame.setStyleSheet(u"background: #84B289;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.today_label = QLabel(self.frame)
        self.today_label.setObjectName(u"today_label")
        self.today_label.setGeometry(QRect(110, 90, 201, 51))
        font1 = QFont()
        font1.setFamilies([u"AvenirNext LT Pro Bold"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.today_label.setFont(font1)
        self.today_label.setStyleSheet(u";\n"
" \n"
"\n"
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
"border-radius: 15px;")

        self.horizontalLayout_3.addWidget(self.previous_button)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.monday_button_2 = QPushButton(self.layoutWidget_2)
        self.monday_button_2.setObjectName(u"monday_button_2")
        self.monday_button_2.setMaximumSize(QSize(93, 41))
        self.monday_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.monday_button_2.setStyleSheet(u";\n"
" \n"
"\n"
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
        self.tuesday_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.tuesday_button_2.setStyleSheet(u";\n"
" \n"
"\n"
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
        self.wednesday_button_2.setStyleSheet(u";\n"
" \n"
"\n"
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
        self.thursday_button_2.setStyleSheet(u";\n"
" \n"
"\n"
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
        self.friday_button_2.setStyleSheet(u";\n"
" \n"
"\n"
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
        self.saturday_button_2.setStyleSheet(u";\n"
" \n"
"\n"
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
        self.sunday_button_2.setStyleSheet(u";\n"
" \n"
"\n"
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
        self.today_label_2.setStyleSheet(u";\n"
" \n"
"\n"
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
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"background: #FEFAE0;")

        self.horizontalLayout.addWidget(self.listWidget)

        self.leftBar_2 = QFrame(Dialog)
        self.leftBar_2.setObjectName(u"leftBar_2")
        self.leftBar_2.setGeometry(QRect(0, 100, 91, 541))
        self.leftBar_2.setStyleSheet(u"\n"
"text-align: center;\n"
"position: absolute;\n"
"width: 140px;\n"
"height: 540px;\n"
"left: 0px;\n"
"top: 100px;\n"
"\n"
"background: #A3C5A7;")
        self.leftBar_2.setFrameShape(QFrame.StyledPanel)
        self.leftBar_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.leftBar_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.homeButton = QPushButton(self.leftBar_2)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeButton.setStyleSheet(u"position: absolute;\n"
"\n"
"image: url(D:/NotaProject/pics/home.png);\n"
"width: 120px;\n"
"height: 37px;\n"
"left: 7px;\n"
"top: 16px;\n"
"text-align: right;\n"
"      \n"
"background: #C4C4C4;\n"
"border: 1px solid #000000;\n"
"\n"
"border-radius: 10px;\n"
"")

        self.verticalLayout_11.addWidget(self.homeButton)

        self.home_label_2 = QLabel(self.leftBar_2)
        self.home_label_2.setObjectName(u"home_label_2")
        self.home_label_2.setStyleSheet(u"text-align: center;")

        self.verticalLayout_11.addWidget(self.home_label_2)


        self.verticalLayout_10.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.timeTableButton_2 = QPushButton(self.leftBar_2)
        self.timeTableButton_2.setObjectName(u"timeTableButton_2")
        self.timeTableButton_2.setCursor(QCursor(Qt.ArrowCursor))
        self.timeTableButton_2.setStyleSheet(u"image: url(D:/NotaProject/pics/timetable.png);\n"
"position: absolute;\n"
"width: 120px;\n"
"height: 37px;\n"
"left: 7px;\n"
"top: 160px;\n"
"text-align: right;\n"
"background: #ECF39E;\n"
"border-radius: 10px;\n"
"text-align: center;")

        self.verticalLayout_12.addWidget(self.timeTableButton_2)

        self.timeTable_label_2 = QLabel(self.leftBar_2)
        self.timeTable_label_2.setObjectName(u"timeTable_label_2")
        self.timeTable_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.timeTable_label_2)


        self.verticalLayout_10.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.noteButton = QPushButton(self.leftBar_2)
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
"border-radius: 10px;\n"
"border: 1px solid #000000;\n"
"")

        self.verticalLayout_13.addWidget(self.noteButton)

        self.note_label_2 = QLabel(self.leftBar_2)
        self.note_label_2.setObjectName(u"note_label_2")

        self.verticalLayout_13.addWidget(self.note_label_2)


        self.verticalLayout_10.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.taskButton = QPushButton(self.leftBar_2)
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
"border-radius: 10px;")

        self.verticalLayout_14.addWidget(self.taskButton)

        self.task_label_2 = QLabel(self.leftBar_2)
        self.task_label_2.setObjectName(u"task_label_2")

        self.verticalLayout_14.addWidget(self.task_label_2)


        self.verticalLayout_10.addLayout(self.verticalLayout_14)


        self.verticalLayout_9.addLayout(self.verticalLayout_10)

        self.frame_2 = QFrame(self.leftBar_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.addTimeTableButton = QPushButton(self.frame_2)
        self.addTimeTableButton.setObjectName(u"addTimeTableButton")
        self.addTimeTableButton.setGeometry(QRect(0, 90, 67, 61))
        self.addTimeTableButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addTimeTableButton.setFocusPolicy(Qt.ClickFocus)
        self.addTimeTableButton.setStyleSheet(u"background: rgba(0,0,0,0);\n"
"image: url(D:/NotaProject/pics/add.png);")

        self.verticalLayout_9.addWidget(self.frame_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
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
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"done", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"ReDo", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Reset", None))
#if QT_CONFIG(tooltip)
        self.homeButton.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/>home</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.homeButton.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>home</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.homeButton.setText("")
        self.home_label_2.setText(QCoreApplication.translate("Dialog", u"     HOME", None))
        self.timeTableButton_2.setText("")
        self.timeTable_label_2.setText(QCoreApplication.translate("Dialog", u" TIMETABLE", None))
        self.noteButton.setText("")
        self.note_label_2.setText(QCoreApplication.translate("Dialog", u"    NOTE", None))
        self.taskButton.setText("")
        self.task_label_2.setText(QCoreApplication.translate("Dialog", u"     TASK", None))
        self.addTimeTableButton.setText("")
    # retranslateUi

