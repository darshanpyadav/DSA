def memoize(f):
    m = {0: 1, 1: 1}

    def helper(n):
        if n not in m:
            m[n] = f(n)
        return m[n]
    return helper


@memoize
def fib(n):
    return fib(n-1) + fib(n-2)


print(fib(10))
