a=float(input("введите первое число:"))
b=float(input("введите второе число:"))
c=input("введите тип операции:")
if c=="+":
    print (a+b)
elif c=="-":
    print (a-b)
elif c=="*":
    print (a*b)
elif c=="/":
    if b==0:
        print("деление на 0!")
    else:
        print (a/b)
elif c=="pow":
    print (a ** b)
elif c=="mod":
    if b==0:
        print("деление на 0!")
    else:
        print (a % b)
elif c=="div":
    if b==0:
        print("деление на 0!")
    else:
        print (a // b)
else:
    print("введена несушествующая операция.")
