a = ord("A") # get the ascii code
n = 4

for i in range(0, n):
    for j in range(1,n-i):
        print(" ", end="")
    for k in range(a,a+(i+1)):
        print(chr(k), end="")
    for l in range(a-1+i,a-1,-1):
        print(chr(l), end="")
    print()


"""
   A
  ABA
 ABCBA
ABCDCBA
"""