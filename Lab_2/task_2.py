import numpy as np
def Solve(n,m):
    A = np.array([[0, 0, 0,0,0], [0, 0, 0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1],[1,1,1,1,1]])
    B = np.array([[3,4],[2,3]])
    i = int()
    j = int()
    l = int()
    k = int()
    max = int()
    for i in range(1,n):
        B[i,1] = A[i,1]
    for j in range(1,m):
        B[1,j] = A[1,j]
    for i in range(2,n):
        for j in range(2,m):
            if (A[i,j] == 0):
                B[i,j] = A[i,j]
            else:
                B[i,j] = min(B[i-1,j],B[i,j-1],B[i-1,j-1])+1
                max = 0
                for i in range(1,n):
                    for j in range(1,m):
                        if(B[i,j] > max):
                            max = B[i,j]
                            l = i
                            k = j
    print('Левые верхние координаты максимального квадрата', l-max+1, ' ', k-max+1)

Solve(2,2)
