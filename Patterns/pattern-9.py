num = int(input("Read a number: "))
row = 1
while(row <= num):
    col = row
    while(col > 0):
        print(col, end=" ")
        col = col - 1
    print()
    row += 1

# while(row <= num):
#     col = 1
#     while(col <= row):
#         print(row - col + 1, end=" ")
#         col = col + 1
#     print()
#     row += 1