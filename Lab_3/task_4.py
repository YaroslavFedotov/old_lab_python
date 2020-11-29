def fact(N):
    if(N < 0):
        return 0
    if(N == 0):
        return 1
    else:
        return N * fact(N-1)
f = open('Выполнино_задачи_python\Лабораторные работы\Lab_3\RTask4.txt', 'w')
print('Найти количество способов достижения Черепашкой конечной клетки\n При условии , что та может идти:\nВправо,Вверх,По диагонали\nВведите кол-во столбцов')
n = int(input())
print('Введите кол-во строк')
m = int(input())

#Расчёт вверха функции
Up = n+m + 1
#Расчёт низа функции
Down = n- 1
#Вычисление факториала верха и низа
FactUp = fact(Up)
FactDown = fact(Down)
#Вычисление результата
Result = FactUp/(FactDown*FactDown)
f.write(str(Result))
f.close()
print('При полном переборе вариантов получившийся ответ равен: ')
print(Result)
