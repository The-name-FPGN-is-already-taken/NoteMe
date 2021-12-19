# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popUp_Redo.ui'
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
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(531, 235)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 531, 241))
        self.frame.setStyleSheet(u"background-color: rgb(254, 250, 224);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.direction = QLabel(self.frame)
        self.direction.setObjectName(u"direction")
        self.direction.setGeometry(QRect(20, 20, 501, 24))
        self.direction.setStyleSheet(u"	font: 75 12pt \"AvenirNext LT Pro Bold\";\n"
"")
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(90, 70, 361, 151))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.option = QHBoxLayout()
        self.option.setObjectName(u"option")
        self.Redo = QPushButton(self.layoutWidget)
        self.Redo.setObjectName(u"Redo")
        self.Redo.setMaximumSize(QSize(60, 28))
        self.Redo.setCursor(QCursor(Qt.PointingHandCursor))
        self.Redo.setStyleSheet(u"QPushButton#Redo{\n"
"   background-color:rgb(254, 254, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover#Redo{\n"
"   background-color:rgb(200, 162, 7);\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 7pt \"AvenirNext LT Pro Bold\";\n"
"	\n"
"}")

        self.option.addWidget(self.Redo)

        self.delete_Redo = QPushButton(self.layoutWidget)
        self.delete_Redo.setObjectName(u"delete_Redo")
        self.delete_Redo.setMaximumSize(QSize(60, 28))
        self.delete_Redo.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_Redo.setStyleSheet(u"QPushButton#delete_Redo{\n"
"   background-color:rgba(255, 0, 0,100);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover#delete_Redo{\n"
"   background-color:rgb(212, 0, 0);\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 7pt \"AvenirNext LT Pro Bold\";\n"
"	\n"
"}")

        self.option.addWidget(self.delete_Redo)


        self.verticalLayout.addLayout(self.option)

        self.confirmationBox = QHBoxLayout()
        self.confirmationBox.setObjectName(u"confirmationBox")
        self.frame_3 = QFrame(self.layoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.confirmation = QLabel(self.frame_3)
        self.confirmation.setObjectName(u"confirmation")
        self.confirmation.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout_3.addWidget(self.confirmation)


        self.confirmationBox.addWidget(self.frame_3)

        self.confirm = QPushButton(self.layoutWidget)
        self.confirm.setObjectName(u"confirm")
        self.confirm.setMaximumSize(QSize(60, 28))
        self.confirm.setCursor(QCursor(Qt.PointingHandCursor))
        self.confirm.setStyleSheet(u"QPushButton#confirm{\n"
"   background-color:rgb(148, 194, 130);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover#confirm{\n"
"   background-color: rgb(148, 194, 130);\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 7pt \"AvenirNext LT Pro Bold\";\n"
"	\n"
"}")

        self.confirmationBox.addWidget(self.confirm)

        self.cancel = QPushButton(self.layoutWidget)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setMaximumSize(QSize(60, 28))
        self.cancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel.setStyleSheet(u"QPushButton#cancel{\n"
"   background-color: rgb(181, 181, 181);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover#cancel{\n"
"   background-color: rgb(181, 181, 181);\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 7pt \"AvenirNext LT Pro Bold\";\n"
"	\n"
"}")

        self.confirmationBox.addWidget(self.cancel)


        self.verticalLayout.addLayout(self.confirmationBox)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.direction.setText(QCoreApplication.translate("Dialog", u"Please choose action you want to do with this task", None))
        self.Redo.setText(QCoreApplication.translate("Dialog", u"REDO", None))
        self.delete_Redo.setText(QCoreApplication.translate("Dialog", u"DELETE", None))
        self.confirmation.setText(QCoreApplication.translate("Dialog", u"Do you really want to delete this?", None))
        self.confirm.setText(QCoreApplication.translate("Dialog", u"YES", None))
        self.cancel.setText(QCoreApplication.translate("Dialog", u"CANCEL", None))
    # retranslateUi

