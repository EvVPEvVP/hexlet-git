def length_of_list(lst):
    if not lst:
        return 0
    lst.pop(0)
    return 1 + length_of_list(lst)