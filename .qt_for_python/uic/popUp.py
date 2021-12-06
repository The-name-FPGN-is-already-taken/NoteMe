# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popUp.ui'
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
        Dialog.resize(400, 170)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 141, 20))
        self.label.setStyleSheet(u"font: 75 14pt \"AvenirNext LT Pro Bold\";")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 361, 21))
        self.label_2.setStyleSheet(u"font: 75 10pt \"AvenirNext LT Pro \";")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 400, 170))
        self.frame.setStyleSheet(u"background-color: rgb(254, 250, 224);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.confirm = QPushButton(self.frame)
        self.confirm.setObjectName(u"confirm")
        self.confirm.setGeometry(QRect(240, 120, 60, 28))
        self.confirm.setMaximumSize(QSize(60, 28))
        self.confirm.setCursor(QCursor(Qt.PointingHandCursor))
        self.confirm.setStyleSheet(u"QPushButton#confirm{\n"
"   background-color:rgb(132, 178, 137);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover#confirm{\n"
"   background-color: rgb(132, 178, 137);\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 7pt \"AvenirNext LT Pro Bold\";\n"
"	\n"
"}")
        self.cancel = QPushButton(self.frame)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(310, 120, 60, 28))
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
        self.frame.raise_()
        self.label.raise_()
        self.label_2.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Delete Task", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Do you really want to delete task?", None))
        self.confirm.setText(QCoreApplication.translate("Dialog", u"YES", None))
        self.cancel.setText(QCoreApplication.translate("Dialog", u"CANCEL", None))
    # retranslateUi

