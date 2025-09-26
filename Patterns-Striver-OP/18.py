n = 5

a = ord("A") # get the ascii code

for i in range(0, n):
    for j in range(a+(n-1),a+(n-2)-i,-1):
        print(chr(j), end="")
    print()
    
"""

E
ED
EDC
EDCB
EDCBA

"""