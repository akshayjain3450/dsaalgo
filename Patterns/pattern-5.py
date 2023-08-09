num = int(input("read a number: "))
row = 1
string = ""
while(row<=num):
    col = 1
    while(col<=row):
        print("*", end=" ")
        col += 1
    print()
    row += 1