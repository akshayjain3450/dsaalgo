row = 65
num = 65 + int(input("Read a number: "))
count = row
while(row < num):
    col = 65
    while(col < num):
        print(chr(count), end=" ")
        count += 1
        col += 1
    print()
    row += 1