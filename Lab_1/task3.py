a=int(input("введите первую сторону треугольника:"))
b=int(input("введите вторую сторону треугольника:"))
c=int(input("введите третью сторону треугольника:"))
p=(a+b+c)/2
s=(p*(p-a)*(p-b)*(p-c))**0.5
print("площадь равна=",s)