def catalan_recursive(n):

    if n == 0:
        return 1

    res = 0
    for i in range(n):
        res += catalan_recursive(i) * catalan_recursive(n-i-1)

    return res

def catalan_iterative(n):

    cat = {}
    cat[0] = 1

    for i in range(1, n+1):
        cat[i] = 0
        for j in range(i):
            cat[i] += cat[j] * cat[i-j-1]

    return cat[n]

def catalan_product(n):

    res = 1
    for i in range(2, n+1):
        res *= ((n+i) / i)

    return round(res)
