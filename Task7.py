def WordSearch(n: int,s: str, subs: str) -> list:

    s1 = list(s)
    length = 0
    length1 = 0
    x = ''
    x1 = ''
    count = 0
    m = False

    if len(s) == n:
        x1 = s
        m = True

    for i in s1:
        if m == True:
            break
        count += 1
        x += i
        length += 1
        length1 += 1
        if i == ' ' and length <= n:
            x1 += x
            x = ''
            length1 = 0
        elif length > (n+1) and length1 < n:
            x1 += '\n'
            length = len(x)
            length1 = len(x)
        elif length == n and s1[count] == ' ':
            x1 += x
            x1 += '\n'
            x = ''
            s1.pop(count)
            length = len(x)
            length1 = len(x)
        elif length1 >= n:
            x1 += x
            x = ''
            length1 = 0
        elif count == len(s1):
            x1 += x

    x2 = x1.split('\n')
    subs1 = ' ' + subs + ' '
    result = []
    for k in x2:
        if subs1 in (" " + k + " "):
            result.append(1)
        else:
            result.append(0)
    return result
