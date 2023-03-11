def print_even(lst):
    if not lst:
        return
    if lst[0] % 2 == 0:
        print(lst[0])
    print_even(lst[1:])
