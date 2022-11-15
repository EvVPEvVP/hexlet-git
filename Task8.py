def SumOfThe(n: int, data: list) -> int:

    for i in range(n):
        sum = 0
        count = 0
        for k in data:
            if data[i] == k and count == 0:
                count += 1
                continue
            sum += k
        if data[i] == sum:
            return data[i]