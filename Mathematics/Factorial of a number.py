def fact(n):
    temp = 1
    for i in range(1,n+1):
        temp *= i
    print(temp)

def fact_recur(n):
    if n == 1 or n ==0:
        return n
    else:
        return n * fact_recur(n-1)

print(fact_recur(3))
fact(3)