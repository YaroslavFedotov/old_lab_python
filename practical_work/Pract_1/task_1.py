print('Введите число, до которого мы будем двигаться')
n = int(input())
fib1 = fib2 = 1
from time import time
start = time()
while n > 0:
    start = time()
    fib1,fib2 = fib2, fib1+fib2
    end = time()
    n -= 1
    print(fib2)
end = time()

print('Время: ')
if(n > 40):
    print('После 40 рекурсивный алгоритм работает медленее!')
print(end - start)
