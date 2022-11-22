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

    for i in range(len(line)):
        length += 1
        if line[i] == '*':
            count += 1
        if line[i] == '*' and count > 1 and line[i - 1] == '.':
            break

    length -= 1

    for i in range(0, len(line), length):
        spisok.append(line[i:i + length])

    if len(spisok[len(spisok) - 1]) == (count - 1):
        spisok.pop(len(spisok) - 1)
        if len(set(spisok)) == 1:
            return True
    return False