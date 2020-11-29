n = str(input())
e = int(n[len(n) - 1])
if e == 1:
    print(n, "Програмист")
elif 0 < e < 5:
    print(n, "Програмиста")
else:
    print(n, "Програмистов")

