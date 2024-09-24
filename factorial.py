def n_factorial(n):
    if n == 1:
        return 1
    else:
        prod = n * n_factorial(n - 1)
    return prod


print(n_factorial(3))