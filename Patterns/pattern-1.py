num = int(input("read the number: "))
row = 1
col = 1
string = ""
while (row<=num):
    while(col<=num):
        string += "*"
        col += 1
    print(string)
    row += 1
