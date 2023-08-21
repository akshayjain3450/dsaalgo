# you have to complete the compareTriplets
def compareTriplets(a, b):
    # Write your code here
    alice = 0
    bob = 0
    count = len(a) if len(a) > len(b) else len(b)
    for i in range(0, count):
        if a[i] > b[i]:
            alice += 1
        if b[i] > a[i]:
            bob += 1
    return [alice, bob]