n = 5

a = ord("A") # get the ascii code

for i in range(0, n):
    for j in range(a,(a+n)-i):
        print(chr(a+i), end="")
    print()


"""
AAAAA
BBBB
CCC
DD
E

"""


for i in range(1, n+1):
    for j in range(a,a+i):
        print(chr(a+(i-1)), end="")
    print()

"""
A
BB
CCC
DDDD
EEEEE
"""