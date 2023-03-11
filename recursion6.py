def print_even_index(lst, i = 0):
    if i >= len(lst):
        return
    if i % 2 == 0:
        print(lst[i])
    print_even_index(lst, i+1)