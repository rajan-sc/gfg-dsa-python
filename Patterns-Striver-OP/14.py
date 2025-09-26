# using chr(take a  ascii number and convert it to string )
# ord("A") to get the ascii no.

n = 5
a = ord("A") # get the ascii code

for i in range(1, n+1):
    for j in range(a,65+i):
        print(chr(j), end="")
    print()

"""
A
AB
ABC
ABCD
ABCDEk
"""