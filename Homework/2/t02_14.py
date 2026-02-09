def a(n):
    # O(n)
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum

def b(n):
    # O(n)
    sum = 0
    for i in range(n + 1):
        sum += i * i
    return sum

def c(n, a_val):
    # O(n)
    sum = 0
    pow_a = 1
    for i in range(n + 1):
        sum += pow_a
        pow_a *= a_val
    return sum

def d(n):
    # O(n^2)
    sum = 0
    for i in range(n + 1):
        term = 1
        for j in range(i):
            term *= i
        sum += term
    return sum

def e(n):
    # O(n)
    prod = 1.0
    for i in range(1, n + 1):
        prod *= (1.0 / (1 + i))
    return prod

def f(n):
    # O(n)
    prod = 1.0
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        prod *= (1.0 / (1 + fact))
    return prod

def g(n, a):
    # O(n)
    prod = 1.0
    pow_a = 1
    fact = 1
    for i in range(1, n + 1):
        pow_a *= a
        fact *= i
        prod *= (pow_a / (1 + fact))
    return prod

def h(n, m):
    # O(nm)
    prod = 1.0
    for i in range(1, n + 1):
        pow_i_m = 1
        for j in range(m):
            pow_i_m *= i
        prod *= (1.0 / (1 + pow_i_m))
    return prod

def i(n):
    # O(n^2)
    prod = 1.0
    for i in range(1, n + 1):
        pow_i_i = 1
        for j in range(i):
            pow_i_i *= i
        prod *= (1.0 / (1 + pow_i_i))
    return prod
