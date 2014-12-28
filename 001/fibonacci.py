def fibonacci_recursive(n):

    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):

    fib = {}
    fib[0] = 0
    fib[1] = 1

    for i in range(2, n+1):
        fib[i] = fib[i-2] + fib[i-1]

    return fib[n]

def fibonacci_efficient(n):

    if n == 0 or n == 1:
        return n

    fib_prev = 0
    fib_curr = 1

    for i in range(2, n+1):
        fib_temp = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_temp

    return fib_curr
