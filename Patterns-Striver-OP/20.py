n = 9

part = n//2 #4 for now


for i in range(0, part):
    # pattern 1 part
    for p1 in range(0,i+1):
        print("*", end="")

    # blank
    for b1 in range((n-1),(i*2),-1):
        print(" ", end="")
    
    # pattern 2 part
    for p2 in range(0,i+1):
        print("*", end="")
    
    print()

for j in range(0,(n+1)):
    print("*", end="")
print()


for k in range(0, part):
    # pattern 1 part
    for p3 in range(part,k,-1):
        print("*", end="")

    # blank
    for b2 in range(0,(k*2)+2):
        print(" ", end="")
    
    # pattern 2 part
    for p4 in range(part,k,-1):
        print("*", end="")
    
    print()


    


"""

*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

"""


    
    
    














