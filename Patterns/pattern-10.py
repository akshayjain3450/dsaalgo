num = int(input("Read a number: "))
row = 65
counter = row + num
while(row < counter):
    col = 1
    while(col <= num):
        print(chr(row), end=" ")
        col += 1
    print()
    row += 1