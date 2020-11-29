temp = 0
a = int(input())
b = int(input())
if b > a:
    temp = a
    a = b
    b = temp
c = int(input())
if c > a:
    temp = a
    a = c
    c = temp
elif c < b:
    temp = b
    b = c
    c = temp
print (a)
print (b)
print (c)
