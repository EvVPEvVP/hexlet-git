def odometer(oksana: list) -> int:

    distance = 0
    for i in range(len(oksana)):
        if i == 0:
            distance += oksana[i] * oksana[i+1]
        elif i > 0 and i % 2 == 0:
            distance += oksana[i] * (oksana[i+1]-oksana[i-1])
    return distance
