a = ord("A") # get the ascii code

n = 5 

for i in range(1, n+1):
    for j in range(a,(a+n)-(i-1)):
        print(chr(j), end="")
    print()

"""
ABCDE
ABCD
ABC
AB
A

"""
