def LineAnalysis(line: str) -> bool:

    count = 0
    count1 = 0
    length = 0
    spisok = []

    for j in line:
        if line[0] == j:
            count1 += 1
        if count1 == len(line):
            return True

    if len(line) == 3 and line[0] == '*' and line[2] == '*':
        return True

    for i in line:
        length += 1
        if i == '*':
            count += 1
        if i == '*' and count > 1:
            break

    length -= 1

    for i in range(0, len(line), length):
        spisok.append(line[i:i + length])

    spisok.pop(len(spisok) - 1)

    if len(set(spisok)) == 1:
        return True
    return False