def fact(N):
    if(N < 0):
        return 0
    if(N == 0):
        return 1
    else:
        return N * fact(N-1)

f = open('Выполнино_задачи_python\Лабораторные работы\Lab_3\RTask.txt', 'w')
print('Задача о черепашке\n Требуется используя движение только вправо и вверх\n достигнуть верхнего правого края доски\nТип решения задачи: Полный перебор вариантов\n Введите кол-во столбцов доски')
n = int(input())
print('Введите количество строк доски')
m = int(input())
#Расчёт вверха функции
Up = n+m - 2
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
