# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vibona4y.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculation(object):
    def setupUi(self, Calculation):
        Calculation.setObjectName("Calculation")
        Calculation.resize(775, 285)
        self.centralwidget = QtWidgets.QWidget(Calculation)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEditInputVibona4y = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditInputVibona4y.setGeometry(QtCore.QRect(320, 30, 141, 21))
        self.lineEditInputVibona4y.setObjectName("lineEditInputVibona4y")
        self.NumberVibona4y = QtWidgets.QLabel(self.centralwidget)
        self.NumberVibona4y.setGeometry(QtCore.QRect(294, 10, 201, 20))
        self.NumberVibona4y.setObjectName("NumberVibona4y")
        self.pushButtonChisloInDataGrid = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonChisloInDataGrid.setGeometry(QtCore.QRect(340, 50, 93, 28))
        self.pushButtonChisloInDataGrid.setAutoDefault(True)
        self.pushButtonChisloInDataGrid.setObjectName("pushButtonChisloInDataGrid")
        self.radioButtonInput1Number = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonInput1Number.setGeometry(QtCore.QRect(630, 30, 95, 20))
        self.radioButtonInput1Number.setChecked(True)
        self.radioButtonInput1Number.setObjectName("radioButtonInput1Number")
        self.radioButtonInput2Number = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonInput2Number.setGeometry(QtCore.QRect(630, 60, 95, 20))
        self.radioButtonInput2Number.setChecked(False)
        self.radioButtonInput2Number.setObjectName("radioButtonInput2Number")
        self.tableWidgetVibona4y = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetVibona4y.setGeometry(QtCore.QRect(10, 91, 751, 161))
        self.tableWidgetVibona4y.setObjectName("tableWidgetVibona4y")
        self.tableWidgetVibona4y.setColumnCount(0)
        self.tableWidgetVibona4y.setRowCount(0)
        Calculation.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Calculation)
        self.statusbar.setObjectName("statusbar")
        Calculation.setStatusBar(self.statusbar)

        self.retranslateUi(Calculation)
        QtCore.QMetaObject.connectSlotsByName(Calculation)

    def retranslateUi(self, Calculation):
        _translate = QtCore.QCoreApplication.translate
        Calculation.setWindowTitle(_translate("Calculation", "Вычисление чисел фибоначчи."))
        self.NumberVibona4y.setText(_translate("Calculation", "Номер элемента ряда Фибоначчи:"))
        self.pushButtonChisloInDataGrid.setText(_translate("Calculation", "Вычислить"))
        self.radioButtonInput1Number.setText(_translate("Calculation", "3"))
        self.radioButtonInput2Number.setText(_translate("Calculation", "5"))
