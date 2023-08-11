num = int(input("Read a number: "))
row = 1
while(row <= num):
    col = 1
    while (col <= row):
        print(chr(64 + row), end=" ")
        col = col + 1
    print()
    row += 1