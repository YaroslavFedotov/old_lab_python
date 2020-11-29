baf = ""
p = ""
tempstr = ""
mas = []
masres = []
masdop = []
while baf != "end":
   baf = str(input())
   if baf != "end":
       mas.append([int(j) for j in baf.split(' ')])   
for f in range(len(mas)):
    if f == 0:
        for h in range (len(mas[f])):
            p += str(mas[0][h]) + ' '
        s = str(mas[0][len(mas[f]) - 1]) + ' ' + str(p) + str(mas[0][0])
        p = ""
        masdop.append([int(j) for j in s.split(' ')])
        for l in range (len(mas[f])):
            p += str(mas[len(mas) - 1 - f][l]) + ' '
        s = str(mas[len(mas) - 1 - f][len(mas[f]) - 1]) + ' ' + str(p) + str(mas[len(mas) - 1 - f][0])
        p = ""
        masdop.append([int(j) for j in s.split(' ')])
    if f == len(mas) - 1:
        for a in range (len(mas[f])):
            p += str(mas[len(mas) - 1 - f][a]) + ' ' 
        s = str(mas[len(mas) - 1 - f][len(mas[f]) - 1]) + ' ' + str(p) + str(mas[len(mas) - 1 - f][0])
        p = ""
        masdop.append([int(j) for j in s.split(' ')])
        for x in range (len(mas[f])):
            p += str(mas[f][x]) + ' '
        s = str(mas[f][len(mas[f]) - 1]) + ' ' + str(p) + str(mas[f][0])
        p = ""
        masdop.append([int(j) for j in s.split(' ')])
    if 0 < f < len(mas) - 1:     
        for v in range (len(mas[f])):
            p += str(mas[len(mas) - 1 - f][v]) + ' '     
        s = str(mas[len(mas) - 1 - f][len(mas[f]) - 1]) + ' ' + str(p) + str(mas[len(mas) - 1 - f][0])
        p = ""
        masdop.append([int(j) for j in s.split(' ')])
for i in range(1, len(mas) + 1):
    for j in range(1, len(mas[0]) + 1):
        tempstr += str(masdop[i - 1][j] + masdop[i + 1][j] + masdop[i][j - 1] + masdop[i][j + 1])
        tempstr += " "
    masres.append(tempstr)
    tempstr = ""
masres.reverse() 
for e in range(0, len(masres)):
    print(masres[e])        

