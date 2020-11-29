print('Задача о черепашке\n Требуется используя движение только вправо и вверх\n достигнуть верхнего правого края доски\nТип принцип задачи: решения с подзадачей')
import numpy as np
def Max(a,b):
    if a>b:
        return a
    else:
        return b

f = open('Выполнино_задачи_python\Лабораторные работы\Lab_3/RTask2.txt', 'w')
A = np.array([[5,14,27,36],[8,21,39,47],[18,32,52,63],[27,40,58,65]])
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
        
f.write(str(B))
print('Результат:')
f.write(str(B[N-1,N-1]))
f.close()
print(B[N-1,N-1])

