print('Введите число, до которого мы будем двигаться')
n = int(input())
from time import time
start = time()
n1 = 0
n2 = 1
i = int()
a = int()
b = int()
c = int()
a = 0
b = 1
for i in range(2,n):
    c = a+b
    a = b
    b = c
print(c)
end = time()
print('Время: ')
print(end - start)
