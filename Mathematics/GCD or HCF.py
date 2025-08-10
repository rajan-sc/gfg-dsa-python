# Real life example is like you have to fill tiles in your floor of size (4 X 6) so its like gcd
# a = 4 , b = 6 
# gcd = 2

def gcd(a, b):
    """
    Compute GCD using subtraction-based Euclidean algorithm.
    Slower than modulo method but same correctness.
    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

print(gcd(4, 6))


def modulo_gcd(a, b):
    if b == 0:
        return a
    return modulo_gcd(b, a % b)


    