
import numpy as np
f = open('Выполнино_задачи_python\Лабораторные работы\Lab_3\RTask3.txt', 'w')
print('Задача о черепашке\n Требуется используя движение только вправо и вверх\n достигнуть верхнего правого края доски\nТип решения задачи: рекурсивный вариант')
A = np.array([[5,14,27,36],[8,21,39,47],[18,32,52,63],[27,40,58,65]])
B = np.array([[5,19,46,82],[13,40,85,132],[31,72,137,200],[58,112,195,265]])
N = int();
N = 4

def Way(i,j):
    
    f.write('i = ')
    f.write(str(i))
    f.write(' j = ')
    f.write(str(j))
    f.write(' ;\n')
    print(i, ' ',j, ' ;')

    if(i == 0) and (j == 0): 
         return
    if(i == 0) and (j > 1): Way(i,j-1)
    elif(i > 1) and(j == 1): Way(i-1,j)
    else:
        if (B[i,j]-A[i,j] == B[i-1,j]):
            Way(i-1,j)
        else: Way(i,j-1)

    
Way(N-1,N-1)
f.close()
