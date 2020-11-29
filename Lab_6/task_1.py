import numpy as np
N  = 6
V0 = 0
H0 = 0
Fuel0 = 0
FuelSmash = 0
FuelMinus0Smash = 0
TypeTask = 0
INF = 1000000
M = np.array([[INF,1,INF,3,3,INF], [INF,INF,6,INF,INF,INF],[INF,2,INF,INF,INF,9],[INF,INF,INF,4,7,INF],[INF,8,INF,INF,INF,4],[INF,INF,INF,INF,INF,INF]])
def inputDataAir():
    H0 = int(input("Введите начальную высоту самолёта: "))
    V0 = int(input("Введите начальную скорость самолёта: "))
    Fuel0 = int(input("Введите начальное количество топлива самолёта: "))
    FuelSmash = int(input("Введите конечное количество топлива самолёта: "))
    TypeTask = int(input("Задайте тип решения задачи (1/2): "))
    print("Ну что полетели!"+'\n'+"Карта пути:")
    print(M)
    print('КРАТЧАЙШИЙ ПУТЬ ПО КАРТЕ ПУТИ:')
    Dijkstra(V0,H0,Fuel0,FuelSmash,FuelMinus0Smash,TypeTask)
def Dijkstra(V0,H0,Fuel0,FuelSmash,FuelMinus0Smash,TypeTask):
    V0Default = V0
    H0Default = H0
    FuelDefault = Fuel0
    Distance = []
    Visited = []
    S = GetVertex()
    if(S == -1):
        return
    for i in range(0,N):
        Distance.append(INF)
        Visited.append(False)
    Distance[S] = 0

    MinD = int()
    while(MinD < INF):
        MinD = INF
        MinV = int(-1)
        for i in range(0,N):
            if(Distance[i] < MinD and Visited[i] == False):
                MinD = Distance[i]
                MinV = i
        H0 = H0Default
        V0 = V0Default
        Fuel0 = FuelDefault
        if(MinV == -1):
            break
        for i in range(0,N):
            if(M[MinV,i] < INF and Visited[i] == False):
                Distance[i] = min(Distance[i],Distance[MinV] + M[MinV,i])
        Visited[MinV] = True

        for i in range(0,N):
            if(Distance[i] > 0 and Distance[i] < INF):
                T = i
                R = ""
                while(T != S):
                    for j in range(0,N):
                        if(M[j,T] < INF and Distance[j] == Distance[T] - M[j,T]):
                            T = j
                            R = chr(ord('A') + T) + "-" + R
                            break
                print(R + chr(ord('A')+i))
                H0 = H0 + 1
                if(TypeTask == 2):
                    V0 = V0 + 1
                Fuel0 = Fuel0 - 1
                FuelMinus0Smash = Fuel0  - FuelSmash
                print("Текущая высота: " + str(H0))
                print("Текущая скорость: " + str(V0))
                print("Количество бензина: " + str(Fuel0))
                print("Остаток бензина до цели:" + str(FuelMinus0Smash))
                Backing = True

def GetVertex():
    ErrorConst = -1
    V = ' '
    MaxLetter = ord('A') + N - 1
    m  = chr(MaxLetter)
    V = 'A'
    if(ord(V) > ord(m)):
        return ErrorConst
    else:
        return ord(V) - ord('A')

inputDataAir()

