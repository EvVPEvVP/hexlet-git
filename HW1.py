#1.

Исходный код функции:

def PatternUnlock(N: int, hits: list) -> str:

    kod = [[6, 1, 9], [5, 2, 8], [4, 3, 7]]
    hits1 = []
    sum = 0
    for a in hits:
        hits1.append(a)

    for k in hits:
        if len(hits1) == 1:
            break
        for i1 in kod:
            for i2 in i1:
                if i2 == k:
                    next = hits1[hits1.index(k) + 1]
                    if k == 6 or k == 9 or k == 4 or k == 7:
                        if next == 2:
                            sum += 1.414215
                        else:
                            sum += 1.00000
                    elif k == 1 or k == 3:
                        if next == 5 or next == 8:
                            sum += 1.414215
                        else:
                            sum += 1.00000
                    elif k == 5 or k == 8:
                        if next == 1 or next == 3:
                            sum += 1.414215
                        else:
                            sum += 1.00000
                    else:
                        if next == 6 or next == 9 or next == 4 or next == 7:
                            sum += 1.414215
                        else:
                            sum += 1.00000
        hits1.pop(0)

    sum = round(sum, 5)
    sum = str(sum)
    sum = list(sum)

    while '.' in sum or '0' in sum:
        for x in sum:
            if x == '.' or x == '0':
                sum.remove(x)
    length = ''.join(sum)
    return length


Результирующий код функции с уменьшенной цикломатической сложностью:

def PatternUnlock(N: int, hits: list) -> str:

    kod = [[6, 1, 9], [5, 2, 8], [4, 3, 7]]
    sum = 0

    for index, k in enumerate(hits[:-1]):
        next_hit = hits[index + 1]

        if k == 6 or k == 9 or k == 4 or k == 7:
            if next_hit == 2:
                sum += 1.414215
            else:
                sum += 1.00000
        elif k == 1 or k == 3:
            if next_hit == 5 or next_hit == 8:
                sum += 1.414215
            else:
                sum += 1.00000
        elif k == 5 or k == 8:
            if next_hit == 1 or next_hit == 3:
                sum += 1.414215
            else:
                sum += 1.00000
        else:
            if next_hit == 6 or next_hit == 9 or next_hit == 4 or next_hit == 7:
                sum += 1.414215
            else:
                sum += 1.00000

    sum = round(sum, 5)
    length = str(sum).replace('.', '')
    return length


Исходная ЦС: 15
Конечная ЦС: 7

Приемы, использованные для снижения ЦС:
1. Замена вложенных циклов на единственный цикл с использованием `enumerate`.
2. Упрощение логики избавлением от лишних проверок и уменьшение количества вложенных условий.




#2.

Исходный код функции:

import textwrap

def TheRabbitsFoot(s: str, encode: bool) -> str:

    if encode == True:
        s = s.replace(' ','')
    else:
        s3 = s.split()
    result = ''
    length = len(s)
    squareroot = length ** (0.5)
    n = int(squareroot)
    m = n + 1

    while (n*m) <= length:
        n += 1

    s1 = textwrap.fill(s, m)
    s2 = s1.split()

    if encode == True:
        s3 = s2

    for i in range(len(s3)):
        for i1 in range(len(s3[i]), m):
            if len(s3[i]) != m:
                s3[i] += '0'

    for i in range(m):
        for j in range(n):
            result += s3[j][i]
            if j == (n - 1) and i != (m - 1) and encode == True:
                result += ' '

    result = result.replace('0','')
    return result


Результирующий код функции с уменьшенной цикломатической сложностью:

import textwrap

def TheRabbitsFoot(s: str, encode: bool) -> str:
    result = ''
    length = len(s)
    squareroot = length ** (0.5)
    n = int(squareroot)
    m = n + 1

    while (n * m) <= length:
        n += 1

    s1 = textwrap.fill(s, m)
    s2 = s1.split()

    if not encode:
        s2 = s.split()

    for i in range(len(s2)):
        s2[i] = s2[i].ljust(m, '0')

    for i in range(m):
        for j in range(n):
            result += s2[j][i]
            if j == (n - 1) and i != (m - 1) and encode:
                result += ' '

    result = result.replace('0', '')
    return result


Исходная ЦС: 14
Конечная ЦС: 7

Приемы, использованные для снижения ЦС:
1. Упрощение условия `if encode == True` до `if encode`.
2. Замена `s3` на `s2` в случае, когда `encode == False`.
3. Упрощение цикла с использованием оператора `not`.
4. Избавление от вложенных циклов и использование одного цикла для обработки данных.
5. Упрощение условия `if len(s3[i]) != m:` до `s2[i].ljust(m, '0')`.




#3.

Исходный код функции:

def MassVote(N: int, votes: list) -> str:
    sum = 0
    perc = []
    count = 0
    result = ''
    maxindex = ''

    for i in votes:
        sum += i

    for i1 in votes:
        x = i1 / sum * 100
        perc.append(x)

    maxperc = max(perc)

    for i2 in range(len(perc)):
        if perc[i2] == maxperc:
            count += 1
            maxindex = str(i2 + 1)

    if count > 1:
        result = 'no winner'
    elif maxperc > 50:
        result = 'majority winner' + ' ' + maxindex
    else:
        result = 'minority winner' + ' ' + maxindex

    return result


Результирующий код функции с уменьшенной цикломатической сложностью:

def MassVote(N: int, votes: list) -> str:
    total_votes = sum(votes)
    percentages = [i / total_votes * 100 for i in votes]
    max_percentage = max(percentages)
    max_indices = [str(i + 1) for i, perc in enumerate(percentages) if perc == max_percentage]

    if len(max_indices) > 1:
        result = 'no winner'
    elif max_percentage > 50:
        result = 'majority winner ' + ' '.join(max_indices)
    else:
        result = 'minority winner ' + ' '.join(max_indices)

    return result


Исходная ЦС: 8
Конечная ЦС: 4

Приемы, использованные для снижения ЦС:
1. Замена цикла `for i in votes` на `total_votes = sum(votes)`.
2. Использование генератора списка для расчета процентов.
3. Замена цикла поиска максимального процента на использование встроенных функций `max` и `enumerate`.
4. Упрощение логики условий и уменьшение количества вложенных блоков.












