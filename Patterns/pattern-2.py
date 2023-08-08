num = int(input("read the number: "))
row = 1
while (row <= num):
    col = 1
    while (col <= num):
        print(col, end=" ")
        col += 1
    print()
    row += 1