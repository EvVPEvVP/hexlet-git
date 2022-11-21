def MaximumDiscount(N: int, price: list) -> int:

    if N < 3:
        return 0

    price = sorted(price, reverse=True)
    price3 = []
    result = 0

    y = N // 3
    price1 = sorted(price, reverse = False)[:y]
    result1 = sum(price1)

    for i in range(0, len(price), 3):
        price3.append(price[i:i + 3])

    for j in range(len(price3)):
        x = min(price3[j])
        if len(price3[j]) == 3:
            result += x

    if result >= result1:
        return result
    return result1

