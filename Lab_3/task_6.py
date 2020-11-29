print('Задача о черепашке\n Дана матрица с закрашенными значениями\n Требуется определить максимальный путь\n Движения: Вправо Вверх')
import numpy as np
def Max(a,b):
    if a>b:
        return a
    else:
        return b
A = np.loadtxt('Выполнино_задачи_python\Лабораторные работы\Lab_3\InputTask6.txt')
f = open('C:/Users/HP/source/repos/PyhtonProject/PyhtonProject/ResTask6.txt', 'w')
B = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
i = int(); j = int(); N = int();
N = 4
B[0,0] = A[0,0]
for i in range(1,N):
    B[i,0] = B[i-1,0]+A[i,0]
for j in range(1,N):
    B[0,j] = B[0,j-1]+A[0,j]
for i in range(1,N):
    for j in range(1,N):
        B[i,j] = Max( B[i-1,j], B[i,j-1] ) + A[i,j];

print('Результат:')
f.write(str(B[N-1,N-1]))
f.close()
print(B[N-1,N-1])

