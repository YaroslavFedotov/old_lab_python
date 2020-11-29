def fakt(n):
    r = int();
    r = 1
    for n in range(n,0,-1):
        r*=n;
    return r;

def bci(n,k):
    return fakt(n)/(fakt(k)*fakt(n-k));

print('Поиск Биноминальных коэффициентов через формулу факториалов ')
print('Введите число - n ,до которого будет поиск')
n = int(input())
print('Введите число - k,с которого начнём поиск')
k = int(input())
print(bci(n,k))
