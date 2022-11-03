def squirrel(N: int) -> int:

    fact = 1
    for i in range(1,N+1):
        fact *= i
    x = fact
    for j in range(len(str(fact))-1):
        x = x // 10
    return x