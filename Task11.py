def BigMinus(str1: str, str2: str) -> str:

    if str1 == str2:
        return '0'

    n1 = len(str1)
    n2 = len(str2)

    if (n1 < n2):
        str1, str2 = str2, str1
    if (n2 < n1):
        str1, str2 = str1, str2

    for i in range(n1):
        if n1 == n2:
            if (str1[i] < str2[i]):
                str1, str2 = str2, str1
            elif (str1[i] > str2[i]):
                str1, str2 = str1, str2

    Str = ""

    n1 = len(str1)
    n2 = len(str2)
    diff = n1 - n2

    carry = 0

    for i in range(n2 - 1, -1, -1):
        sub = ((ord(str1[i + diff]) - ord('0')) -
               (ord(str2[i]) - ord('0')) - carry)

        if (sub < 0):
            sub += 10
            carry = 1
        else:
            carry = 0

        Str += chr(sub + ord('0'))

    for i in range(n1 - n2 - 1, -1, -1):
        if (str1[i] == '0' and carry):
            Str += '9'
            continue

        sub = (ord(str1[i]) - ord('0')) - carry

        if (i > 0 or sub > 0):
            Str += chr(sub + ord('0'))

        carry = 0

    Str = Str[::-1]

    Str = list(Str)
    for j in range(len(Str)):
        if Str[j] != '0':
            break
        Str[j] = ''
    Str = ''.join(Str)

    return Str