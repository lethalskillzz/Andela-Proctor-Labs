def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)
def iterative_factorial(n):
    x = 1
    li = list(range(1, n + 1))
    for each in li:
        x = x * each
    return x       
