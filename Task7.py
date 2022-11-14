import textwrap

def WordSearch(n: int,s: str, subs: str) -> list:

    x1 = textwrap.fill(s,n)
    x2 = x1.split('\n')
    subs1 = ' ' + subs + ' '
    result = []
    for k in x2:
        if subs1 in (" " + k + " "):
            result.append(1)
        else:
            result.append(0)
    return result
