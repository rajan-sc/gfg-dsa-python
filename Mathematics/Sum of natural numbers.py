def sum_forloop(n):
    a = 0
    for i in range(1, n+1):
        a += i
    print(a)
# loop is going to take a lot of time 


def sum_formula(n):
    a = n*(n+1)//2
    print(a)
# single / for division and double // for floor division  
# formula is always better because of the complexity

def sum_natural_recur(n):
    if n == 1 or n == 0:
        return 1
    return n + sum_natural_recur(n - 1)



