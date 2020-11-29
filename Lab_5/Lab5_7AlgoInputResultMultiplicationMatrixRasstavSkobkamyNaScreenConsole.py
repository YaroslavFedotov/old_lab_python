import numpy as np
from time import time
a = np.loadtxt('C:/Users/HP/Desktop/K.J.P Floder/Лабы/Отчёт/Korneela.E.I/Лабораторная работа №5/Matrix_1.txt')
b = np.loadtxt('C:/Users/HP/Desktop/K.J.P Floder/Лабы/Отчёт/Korneela.E.I/Лабораторная работа №5/Matrix_2.txt')
c = np.loadtxt('C:/Users/HP/Desktop/K.J.P Floder/Лабы/Отчёт/Korneela.E.I/Лабораторная работа №5/Matrix_3.txt')

def Matrix_Multiply(A,B):
    columns = int (A.shape[0])
    rows = int(B.shape[1])
    c = np.zeros((rows, columns))
    if (columns != rows):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Ошибка!")
        msg.setText("Умножить нельзя")
        msg.setIcon(msg.Warning)
        msg.exec()   
    else:
        for i in range(len(A)):
            for j in range(len(B[0])):
                if(c[i][j] == 0):
                    for k in range(len(B)):
                        c[i][j] += A[i][k] * B[k][j]
    return c
startMatrixAB = time()
d = Matrix_Multiply(a,b)
endMatrixAB = time()
EndTimeMatrixAB = endMatrixAB - startMatrixAB
startMatrixBA = time()
d = Matrix_Multiply(b,a)
endMatrixBA = time()
EndTimeMatrixBA = endMatrixBA - startMatrixBA
startMatrixAC = time()
d = Matrix_Multiply(a,c)
endMatrixAC = time()
EndTimeMatrixAC = endMatrixAC - startMatrixAC
startMatrixCA = time()
d = Matrix_Multiply(c,a)
endMatrixCA = time()
EndTimeMatrixCA = endMatrixCA - startMatrixCA
startMatrixBC = time()
d = Matrix_Multiply(b,c)
endMatrixBC = time()
EndTimeMatrixBC = endMatrixBC - startMatrixBC
startMatrixCB = time()
d = Matrix_Multiply(c,b)
endMatrixCB = time()
EndTimeMatrixCB = endMatrixCB - startMatrixCB
bracket = str("")
if(EndTimeMatrixAB < EndTimeMatrixBA):
    bracket = bracket + " (A)*(B) "
else:
    bracket = bracket + " (B)*(A) "
if(EndTimeMatrixAC < EndTimeMatrixCA):
    bracket = bracket + " (A)*(C) "
else:
    bracket = bracket + " (C)*(A) "
if(EndTimeMatrixBC < EndTimeMatrixCB):
    bracket = bracket + " (B)*(C) "
else:
    bracket = bracket + " (C)*(B) "

print(bracket)


