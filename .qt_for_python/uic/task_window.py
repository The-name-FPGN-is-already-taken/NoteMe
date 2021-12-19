# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task_window.ui'
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

class Ui_homeCal(object):
    def setupUi(self, homeCal):
        if not homeCal.objectName():
            homeCal.setObjectName(u"homeCal")
        homeCal.resize(1024, 640)
        homeCal.setMinimumSize(QSize(1024, 640))
        homeCal.setMaximumSize(QSize(1920, 1080))
        self.backFrame = QFrame(homeCal)
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
"        \n"
"border-radius: 35px;\n"
"")
        self.app_icon.setFrameShape(QFrame.StyledPanel)
        self.app_icon.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.topBar)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 20, 681, 53))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.welcomeUser = QLabel(self.layoutWidget)
        self.welcomeUser.setObjectName(u"welcomeUser")
        font = QFont()
        font.setFamilies([u"Tenor Sans"])
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
        self.frame = QFrame(self.frame_5)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 20, 871, 481))
        self.frame.setStyleSheet(u"width: 763px;\n"
"height: 456px;\n"
"left: 60px;\n"
"top: 30px;\n"
"\n"
"background: #E4E2C7;\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(151, 33, 16, 28))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(62, 31, 755, 412))
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Today_Label = QLabel(self.widget)
        self.Today_Label.setObjectName(u"Today_Label")
        sizePolicy.setHeightForWidth(self.Today_Label.sizePolicy().hasHeightForWidth())
        self.Today_Label.setSizePolicy(sizePolicy)
        self.Today_Label.setMaximumSize(QSize(100, 20))
        self.Today_Label.setStyleSheet(u"font: 75 14pt \"AvenirNext LT Pro Bold\";")
        self.Today_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.Today_Label)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_3)

        self.showButton = QPushButton(self.widget)
        self.showButton.setObjectName(u"showButton")
        self.showButton.setMaximumSize(QSize(200, 28))
        self.showButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.showButton.setStyleSheet(u"QPushButton#showButton{\n"
"   background-color: rgb(252, 188, 64);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover#showButton{\n"
"   background-color: rgb(252, 188, 64);\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 8pt \"AvenirNext LT Pro Bold\";\n"
"	\n"
"}")

        self.horizontalLayout_2.addWidget(self.showButton)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.listWidget = QListWidget(self.widget)
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
        self.listWidget.setMaximumSize(QSize(371, 371))
        self.listWidget.setStyleSheet(u"background-color: rgb(254, 250, 224);")

        self.verticalLayout_8.addWidget(self.listWidget)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Tomorrow_Label = QLabel(self.widget)
        self.Tomorrow_Label.setObjectName(u"Tomorrow_Label")
        self.Tomorrow_Label.setMaximumSize(QSize(200, 28))
        self.Tomorrow_Label.setStyleSheet(u"font: 75 14pt \"AvenirNext LT Pro Bold\";")
        self.Tomorrow_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.Tomorrow_Label)

        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_4)

        self.sortButton = QPushButton(self.widget)
        self.sortButton.setObjectName(u"sortButton")
        self.sortButton.setMaximumSize(QSize(60, 28))
        self.sortButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.sortButton.setStyleSheet(u"QPushButton#sortButton{\n"
"   background-color: rgb(252, 188, 64);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover#sortButton{\n"
"   background-color: rgb(252, 188, 64);\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 9pt \"AvenirNext LT Pro Bold\";\n"
"	\n"
"}")

        self.horizontalLayout_3.addWidget(self.sortButton)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)

        self.listWidget_incoming = QListWidget(self.widget)
        QListWidgetItem(self.listWidget_incoming)
        QListWidgetItem(self.listWidget_incoming)
        QListWidgetItem(self.listWidget_incoming)
        QListWidgetItem(self.listWidget_incoming)
        QListWidgetItem(self.listWidget_incoming)
        QListWidgetItem(self.listWidget_incoming)
        QListWidgetItem(self.listWidget_incoming)
        QListWidgetItem(self.listWidget_incoming)
        QListWidgetItem(self.listWidget_incoming)
        QListWidgetItem(self.listWidget_incoming)
        QListWidgetItem(self.listWidget_incoming)
        QListWidgetItem(self.listWidget_incoming)
        QListWidgetItem(self.listWidget_incoming)
        QListWidgetItem(self.listWidget_incoming)
        QListWidgetItem(self.listWidget_incoming)
        QListWidgetItem(self.listWidget_incoming)
        QListWidgetItem(self.listWidget_incoming)
        self.listWidget_incoming.setObjectName(u"listWidget_incoming")
        self.listWidget_incoming.setMaximumSize(QSize(371, 371))
        self.listWidget_incoming.setStyleSheet(u"background-color: rgb(254, 250, 224);")

        self.verticalLayout_9.addWidget(self.listWidget_incoming)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)

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
        self.verticalLayout_7 = QVBoxLayout(self.leftBar)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
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
"        \n"
"background: #C4C4C4;\n"
"border: 1px solid #000000;\n"
"\n"
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
"")

        self.verticalLayout_3.addWidget(self.timeTableButton)

        self.timeTable_label = QLabel(self.leftBar)
        self.timeTable_label.setObjectName(u"timeTable_label")
        self.timeTable_label.setAlignment(Qt.AlignCenter)

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
        self.taskButton.setCursor(QCursor(Qt.ArrowCursor))
        self.taskButton.setStyleSheet(u"image: url(D:/NotaProject/pics/task.png);\n"
"position: absolute;\n"
"width: 120px;\n"
"height: 37px;\n"
"left: 7px;\n"
"top: 160px;\n"
"text-align: right;\n"
"background: #ECF39E;\n"
"\n"
"\n"
"border-radius: 10px;")

        self.verticalLayout_5.addWidget(self.taskButton)

        self.task_label = QLabel(self.leftBar)
        self.task_label.setObjectName(u"task_label")

        self.verticalLayout_5.addWidget(self.task_label)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.frame_2 = QFrame(self.leftBar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.addTask = QPushButton(self.frame_2)
        self.addTask.setObjectName(u"addTask")
        self.addTask.setGeometry(QRect(0, 90, 67, 61))
        self.addTask.setCursor(QCursor(Qt.PointingHandCursor))
        self.addTask.setFocusPolicy(Qt.ClickFocus)
        self.addTask.setStyleSheet(u"background: rgba(0,0,0,0);\n"
"image: url(D:/NotaProject/pics/add.png);")

        self.verticalLayout_7.addWidget(self.frame_2)

        self.layoutWidget1 = QWidget(homeCal)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.retranslateUi(homeCal)

        QMetaObject.connectSlotsByName(homeCal)
    # setupUi

    def retranslateUi(self, homeCal):
        homeCal.setWindowTitle(QCoreApplication.translate("homeCal", u"Form", None))
        self.welcomeUser.setText(QCoreApplication.translate("homeCal", u"Welcome,", None))
        self.date.setText(QCoreApplication.translate("homeCal", u"November 21, 2021", None))
        self.Today_Label.setText(QCoreApplication.translate("homeCal", u"TODAY", None))
        self.showButton.setText(QCoreApplication.translate("homeCal", u"SHOW COMPLETED TASKS", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("homeCal", u"\u0e22\u0e1f\u0e2b\u0e01\u0e1f\u0e2b\u0e01", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem5 = self.listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem6 = self.listWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem7 = self.listWidget.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem8 = self.listWidget.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem9 = self.listWidget.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem10 = self.listWidget.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem11 = self.listWidget.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem12 = self.listWidget.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem13 = self.listWidget.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem14 = self.listWidget.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem15 = self.listWidget.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem16 = self.listWidget.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("homeCal", u"\u0e1f\u0e2b\u0e01\u0e1f\u0e2b\u0e01", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.listWidget.setToolTip(QCoreApplication.translate("homeCal", u"<html><head/><body><p>double click to edit</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Tomorrow_Label.setText(QCoreApplication.translate("homeCal", u"ALL TASKS", None))
        self.sortButton.setText(QCoreApplication.translate("homeCal", u"SORT", None))

        __sortingEnabled1 = self.listWidget_incoming.isSortingEnabled()
        self.listWidget_incoming.setSortingEnabled(False)
        ___qlistwidgetitem17 = self.listWidget_incoming.item(0)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("homeCal", u"\u0e22\u0e1f\u0e2b\u0e01\u0e1f\u0e2b\u0e01", None));
        ___qlistwidgetitem18 = self.listWidget_incoming.item(1)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem19 = self.listWidget_incoming.item(2)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem20 = self.listWidget_incoming.item(3)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem21 = self.listWidget_incoming.item(4)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem22 = self.listWidget_incoming.item(5)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem23 = self.listWidget_incoming.item(6)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem24 = self.listWidget_incoming.item(7)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem25 = self.listWidget_incoming.item(8)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem26 = self.listWidget_incoming.item(9)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem27 = self.listWidget_incoming.item(10)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem28 = self.listWidget_incoming.item(11)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem29 = self.listWidget_incoming.item(12)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem30 = self.listWidget_incoming.item(13)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem31 = self.listWidget_incoming.item(14)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem32 = self.listWidget_incoming.item(15)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("homeCal", u"New Item", None));
        ___qlistwidgetitem33 = self.listWidget_incoming.item(16)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("homeCal", u"\u0e1f\u0e2b\u0e01\u0e1f\u0e2b\u0e01", None));
        self.listWidget_incoming.setSortingEnabled(__sortingEnabled1)

#if QT_CONFIG(tooltip)
        self.listWidget_incoming.setToolTip(QCoreApplication.translate("homeCal", u"<html><head/><body><p>double click to edit</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.homeButton.setToolTip(QCoreApplication.translate("homeCal", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.homeButton.setWhatsThis(QCoreApplication.translate("homeCal", u"<html><head/><body><p>home</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.homeButton.setText("")
        self.home_label.setText(QCoreApplication.translate("homeCal", u"     HOME", None))
        self.timeTableButton.setText("")
        self.timeTable_label.setText(QCoreApplication.translate("homeCal", u" TIMETABLE", None))
        self.noteButton.setText("")
        self.note_label.setText(QCoreApplication.translate("homeCal", u"    NOTE", None))
        self.taskButton.setText("")
        self.task_label.setText(QCoreApplication.translate("homeCal", u"     TASK", None))
        self.addTask.setText("")
    # retranslateUi

