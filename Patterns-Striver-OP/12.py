n = 4
for i in range(0,n):
    for j in range(1,i+2):
        print(j, end="")
    
    for k in range(1,(2*n+1)-(2*(i+1))):
        print(" ", end="")

    for l in range(i+1,0,-1):
        print(l, end="")
    print()


"""
1      1
12    21
123  321
12344321
"""
# start the first loop with 0 and later you can add/ modify the later i values.