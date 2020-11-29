import sys
#Импортируем наш интерфейс
from Vibona4y import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
class MyWin(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_Calculation()
        self.ui.setupUi(self)

        # Начало моего дописанного кода:
        self.ui.tableWidgetVibona4y.setColumnCount(5)
        self.ui.tableWidgetVibona4y.setHorizontalHeaderLabels(["Номер вычисления", "Число n", "Алгоритм","Результат вычисления","Время выполнения алгоритма"])
        self.ui.tableWidgetVibona4y.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
        self.ui.tableWidgetVibona4y.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.ui.tableWidgetVibona4y.horizontalHeaderItem(2).setTextAlignment(Qt.AlignHCenter)
        self.ui.tableWidgetVibona4y.horizontalHeaderItem(3).setTextAlignment(Qt.AlignHCenter)
        self.ui.tableWidgetVibona4y.horizontalHeaderItem(4).setTextAlignment(Qt.AlignHCenter)
        self.ui.pushButtonChisloInDataGrid.clicked.connect(self.getResult)
        #Функция вычисления чисел фибоначчи
    def getResult(self):
        try:
            f = open('C:/Users/HP/Desktop/PythonQ5/TableSave.txt', 'w')
            f.write("Номер вычисления         Число n               Алгоритм         Результат вычисления         Время выполнения алгоритмa")
            fib1 = fib2 = 1
            if(self.ui.lineEditInputVibona4y.text() == ""):
                n = int()
                if(self.ui.radioButtonInput1Number.isChecked()):
                    n = 3
                else:
                    n = 5
                self.ui.tableWidgetVibona4y.setRowCount(n)
                i = int(0)
                from time import time
                while n > 0:
                    start = time()
                    fib1,fib2 = fib2, fib1+fib2
                    end = time()
                    self.ui.tableWidgetVibona4y.setItem(i,0, QTableWidgetItem(str(i)))
                    self.ui.tableWidgetVibona4y.setItem(i,1, QTableWidgetItem(str(n)))
                    self.ui.tableWidgetVibona4y.setItem(i,2, QTableWidgetItem("RadioButton"))
                    self.ui.tableWidgetVibona4y.setItem(i,3, QTableWidgetItem(str(fib2)))
                    self.ui.tableWidgetVibona4y.setItem(i,4, QTableWidgetItem(str(end-start)))
                    f.write('\n')
                    f.write(str(i))
                    f.write('			   ')
                    f.write(str(n))
                    f.write('			   ')
                    f.write("RadioButton")
                    f.write('			   ')
                    f.write(str(fib2))
                    f.write('			   ')
                    f.write(str(end-start))
                    n -= 1
                    i+=1
                f.close()
            if(self.ui.lineEditInputVibona4y.text() != ""):
                n = int(self.ui.lineEditInputVibona4y.text())
                self.ui.tableWidgetVibona4y.setRowCount(n)
                i = int(0)
                from time import time
                while n > 0:
                    start = time()
                    fib1,fib2 = fib2, fib1+fib2
                    end = time()
                    self.ui.tableWidgetVibona4y.setItem(i,0, QTableWidgetItem(str(i)))
                    self.ui.tableWidgetVibona4y.setItem(i,1, QTableWidgetItem(str(n)))
                    self.ui.tableWidgetVibona4y.setItem(i,2, QTableWidgetItem("Клавиатура"))
                    self.ui.tableWidgetVibona4y.setItem(i,3, QTableWidgetItem(str(fib2)))
                    self.ui.tableWidgetVibona4y.setItem(i,4, QTableWidgetItem(str(end-start)))
                    f.write('\n')
                    f.write(str(i))
                    f.write('			   ')
                    f.write(str(n))
                    f.write('			   ')
                    f.write("Клавиатура")
                    f.write('			   ')
                    f.write(str(fib2))
                    f.write('			   ')
                    f.write(str(end-start))
                    n -= 1
                    i+=1
                f.close()
        except:
            f.close()
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Ошибка ввода!")
            msg.setText("Введите корректные данные!")
            msg.setIcon(msg.Warning)
            msg.exec()

        # Конец моего кода
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
