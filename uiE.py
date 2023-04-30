# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EmployeeszZFTmX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_window(object):
    def setupUi(self, window):
        if not window.objectName():
            window.setObjectName(u"window")
        window.resize(532, 634)
        window.setMinimumSize(QSize(532, 634))
        window.setMaximumSize(QSize(532, 634))
        window.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.prev = QPushButton(self.centralwidget)
        self.prev.setObjectName(u"prev")
        self.prev.setGeometry(QRect(370, 10, 81, 51))
        self.next = QPushButton(self.centralwidget)
        self.next.setObjectName(u"next")
        self.next.setEnabled(True)
        self.next.setGeometry(QRect(450, 10, 81, 51))
        self.settings = QPushButton(self.centralwidget)
        self.settings.setObjectName(u"settings")
        self.settings.setGeometry(QRect(0, 10, 81, 51))
        self.save = QPushButton(self.centralwidget)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(80, 10, 61, 51))
        self.remove = QPushButton(self.centralwidget)
        self.remove.setObjectName(u"remove")
        self.remove.setGeometry(QRect(140, 10, 61, 51))
        self.conn = QLabel(self.centralwidget)
        self.conn.setObjectName(u"conn")
        self.conn.setGeometry(QRect(10, 600, 121, 21))
        self.name = QLabel(self.centralwidget)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(10, 130, 241, 51))
        self.name.setScaledContents(True)
        self.age = QLabel(self.centralwidget)
        self.age.setObjectName(u"age")
        self.age.setGeometry(QRect(10, 170, 151, 41))
        self.schedule = QLabel(self.centralwidget)
        self.schedule.setObjectName(u"schedule")
        self.schedule.setGeometry(QRect(10, 210, 231, 41))
        self.phone = QLabel(self.centralwidget)
        self.phone.setObjectName(u"phone")
        self.phone.setGeometry(QRect(10, 250, 231, 41))
        self.photo = QLabel(self.centralwidget)
        self.photo.setObjectName(u"photo")
        self.photo.setGeometry(QRect(270, 90, 231, 231))
        self.photo.setCursor(QCursor(Qt.ArrowCursor))
        self.photo.setPixmap(QPixmap(u"../../../../home/fmmaks/Pictures/150px-Mascot_konqi-dev-qt.png"))
        self.email = QLabel(self.centralwidget)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(10, 290, 231, 41))
        self.error = QLabel(self.centralwidget)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(75, 90, 371, 161))
        self.error.setStyleSheet(u"border: 1px solid red;")
        self.error.setAlignment(Qt.AlignCenter)
        window.setCentralWidget(self.centralwidget)

        self.retranslateUi(window)

        QMetaObject.connectSlotsByName(window)
    # setupUi

    def retranslateUi(self, window):
        window.setWindowTitle(QCoreApplication.translate("window", u"EmployeesViewer.AppImage", None))
        self.prev.setText(QCoreApplication.translate("window", u"<<", None))
        self.next.setText(QCoreApplication.translate("window", u">>", None))
        self.settings.setText(QCoreApplication.translate("window", u"Settings", None))
        self.save.setText(QCoreApplication.translate("window", u"Save", None))
        self.remove.setText(QCoreApplication.translate("window", u"Delete", None))
        self.conn.setText(QCoreApplication.translate("window", u"Connected to:", None))
        self.name.setText(QCoreApplication.translate("window", u"Name: ", None))
        self.age.setText(QCoreApplication.translate("window", u"Age: ", None))
        self.schedule.setText(QCoreApplication.translate("window", u"Schedule:", None))
        self.phone.setText(QCoreApplication.translate("window", u"Phone: ", None))
        self.photo.setText("")
        self.email.setText(QCoreApplication.translate("window", u"Email:  ", None))
    # retranslateUi
