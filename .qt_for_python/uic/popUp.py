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
        Dialog.resize(531, 235)
        icon = QIcon()
        icon.addFile(u"pics/notaKung.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
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
        self.edit = QPushButton(self.layoutWidget)
        self.edit.setObjectName(u"edit")
        self.edit.setMaximumSize(QSize(60, 28))
        self.edit.setCursor(QCursor(Qt.PointingHandCursor))
        self.edit.setStyleSheet(u"QPushButton#edit{\n"
"   background-color:rgb(254, 254, 0);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover#edit{\n"
"   background-color:rgb(200, 162, 7);\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 7pt \"AvenirNext LT Pro Bold\";\n"
"	\n"
"}")

        self.option.addWidget(self.edit)

        self.mark = QPushButton(self.layoutWidget)
        self.mark.setObjectName(u"mark")
        self.mark.setMaximumSize(QSize(150, 28))
        self.mark.setCursor(QCursor(Qt.PointingHandCursor))
        self.mark.setStyleSheet(u"QPushButton#mark{\n"
"   background-color:rgba(165, 255, 236,150);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover#mark{\n"
"   background-color: rgb(0, 204, 153);\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 7pt \"AvenirNext LT Pro Bold\";\n"
"	\n"
"}")

        self.option.addWidget(self.mark)

        self.delete_2 = QPushButton(self.layoutWidget)
        self.delete_2.setObjectName(u"delete_2")
        self.delete_2.setMaximumSize(QSize(60, 28))
        self.delete_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_2.setStyleSheet(u"QPushButton#delete_2{\n"
"   background-color:rgba(255, 0, 0,100);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover#delete_2{\n"
"   background-color:rgb(212, 0, 0);\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 7pt \"AvenirNext LT Pro Bold\";\n"
"	\n"
"}")

        self.option.addWidget(self.delete_2)


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
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"NOTA", None))
        self.direction.setText(QCoreApplication.translate("Dialog", u"Please choose action you want to do with this task", None))
        self.edit.setText(QCoreApplication.translate("Dialog", u"EDIT", None))
        self.mark.setText(QCoreApplication.translate("Dialog", u"MARK AS COMPLETED", None))
        self.delete_2.setText(QCoreApplication.translate("Dialog", u"DELETE", None))
        self.confirmation.setText(QCoreApplication.translate("Dialog", u"Do you really want to delete this?", None))
        self.confirm.setText(QCoreApplication.translate("Dialog", u"YES", None))
        self.cancel.setText(QCoreApplication.translate("Dialog", u"CANCEL", None))
    # retranslateUi

