def white_walkers(village: str) -> bool:
    result = False

    for i in range(len(village)):
        lst = []
        if not village[i].isdigit():
            continue
        for j in range(i + 1, len(village)):
            if not village[j].isdigit():
                lst.append(village[j])
            else:
                break
        if i != (len(village) - 1) and village[i].isdigit() and village[j].isdigit() and (
                int(village[i]) + int(village[j]) != 10):
            continue
        elif i != (len(village) - 1) and village[i].isdigit() and village[j].isdigit() and (
                int(village[i]) + int(village[j]) == 10) and lst.count('=') == 3:
            result = True
        elif i != (len(village) - 1) and village[i].isdigit() and village[j].isdigit() and (
                int(village[i]) + int(village[j]) == 10) and lst.count('=') != 3:
            result = False
            break

    if result:
        return True
    return False

