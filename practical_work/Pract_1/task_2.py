print('Введите число, до которого будет двигаться цикл for')
n = int(input())
F = [] 
from time import time
start = time()
F.append(0)
F.append(1)
for i in range(2,n):
    F.append(F[i-1]+F[i-2])
print(F[len(F)-1])
end = time()
print('Время: ')
print(end - start)
