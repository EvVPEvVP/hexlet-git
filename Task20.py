elements = []
resultstring = ''
spisok = []
delspisok = []
redospisok = []
count = 0

def BastShoe(command):
    
    x = int(command.partition(' ')[0])
    x1 = command.partition(' ')[2]
    global resultstring
    global spisok
    global delspisok
    global count

    if x > 5 or x < 1:
        return resultstring
    if x == 1 and count > 0:
        spisok.clear()
        redospisok.clear()
        delspisok.clear()
        resultstring += x1
        spisok.append(x1)
        elements.append(1)
        count = 0
        return resultstring
    if x == 1 and count <= 0:
        resultstring += x1
        spisok.append(x1)
        elements.append(1)
        count = 0
        return resultstring
    if x == 2 and count > 0:
        spisok.clear()
        redospisok.clear()
        delspisok.clear()
        rem = int(x1) * -1
        delspisok.append(resultstring[rem:])
        resultstring = resultstring[:rem]
        elements.append(2)
        count = 0
        return resultstring
    if x == 2 and count <= 0:
        rem = int(x1) * -1
        delspisok.append(resultstring[rem:])
        resultstring = resultstring[:rem]
        elements.append(2)
        count = 0
        return resultstring
    if x == 3 and int(x1) <= (len(resultstring) - 1):
        return resultstring[int(x1)]
    if x == 4 and len(elements) == 0:
        return resultstring
    if x == 4 and elements[-1] == 1 and len(spisok) == 0:
        return resultstring
    if x == 4 and elements[-1] == 1 and len(spisok) > 0:
        resultstring = resultstring[:len(spisok[-1]) * -1]
        delspisok.append(spisok[-1])
        redospisok.append(delspisok[-1])
        del elements[-1]
        del spisok[-1]
        count = 1
        return resultstring
    if x == 4 and elements[-1] == 2 and (len(elements) == 0 or len(delspisok) == 0):
        return resultstring
    if x == 4 and elements[-1] == 2 and len(elements) > 0 and len(delspisok) > 0:
        resultstring += delspisok[-1]
        redospisok.append(delspisok[-1])
        del delspisok[-1]
        del elements[-1]
        count = 2
        return resultstring
    if x == 5 and len(redospisok) == 0:
        return resultstring
    if x == 5 and count == 2:
        resultstring = resultstring[:len(redospisok[-1]) * -1]
        del redospisok[-1]
        return resultstring
    if x == 5 and count != 2:
        resultstring += redospisok[-1]
        spisok.append(redospisok[-1])
        elements.append(1)
        del redospisok[-1]
        return resultstring

