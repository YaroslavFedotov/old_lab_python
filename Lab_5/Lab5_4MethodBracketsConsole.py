def possible_groupings(n):
    print("Метод оптимальной расстановки скобок")
    total = 0
    if(n == 1):
        print('A')
        total = total + 1
    elif(n == 2):
        print('AB')
        total = total + 1
    else:
        a = 2
        substr = ''
        while(a <= n-1):
            b = 0
            d = 0
            while((b+a) <= (n )):
                c = b = d
                while(d <= c):
                    substr = substr + chr(65+d)
                    d = d + 1

            if substr != '':
                if len(substr) == 1:
                    print(substr,end = '')
                else:
                    print('(' + substr + ')',end = '')
            a = a +1
        print('(',end = '')
        while(c < (b+a)):
            print(chr(65 + c),end = '')
            c = c + 1
        print(')',end = '')

        e = b+a

        substr = ''
        while(e < n):
            substr = substr + chr(65 + e)
            e = e + 1
        if substr != '':
            if len(substr) == 1:
                print( substr,end = '')
            else:
                print('(' + substr + ')',end = '')
        print('')

        total = total + 1

        b = b + 1
    a = a + 1
    print('Варинты: ' + str(total))

possible_groupings(4)