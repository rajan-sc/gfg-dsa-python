n = 10

part = n//2 #5 for now

# upper half
for i in range(0,part):
    for j1 in range(0,part-i):
        print("*", end="")
    #  blanks
    for b1 in range(0,(i*2)):
        print(" ", end="")
    for j2 in range(0,part-i):
        print("*", end="")
    print()
    
    # lower half
for i2 in range(0,part):
    for l1 in range(0,i2+1):
        print("*", end="")
    for b2 in range((n-2),(i2*2),-1):
        print(" ", end="")
    for l2 in range(0,i2+1):
        print("*", end="")
    print()


"""

**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********

"""
    