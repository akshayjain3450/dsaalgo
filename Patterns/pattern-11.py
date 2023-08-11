num = int(input("Read a number: "))
row  = 65
count = row + num
while(row < count):
    col = 65
    while(col < count):
        print(chr(col), end= " ")
        col = col + 1
    print()
    row = row + 1
