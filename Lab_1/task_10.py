r = int(input())
step = int(1)
string = str("")
for x in range(r - 1):
    for i in range(step):
        if len(string) == r: 
            print(string)
            raise SystemExit()
        string += str(step) + " "
    step += 1
print(string)
