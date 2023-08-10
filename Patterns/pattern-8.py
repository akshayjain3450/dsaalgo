num = int(input("Read a number: "))
row = 1
while(row <= num):
    col = 1
    count = row
    while(col <= row):
        print(count, end=" ")
        col = col + 1
        count = count + 1
    print()
    row += 1

# while(row <= num):
#     col = row
#     while(col < row*2):
#         print(col, end=" ")
#         col = col + 1
#     print()
#     row += 1