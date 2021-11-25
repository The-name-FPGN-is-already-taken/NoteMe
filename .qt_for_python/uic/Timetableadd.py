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


class Ui_timetable_addmenu(object):
    def setupUi(self, timetable_addmenu):
        if not timetable_addmenu.objectName():
            timetable_addmenu.setObjectName(u"timetable_addmenu")
        timetable_addmenu.resize(971, 403)
        timetable_addmenu.setStyleSheet(u"border-radius: 8px;")
        self.topBar = QFrame(timetable_addmenu)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setGeometry(QRect(0, 0, 971, 141))
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
        self.app_icon.setGeometry(QRect(10, 30, 81, 81))
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
        self.widget = QWidget(self.topBar)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(120, 80, 753, 43))
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.monday_button_Repeat = QPushButton(self.widget)
        self.monday_button_Repeat.setObjectName(u"monday_button_Repeat")
        self.monday_button_Repeat.setMaximumSize(QSize(93, 41))
        self.monday_button_Repeat.setCursor(QCursor(Qt.PointingHandCursor))
        self.monday_button_Repeat.setStyleSheet(u"display: flex;\n"
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

        self.horizontalLayout_6.addWidget(self.monday_button_Repeat)

        self.tuesday_button_Repeat = QPushButton(self.widget)
        self.tuesday_button_Repeat.setObjectName(u"tuesday_button_Repeat")
        self.tuesday_button_Repeat.setMaximumSize(QSize(93, 41))
        self.tuesday_button_Repeat.setCursor(QCursor(Qt.PointingHandCursor))
        self.tuesday_button_Repeat.setStyleSheet(u"display: flex;\n"
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

        self.horizontalLayout_6.addWidget(self.tuesday_button_Repeat)

        self.wednesday_Repeat = QPushButton(self.widget)
        self.wednesday_Repeat.setObjectName(u"wednesday_Repeat")
        self.wednesday_Repeat.setMaximumSize(QSize(93, 41))
        self.wednesday_Repeat.setCursor(QCursor(Qt.PointingHandCursor))
        self.wednesday_Repeat.setStyleSheet(u"display: flex;\n"
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

        self.horizontalLayout_6.addWidget(self.wednesday_Repeat)

        self.thursday_Repeat = QPushButton(self.widget)
        self.thursday_Repeat.setObjectName(u"thursday_Repeat")
        self.thursday_Repeat.setMaximumSize(QSize(93, 41))
        self.thursday_Repeat.setCursor(QCursor(Qt.PointingHandCursor))
        self.thursday_Repeat.setStyleSheet(u"display: flex;\n"
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

        self.horizontalLayout_6.addWidget(self.thursday_Repeat)

        self.friday_button_Repeat = QPushButton(self.widget)
        self.friday_button_Repeat.setObjectName(u"friday_button_Repeat")
        self.friday_button_Repeat.setMaximumSize(QSize(93, 41))
        self.friday_button_Repeat.setCursor(QCursor(Qt.PointingHandCursor))
        self.friday_button_Repeat.setStyleSheet(u"display: flex;\n"
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

        self.horizontalLayout_6.addWidget(self.friday_button_Repeat)

        self.saturday_button_Repeat = QPushButton(self.widget)
        self.saturday_button_Repeat.setObjectName(u"saturday_button_Repeat")
        self.saturday_button_Repeat.setMaximumSize(QSize(93, 41))
        self.saturday_button_Repeat.setCursor(QCursor(Qt.PointingHandCursor))
        self.saturday_button_Repeat.setStyleSheet(u"display: flex;\n"
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

        self.horizontalLayout_6.addWidget(self.saturday_button_Repeat)

        self.sunday_button_Repeat = QPushButton(self.widget)
        self.sunday_button_Repeat.setObjectName(u"sunday_button_Repeat")
        self.sunday_button_Repeat.setMaximumSize(QSize(93, 41))
        self.sunday_button_Repeat.setCursor(QCursor(Qt.PointingHandCursor))
        self.sunday_button_Repeat.setStyleSheet(u"display: flex;\n"
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

        self.horizontalLayout_6.addWidget(self.sunday_button_Repeat)

        self.Repate = QLabel(self.topBar)
        self.Repate.setObjectName(u"Repate")
        self.Repate.setGeometry(QRect(130, 20, 201, 51))
        font = QFont()
        font.setFamily(u"AvenirNext LT Pro Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Repate.setFont(font)
        self.Repate.setStyleSheet(u"display: flex;\n"
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
        self.Repate.setAlignment(Qt.AlignCenter)
        self.timeEdit = QTimeEdit(self.topBar)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(740, 20, 191, 41))
        self.timeEdit.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.frame = QFrame(timetable_addmenu)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 140, 971, 271))
        self.frame.setStyleSheet(u"background: #84B289;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 10, 931, 181))
        self.frame_2.setStyleSheet(u"width: 744px;\n"
"height: 372px;\n"
"left: 83px;\n"
"top: 53px;\n"
"border-radius: 10px;\n"
"\n"
"background: #E4E2C7;\n"
"box-shadow: 6px 6px 4px 2px rgba(0, 0, 0, 0.25);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(60, 20, 711, 41))
        self.textEdit.setStyleSheet(u"background: rgba(0,0,0,0);\n"
"")
        self.plainTextEdit = QPlainTextEdit(self.frame_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(60, 70, 711, 311))
        self.dailyTaskadd = QLineEdit(self.frame_2)
        self.dailyTaskadd.setObjectName(u"dailyTaskadd")
        self.dailyTaskadd.setGeometry(QRect(10, 10, 891, 161))
        self.dailyTaskadd.setStyleSheet(u"\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.dailyTaskadd.setMaxLength(50)
        self.dailyTaskadd.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(730, 200, 209, 52))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cancelAdding = QPushButton(self.layoutWidget)
        self.cancelAdding.setObjectName(u"cancelAdding")
        self.cancelAdding.setMaximumSize(QSize(100, 50))
        self.cancelAdding.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelAdding.setStyleSheet(u"\n"
"background: #EC8E65;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 15px;")

        self.horizontalLayout_2.addWidget(self.cancelAdding)

        self.saveNoteButton = QPushButton(self.layoutWidget)
        self.saveNoteButton.setObjectName(u"saveNoteButton")
        self.saveNoteButton.setMaximumSize(QSize(100, 50))
        self.saveNoteButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveNoteButton.setStyleSheet(u"\n"
"background: #C6D57E;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 15px;")

        self.horizontalLayout_2.addWidget(self.saveNoteButton)


        self.retranslateUi(timetable_addmenu)

        QMetaObject.connectSlotsByName(timetable_addmenu)
    # setupUi

    def retranslateUi(self, timetable_addmenu):
        timetable_addmenu.setWindowTitle(QCoreApplication.translate("timetable_addmenu", u"Dialog", None))
        self.monday_button_Repeat.setText(QCoreApplication.translate("timetable_addmenu", u"MONDAY", None))
        self.tuesday_button_Repeat.setText(QCoreApplication.translate("timetable_addmenu", u"TUESDAY", None))
        self.wednesday_Repeat.setText(QCoreApplication.translate("timetable_addmenu", u"WEDNESDAY", None))
        self.thursday_Repeat.setText(QCoreApplication.translate("timetable_addmenu", u"THURSDAY", None))
        self.friday_button_Repeat.setText(QCoreApplication.translate("timetable_addmenu", u"FRIDAY", None))
        self.saturday_button_Repeat.setText(QCoreApplication.translate("timetable_addmenu", u"SATURDAY", None))
        self.sunday_button_Repeat.setText(QCoreApplication.translate("timetable_addmenu", u"SUNDAY", None))
#if QT_CONFIG(tooltip)
        self.Repate.setToolTip(QCoreApplication.translate("timetable_addmenu", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Repate.setWhatsThis(QCoreApplication.translate("timetable_addmenu", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Repate.setText(QCoreApplication.translate("timetable_addmenu", u"Repeat", None))
        self.textEdit.setHtml(QCoreApplication.translate("timetable_addmenu", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.dailyTaskadd.setText("")
        self.dailyTaskadd.setPlaceholderText(QCoreApplication.translate("timetable_addmenu", u"add dairy task here...", None))
        self.cancelAdding.setText(QCoreApplication.translate("timetable_addmenu", u"CANCEL", None))
        self.saveNoteButton.setText(QCoreApplication.translate("timetable_addmenu", u"SAVE", None))
    # retranslateUi

