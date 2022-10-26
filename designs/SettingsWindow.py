# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(420, 720)
        Settings.setStyleSheet("")
        self.UseDB = QtWidgets.QLabel(Settings)
        self.UseDB.setGeometry(QtCore.QRect(10, 150, 401, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.UseDB.setFont(font)
        self.UseDB.setObjectName("UseDB")
        self.BackButton = QtWidgets.QPushButton(Settings)
        self.BackButton.setGeometry(QtCore.QRect(270, 620, 141, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.BackButton.setFont(font)
        self.BackButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.BackButton.setObjectName("BackButton")
        self.CompleteBut = QtWidgets.QPushButton(Settings)
        self.CompleteBut.setGeometry(QtCore.QRect(304, 230, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.CompleteBut.setFont(font)
        self.CompleteBut.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.CompleteBut.setObjectName("CompleteBut")
        self.ChoiceBut = QtWidgets.QPushButton(Settings)
        self.ChoiceBut.setGeometry(QtCore.QRect(10, 230, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.ChoiceBut.setFont(font)
        self.ChoiceBut.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.ChoiceBut.setObjectName("ChoiceBut")
        self.ItSaveLabel = QtWidgets.QLabel(Settings)
        self.ItSaveLabel.setGeometry(QtCore.QRect(170, 270, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        self.ItSaveLabel.setFont(font)
        self.ItSaveLabel.setText("")
        self.ItSaveLabel.setObjectName("ItSaveLabel")
        self.DBText = QtWidgets.QPlainTextEdit(Settings)
        self.DBText.setGeometry(QtCore.QRect(10, 180, 401, 31))
        self.DBText.setObjectName("DBText")

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Настройки"))
        self.UseDB.setText(_translate("Settings", "Используемая БД:"))
        self.BackButton.setText(_translate("Settings", "Назад"))
        self.CompleteBut.setText(_translate("Settings", "Подтвердить"))
        self.ChoiceBut.setText(_translate("Settings", "Выбрать"))
