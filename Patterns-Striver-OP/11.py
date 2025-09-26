n = 5

start = 1
for i in range(1,n+1):
    if i % 2 == 0:
        start = 0
    else:
        start = 1
    for k in range(1,i+1): 
        print(start,end="")
        start = 1 - start
    print()


"""

1
01
101
0101
10101

"""