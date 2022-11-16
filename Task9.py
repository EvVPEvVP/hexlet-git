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


