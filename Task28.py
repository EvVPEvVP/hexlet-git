def Keymaker(k: int) -> str:

    lst = []
    count = 0
    result = ''

    for i in range( k +1):
        lst.append(0)

    for i in range(len(lst ) -1):
        count += 1
        for j in range(0 ,len(lst) ,count):
            if lst[j] == 1:
                lst[j] = 0
            else:
                lst[j] = 1
    resultlst = lst[1:]

    for i in resultlst:
        result += str(i)

    return result