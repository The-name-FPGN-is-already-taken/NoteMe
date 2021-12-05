# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Timetableadd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_timetabledialog(object):
    def setupUi(self, timetabledialog):
        if not timetabledialog.objectName():
            timetabledialog.setObjectName(u"timetabledialog")
        timetabledialog.resize(1024, 640)
        timetabledialog.setMinimumSize(QSize(1024, 640))
        timetabledialog.setMaximumSize(QSize(1920, 1080))
        self.backFrame = QFrame(timetabledialog)
        self.backFrame.setObjectName(u"backFrame")
        self.backFrame.setGeometry(QRect(0, 0, 1024, 640))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backFrame.sizePolicy().hasHeightForWidth())
        self.backFrame.setSizePolicy(sizePolicy)
        self.backFrame.setMaximumSize(QSize(1920, 1080))
        self.backFrame.setFrameShape(QFrame.StyledPanel)
        self.backFrame.setFrameShadow(QFrame.Raised)
        self.topBar = QFrame(self.backFrame)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setGeometry(QRect(0, 0, 1024, 101))
        sizePolicy.setHeightForWidth(self.topBar.sizePolicy().hasHeightForWidth())
        self.topBar.setSizePolicy(sizePolicy)
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
"\n"
"border-radius: 35px;\n"
"")
        self.app_icon.setFrameShape(QFrame.StyledPanel)
        self.app_icon.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.topBar)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 20, 521, 53))
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
        self.layoutWidget_2 = QWidget(self.frame_5)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(670, 480, 209, 52))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cancelTimetableButton = QPushButton(self.layoutWidget_2)
        self.cancelTimetableButton.setObjectName(u"cancelTimetableButton")
        self.cancelTimetableButton.setMaximumSize(QSize(100, 50))
        self.cancelTimetableButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelTimetableButton.setStyleSheet(u"\n"
"background: #EC8E65;\n"
"border-radius: 15px;")

        self.horizontalLayout_2.addWidget(self.cancelTimetableButton)

        self.saveTimetableButton = QPushButton(self.layoutWidget_2)
        self.saveTimetableButton.setObjectName(u"saveTimetableButton")
        self.saveTimetableButton.setMaximumSize(QSize(100, 50))
        self.saveTimetableButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveTimetableButton.setStyleSheet(u"\n"
"background: #C6D57E;\n"
"border-radius: 15px;")

        self.horizontalLayout_2.addWidget(self.saveTimetableButton)

        self.widget = QWidget(self.frame_5)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 90, 821, 381))
        self.widget.setStyleSheet(u"background: #E4E2C7;\n"
"\n"
"\n"
"")
        self.timetabletitleName_textEdit = QTextEdit(self.widget)
        self.timetabletitleName_textEdit.setObjectName(u"timetabletitleName_textEdit")
        self.timetabletitleName_textEdit.setGeometry(QRect(70, 30, 361, 31))
        self.timetabletitleName_textEdit.setMaximumSize(QSize(759, 50))
        self.timetabletitleName_textEdit.setStyleSheet(u"background: rgba(0,0,0,0);\n"
"border-radius: 10px;\n"
"background-color: rgb(244, 255, 228);\n"
"color: rgb(88, 105, 82);")
        self.timetable_description = QTextEdit(self.widget)
        self.timetable_description.setObjectName(u"timetable_description")
        self.timetable_description.setGeometry(QRect(50, 90, 731, 261))
        self.timetable_description.setStyleSheet(u"background: rgba(0,0,0,0);\n"
"border-radius: 10px;\n"
"background-color: rgb(244, 255, 228);\n"
"color: rgb(88, 105, 82);")
        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(60, 70, 721, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.timetable_Edittime = QTimeEdit(self.widget)
        self.timetable_Edittime.setObjectName(u"timetable_Edittime")
        self.timetable_Edittime.setGeometry(QRect(670, 30, 91, 31))
        self.timetable_Edittime.setStyleSheet(u"background: rgba(0,0,0,0);\n"
"border-radius: 10px;\n"
"background-color: rgb(244, 255, 228);\n"
"color: rgb(88, 105, 82);")
        self.layoutWidget_3 = QWidget(self.frame_5)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(80, 30, 753, 43))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.monday_button_Repeat = QPushButton(self.layoutWidget_3)
        self.monday_button_Repeat.setObjectName(u"monday_button_Repeat")
        self.monday_button_Repeat.setMaximumSize(QSize(93, 41))
        self.monday_button_Repeat.setCursor(QCursor(Qt.PointingHandCursor))
        self.monday_button_Repeat.setStyleSheet(u";\n"
"  \n"
"\n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_6.addWidget(self.monday_button_Repeat)

        self.tuesday_button_Repeat = QPushButton(self.layoutWidget_3)
        self.tuesday_button_Repeat.setObjectName(u"tuesday_button_Repeat")
        self.tuesday_button_Repeat.setMaximumSize(QSize(93, 41))
        self.tuesday_button_Repeat.setCursor(QCursor(Qt.PointingHandCursor))
        self.tuesday_button_Repeat.setStyleSheet(u";\n"
"  \n"
"\n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_6.addWidget(self.tuesday_button_Repeat)

        self.wednesday_Repeat = QPushButton(self.layoutWidget_3)
        self.wednesday_Repeat.setObjectName(u"wednesday_Repeat")
        self.wednesday_Repeat.setMaximumSize(QSize(93, 41))
        self.wednesday_Repeat.setCursor(QCursor(Qt.PointingHandCursor))
        self.wednesday_Repeat.setStyleSheet(u";\n"
"  \n"
"\n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_6.addWidget(self.wednesday_Repeat)

        self.thursday_Repeat = QPushButton(self.layoutWidget_3)
        self.thursday_Repeat.setObjectName(u"thursday_Repeat")
        self.thursday_Repeat.setMaximumSize(QSize(93, 41))
        self.thursday_Repeat.setCursor(QCursor(Qt.PointingHandCursor))
        self.thursday_Repeat.setStyleSheet(u";\n"
"  \n"
"\n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_6.addWidget(self.thursday_Repeat)

        self.friday_button_Repeat = QPushButton(self.layoutWidget_3)
        self.friday_button_Repeat.setObjectName(u"friday_button_Repeat")
        self.friday_button_Repeat.setMaximumSize(QSize(93, 41))
        self.friday_button_Repeat.setCursor(QCursor(Qt.PointingHandCursor))
        self.friday_button_Repeat.setStyleSheet(u";\n"
"  \n"
"\n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_6.addWidget(self.friday_button_Repeat)

        self.saturday_button_Repeat = QPushButton(self.layoutWidget_3)
        self.saturday_button_Repeat.setObjectName(u"saturday_button_Repeat")
        self.saturday_button_Repeat.setMaximumSize(QSize(93, 41))
        self.saturday_button_Repeat.setCursor(QCursor(Qt.PointingHandCursor))
        self.saturday_button_Repeat.setStyleSheet(u";\n"
"  \n"
"\n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_6.addWidget(self.saturday_button_Repeat)

        self.sunday_button_Repeat = QPushButton(self.layoutWidget_3)
        self.sunday_button_Repeat.setObjectName(u"sunday_button_Repeat")
        self.sunday_button_Repeat.setMaximumSize(QSize(93, 41))
        self.sunday_button_Repeat.setCursor(QCursor(Qt.PointingHandCursor))
        self.sunday_button_Repeat.setStyleSheet(u";\n"
"  \n"
"\n"
"padding: 8px 0px;\n"
"position: static;\n"
"width: 40px;\n"
"left: calc(50% - 40px/2 - 189.71px);\n"
"top: 0%;\n"
"bottom: 0%;\n"
"background-color: rgb(228, 226, 199);\n"
"border-radius: 8px;")

        self.horizontalLayout_6.addWidget(self.sunday_button_Repeat)

        self.widget.raise_()
        self.layoutWidget_2.raise_()
        self.layoutWidget_3.raise_()
        self.leftBar = QFrame(self.backFrame)
        self.leftBar.setObjectName(u"leftBar")
        self.leftBar.setGeometry(QRect(0, 100, 91, 541))
        self.leftBar.setStyleSheet(u"\n"
"text-align: center;\n"
"position: absolute;\n"
"width: 140px;\n"
"height: 540px;\n"
"left: 0px;\n"
"top: 100px;\n"
"\n"
"background: #A3C5A7;")
        self.leftBar.setFrameShape(QFrame.StyledPanel)
        self.leftBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.leftBar)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.homeButton = QPushButton(self.leftBar)
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

        self.home_label_2 = QLabel(self.leftBar)
        self.home_label_2.setObjectName(u"home_label_2")
        self.home_label_2.setStyleSheet(u"text-align: center;")

        self.verticalLayout_11.addWidget(self.home_label_2)


        self.verticalLayout_10.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.timeTableButton_2 = QPushButton(self.leftBar)
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

        self.timeTable_label_2 = QLabel(self.leftBar)
        self.timeTable_label_2.setObjectName(u"timeTable_label_2")
        self.timeTable_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.timeTable_label_2)


        self.verticalLayout_10.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
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
"border-radius: 10px;\n"
"border: 1px solid #000000;\n"
"")

        self.verticalLayout_13.addWidget(self.noteButton)

        self.note_label_2 = QLabel(self.leftBar)
        self.note_label_2.setObjectName(u"note_label_2")

        self.verticalLayout_13.addWidget(self.note_label_2)


        self.verticalLayout_10.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
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
"border-radius: 10px;")

        self.verticalLayout_14.addWidget(self.taskButton)

        self.task_label_2 = QLabel(self.leftBar)
        self.task_label_2.setObjectName(u"task_label_2")

        self.verticalLayout_14.addWidget(self.task_label_2)


        self.verticalLayout_10.addLayout(self.verticalLayout_14)


        self.verticalLayout_9.addLayout(self.verticalLayout_10)

        self.frame_2 = QFrame(self.leftBar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.unAddButton = QPushButton(self.frame_2)
        self.unAddButton.setObjectName(u"unAddButton")
        self.unAddButton.setGeometry(QRect(0, 90, 67, 61))
        self.unAddButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.unAddButton.setFocusPolicy(Qt.ClickFocus)
        self.unAddButton.setStyleSheet(u"background: rgba(0,0,0,0);\n"
"image: url(D:/NotaProject/pics/unAdd.png);")

        self.verticalLayout_9.addWidget(self.frame_2)

        self.frame_5.raise_()
        self.topBar.raise_()
        self.leftBar.raise_()
        self.layoutWidget1 = QWidget(timetabledialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.retranslateUi(timetabledialog)

        QMetaObject.connectSlotsByName(timetabledialog)
    # setupUi

    def retranslateUi(self, timetabledialog):
        timetabledialog.setWindowTitle(QCoreApplication.translate("timetabledialog", u"Nota", None))
        self.welcomeUser.setText(QCoreApplication.translate("timetabledialog", u"Welcome,", None))
        self.date.setText(QCoreApplication.translate("timetabledialog", u"November 21, 2021", None))
        self.cancelTimetableButton.setText(QCoreApplication.translate("timetabledialog", u"CANCEL", None))
        self.saveTimetableButton.setText(QCoreApplication.translate("timetabledialog", u"ADD", None))
        self.timetabletitleName_textEdit.setHtml(QCoreApplication.translate("timetabledialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.timetabletitleName_textEdit.setPlaceholderText(QCoreApplication.translate("timetabledialog", u"TASKNAME", None))
        self.timetable_description.setPlaceholderText(QCoreApplication.translate("timetabledialog", u"DESCRIPTION", None))
#if QT_CONFIG(tooltip)
        self.monday_button_Repeat.setToolTip(QCoreApplication.translate("timetabledialog", u"<html><head/><body><p align=\"center\">Press to select the day that you want to do every day. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.monday_button_Repeat.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.monday_button_Repeat.setText(QCoreApplication.translate("timetabledialog", u"MONDAY", None))
#if QT_CONFIG(tooltip)
        self.tuesday_button_Repeat.setToolTip(QCoreApplication.translate("timetabledialog", u"<html><head/><body><p align=\"center\">Press to select the day that you want to do every day. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tuesday_button_Repeat.setText(QCoreApplication.translate("timetabledialog", u"TUESDAY", None))
#if QT_CONFIG(tooltip)
        self.wednesday_Repeat.setToolTip(QCoreApplication.translate("timetabledialog", u"<html><head/><body><p align=\"center\">Press to select the day that you want to do every day. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.wednesday_Repeat.setText(QCoreApplication.translate("timetabledialog", u"WEDNESDAY", None))
#if QT_CONFIG(tooltip)
        self.thursday_Repeat.setToolTip(QCoreApplication.translate("timetabledialog", u"<html><head/><body><p align=\"center\">Press to select the day that you want to do every day. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.thursday_Repeat.setText(QCoreApplication.translate("timetabledialog", u"THURSDAY", None))
#if QT_CONFIG(tooltip)
        self.friday_button_Repeat.setToolTip(QCoreApplication.translate("timetabledialog", u"<html><head/><body><p align=\"center\">Press to select the day that you want to do every day. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.friday_button_Repeat.setText(QCoreApplication.translate("timetabledialog", u"FRIDAY", None))
#if QT_CONFIG(tooltip)
        self.saturday_button_Repeat.setToolTip(QCoreApplication.translate("timetabledialog", u"<html><head/><body><p align=\"center\">Press to select the day that you want to do every day. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.saturday_button_Repeat.setText(QCoreApplication.translate("timetabledialog", u"SATURDAY", None))
#if QT_CONFIG(tooltip)
        self.sunday_button_Repeat.setToolTip(QCoreApplication.translate("timetabledialog", u"<html><head/><body><p align=\"center\">Press to select the day that you want to do every day. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sunday_button_Repeat.setText(QCoreApplication.translate("timetabledialog", u"SUNDAY", None))
#if QT_CONFIG(tooltip)
        self.homeButton.setToolTip(QCoreApplication.translate("timetabledialog", u"<html><head/><body><p><br/>home</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.homeButton.setWhatsThis(QCoreApplication.translate("timetabledialog", u"<html><head/><body><p>home</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.homeButton.setText("")
        self.home_label_2.setText(QCoreApplication.translate("timetabledialog", u"     HOME", None))
        self.timeTableButton_2.setText("")
        self.timeTable_label_2.setText(QCoreApplication.translate("timetabledialog", u" TIMETABLE", None))
        self.noteButton.setText("")
        self.note_label_2.setText(QCoreApplication.translate("timetabledialog", u"    NOTE", None))
        self.taskButton.setText("")
        self.task_label_2.setText(QCoreApplication.translate("timetabledialog", u"     TASK", None))
        self.unAddButton.setText("")
    # retranslateUi

