
def lcm(a, b): # naive approach

    res = max(a,b)

    while True:

        if res % a == 0 and res % b == 0:
            return res
        res += 1


print(lcm(6, 4))


def modulo_gcd(a, b):
    if b == 0:
        return a
    return modulo_gcd(b, a % b)


def lcm_formulae(a, b):
    return a * b // modulo_gcd(a, b)

print(lcm_formulae(4, 6))