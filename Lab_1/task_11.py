massive = str(input())
n = int(input())
string = ""
for i in range(len(massive)):
    if int(massive[i]) == n:
        string += str(i) + " "
if string == "":
    print("Отсутствует")
else:
    print(string)
        
        
