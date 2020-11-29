import sys
#Импортируем наш интерфейс
from Lab5 import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
import numpy as np
class MyWin(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_MatrixMultiptionWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonResult.clicked.connect(self.getResult)
        self.ui.pushButtonFileResult.clicked.connect(self.fileRec)
    

    def fileRec(self):
        with open('C:/Users/HP/Desktop/PyQt5/TableSave.txt', 'w') as yourFile:
            yourFile.write(str(self.ui.plainTextEditResultMultiplicationMatrix.toPlainText()))

    def getResult(self):
        self.ui.plainTextEditResultMultiplicationMatrix.setPlainText(str(""))
        with open('C:/Users/HP/Desktop/PyQt5/Matrix_1.txt', 'w') as yourFile:
            yourFile.write(str(self.ui.plainTextEditMatrix_1.toPlainText()))
        with open('C:/Users/HP/Desktop/PyQt5/Matrix_2.txt', 'w') as your_File:
            your_File.write(str(self.ui.plainTextEditMatrix_2.toPlainText()))
        A = np.loadtxt('C:/Users/HP/Desktop/PyQt5/Matrix_1.txt')
        B = np.loadtxt('C:/Users/HP/Desktop/PyQt5/Matrix_2.txt')
        columns = int(A.shape[1])
        rows = int(B.shape[0])
        C = np.zeros((rows, columns))
        if(self.ui.radioButtonStayAlgoMultiptication.isChecked()):
          if(columns != rows):
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Ошибка!")
            msg.setText("Умножить нельзя")
            msg.setIcon(msg.Warning)
            msg.exec()
          else:
              C = Matrix_Multiply(A,B)
          self.ui.plainTextEditResultMultiplicationMatrix.setPlainText(str(C))
        if(self.ui.radioButtonPerebor.isChecked()):
            for i in range(len(A)):
                for j in range(len(B[0])):
                    if(C[i][j] == 0):
                        for k in range(len(B)):
                            C[i][j] += A[i][k] * B[k][j]
            self.ui.plainTextEditResultMultiplicationMatrix.setPlainText(str(C))
        if(self.ui.radioButtonMaxBuyPodTasks.isChecked()):
            n = len(A)
            for i in range(n):
                C[i][i] = 0
            for l in range(2,n):
                for i in range(1,n-l+1):
                    j=i+l-1
                    C[i][j] = 10000
                    for k in range(i,j-1):
                        q = C[i][k]+C[k+1][j]
                        if(q < C[i][j]):
                            C[i][j] = q
                            B[i][j] = k
            for i in range(len(A)):
                for j in range(len(B[0])):
                    if(C[i][j] == 0):
                        for k in range(len(B)):
                            C[i][j] += A[i][k] * B[k][j]
            self.ui.plainTextEditResultMultiplicationMatrix.appendPlainText(str(C))
            self.ui.plainTextEditResultMultiplicationMatrix.appendPlainText("\n"+str(B))
        if(self.ui.radioButtonOptimalRastBackets.isChecked()):
            C = Matrix_Chain_Multiply(A,B,0,0)
            self.ui.plainTextEditResultMultiplicationMatrix.appendPlainText(str(C))
        if(self.ui.radioButtonRekyrsyvniyAlgoMultiplicationMatrix.isChecked()):
            CountsNumbers = Recursive_Matrix_Chain(A,B)
            self.ui.plainTextEditResultMultiplicationMatrix.appendPlainText(str(CountsNumbers))
        if(self.ui.radioButtonMemoizationMultiplicationMatrix.isChecked()):
            Ci = Memomization_Matrix(A,B)
            self.ui.plainTextEditResultMultiplicationMatrix.appendPlainText(str(Ci))
        if(self.ui.radioButtonAlgoInputResultMultiplicationMatrixRasstavSkobkamyNaScreen.isChecked()):
            n = len(A)
            bracket = str("")
            matrixChainOrder(A,n)
            bracket = printParenthesis(1,n-1,A,'A',bracket)
            self.ui.plainTextEditResultMultiplicationMatrix.appendPlainText(str(bracket))

def Matrix_Multiply(A,B):
    columns = int(A.shape[1])
    rows = int(B.shape[0])
    C = np.zeros((rows, columns))
    for i in range(len(A)):
        for j in range(len(B[0])):
                if(C[i][j] == 0):
                    for k in range(len(B)):
                        C[i][j] += A[i][k] * B[k][j]
    return C

def Matrix_Chain_Multiply(A, s, i, j):
        if j > i:
            X = Matrix_Chain_Multiply(A, s, i, s[i][j])
            Y = Matrix_Chain_Multiply(A, s, s[i][j]+1, j)
            return Matrix_Multiply(X,Y)
        else:
            return A

def Recursive_Matrix_Chain(m1,m2):
    s=0     #сумма
    t=[]    #временная матрица
    m3=[] # конечная матрица
    if len(m2)!=len(m1[0]):
         msg = QtWidgets.QMessageBox()
         msg.setWindowTitle("Ошибка!")
         msg.setText("Умножить нельзя")
         msg.setIcon(msg.Warning)
         msg.exec()        
    else:
        r1=len(m1) #количество строк в первой матрице
        c1=len(m1[0]) #Количество столбцов в 1   
        r2=c1           #и строк во 2ой матрице
        c2=len(m2[0])  # количество столбцов во 2ой матрице
        for z in range(0,r1):
            for j in range(0,c2):
                for i in range(0,c1):
                   s=s+m1[z][i]*m2[i][j]
                t.append(s)
                s=0
            m3.append(t)
            t=[]

    return m3
def Memomization_Matrix(A,B):
    res =[[0for x in range(A.shape[1])] for y in range(B.shape[1])] 
    for i in range(len(A)): 
        for j in range(len(B[0])): 
            for k in range(len(B)): 
                # resulted matrix 
                res[i][j] +=A[i][k] *B[k][j] 
    return res
def matrixChainOrder(p,n):
    m = np.zeros((n,n))
    bracket = np.zeros((n,n))
    for i in range(1,n):
        m[i][i] = 0
    for L in range(2,n):
        for i in range(1,n-L+1):
            j = i+L-1
            m[i][j] = 100000
            for k in range(i,j-1):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if(q < m[i][j]):
                    m[i][j] = q
                    bracket[i][j] = k

def printParenthesis(i,j,bracket,name,strl):

   if (i == j):
    strl +=name
    return

    strl += "("

    printParenthesis(i, bracket[i][j], bracket, name)

    printParenthesis(bracket[i][j]+1, j, bracket, name)

    strl += ")"
    return strl

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
