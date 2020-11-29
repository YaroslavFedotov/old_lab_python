import numpy as np
def Way(i,j):
    
    f.write('i = ')
    f.write(str(i))
    f.write(' j = ')
    f.write(str(j))
    f.write(' ;\n')
    print(i, ' ',j, ' ;')
    if(i != 3 ) and (j != 3):
        if(i == 1) and (j == 1): return
        if(i == 0) and (j > 1): Way(i,j-1)
        elif(i > 1) and(j == 1): Way(i-1,j)
        else:
            if (B[i,j]-A[i,j] == B[i-1,j]):
             Way(i-1,j)
            else: Way(i,j-1)
def Min(a,b):
    if a<b:
        return a
    else:
        return b

def fact(N):
    if(N < 0):
        return 0
    if(N == 0):
        return 1
    else:
        return N * fact(N-1)
f = open('Выполнино_задачи_python\Лабораторные работы\Lab_3\RTask5.txt', 'w')
print('Найти количество способов достижения Черепашкой конечной клетки\n При условии , что та может идти:\nВправо,Вверх,По диагонали,А также по диагонали вправо и вверх\nВведите кол-во столбцов')
A = np.array([[5,14,27,36],[8,21,39,47],[18,32,52,63],[27,40,58,65]])
B = np.array([[5,19,46,82],[13,40,85,132],[31,72,137,200],[58,112,195,265]])
N = 4
B[0,0] = A[0,0]
for i in range(1,N):
    B[i,0] = B[i-1,0]+B[0,i-1]+B[i-1,0]+A[i,0]+A[i-1,0]+A[i,0];
for j in range(1,N):
    B[0,j] = B[0,j-1]+B[j-1,0]+B[0,j-1]+A[0,j]+A[0,j-1]+A[0,j]
for i in range(1,N):
    for j in range(1,N):
        B[i,j] = Min( B[i-1,j], B[i,j-1] ) + A[i,j];
        Way(i,j)


print('Результат:')
f.write(str(B[N-1,N-1]))
f.close()
print(B[N-1,N-1])
