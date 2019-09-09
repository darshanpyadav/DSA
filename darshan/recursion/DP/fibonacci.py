m = {0: 1, 1: 1}


def fib(n):
    if n not in m:
        m[n] = fib(n-1) + fib(n-2)
    return m[n]