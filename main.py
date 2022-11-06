from solve import *

items = [1,9,4,9,9,4,0,5,9,0]

solve(items)
print(items)
print((int)(5/2))

def test():
    first_line = input().split()
    numValues  = int(first_line[0])

    items = []
    for j in range(1, numValues+1):
        parts      = input().split()
        items.append (int(parts[0]))