num = int(input("Read a number: "))
row = 1
while(row <= num):
    col = 1
    while (col<=row):
        print(row, end=" ")
        col += 1
    print()
    row += 1
