num = int(input("Read a number: "))
row = 1
while (row <= num):
    col = 1
    while(col <= num):
        print(chr(64+row+col-1), end=" ")
        col += 1
    print()
    row += 1