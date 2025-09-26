k = int(input())

n = k//2

for i in range(0,n):
    for k in range(0,i+1): 
        print("*",end="")
    print()

for j in range(0,n+1):
    print("*",end="")
print()

for i in range(0,n):
    for k in range(0,n-i): 
        print("*",end="")
    print()


    '''
*
**
***
****
*****
****
***
**
*
    '''