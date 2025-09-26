n = 5

for i in range(0,n):
    for k in range(0,(n-1)-i): 
        print(" ",end="")
    for j in range(0,(2*i)+1):
        print("*",end="")
    print()



"""
    *
   ***
  *****
 *******
*********
"""