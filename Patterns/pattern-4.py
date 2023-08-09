num = int(input("read a number: "))
row = 1
count = 1
while(row<=num):
    col = 1
    while(col<=num):
        print(count, end=" ")
        count += 1
        col += 1
    print()
    row += 1