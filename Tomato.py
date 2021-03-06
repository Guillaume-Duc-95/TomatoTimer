# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tomato.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(333, 304)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonSetTime = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSetTime.setGeometry(QtCore.QRect(220, 30, 89, 71))
        self.pushButtonSetTime.setObjectName("pushButtonSetTime")
        self.pushButtonStartTime = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStartTime.setGeometry(QtCore.QRect(30, 220, 89, 51))
        self.pushButtonStartTime.setObjectName("pushButtonStartTime")
        self.pushButtonPause = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPause.setGeometry(QtCore.QRect(220, 220, 89, 25))
        self.pushButtonPause.setObjectName("pushButtonPause")
        self.pushButtonNextStep = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNextStep.setGeometry(QtCore.QRect(130, 220, 89, 25))
        self.pushButtonNextStep.setObjectName("pushButtonNextStep")
        self.pushButtonSnooze = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSnooze.setGeometry(QtCore.QRect(130, 250, 89, 25))
        self.pushButtonSnooze.setObjectName("pushButtonSnooze")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 120, 281, 91))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButtonQuit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonQuit.setGeometry(QtCore.QRect(220, 250, 89, 25))
        self.pushButtonQuit.setObjectName("pushButtonQuit")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 40, 144, 64))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBoxWork = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBoxWork.setToolTip("")
        self.spinBoxWork.setWhatsThis("")
        self.spinBoxWork.setAccessibleName("")
        self.spinBoxWork.setStyleSheet("")
        self.spinBoxWork.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBoxWork.setSpecialValueText("")
        self.spinBoxWork.setMaximum(999)
        self.spinBoxWork.setProperty("value", 20)
        self.spinBoxWork.setObjectName("spinBoxWork")
        self.horizontalLayout.addWidget(self.spinBoxWork)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spinBoxBreak = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBoxBreak.setToolTip("")
        self.spinBoxBreak.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBoxBreak.setSuffix("")
        self.spinBoxBreak.setMaximum(999)
        self.spinBoxBreak.setProperty("value", 5)
        self.spinBoxBreak.setObjectName("spinBoxBreak")
        self.horizontalLayout_2.addWidget(self.spinBoxBreak)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.labelDispTimer = QtWidgets.QLabel(self.centralwidget)
        self.labelDispTimer.setGeometry(QtCore.QRect(36, 126, 271, 81))
        font = QtGui.QFont()
        font.setPointSize(57)
        font.setBold(False)
        font.setWeight(50)
        self.labelDispTimer.setFont(font)
        self.labelDispTimer.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.labelDispTimer.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDispTimer.setObjectName("labelDispTimer")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButtonQuit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tomato"))
        self.pushButtonSetTime.setText(_translate("MainWindow", "Set"))
        self.pushButtonStartTime.setText(_translate("MainWindow", "Start"))
        self.pushButtonPause.setText(_translate("MainWindow", "Pause"))
        self.pushButtonNextStep.setText(_translate("MainWindow", "Next"))
        self.pushButtonSnooze.setText(_translate("MainWindow", "Snooze"))
        self.pushButtonQuit.setText(_translate("MainWindow", "Quit"))
        self.label.setText(_translate("MainWindow", "Work Time"))
        self.spinBoxWork.setAccessibleDescription(_translate("MainWindow", "<html><head/><body><p>Time of Work Session</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Break Time"))
        self.labelDispTimer.setText(_translate("MainWindow", "999:00"))

