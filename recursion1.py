def power(n, m):
    if m == 0:
        return 1
    elif m % 2 == 0:
        return power(n * n, m / 2)
    return n * power(n * n, (m - 1) / 2)




