def find_second_largest(lst):
    if lst[0] > lst[1]:
        max1 = lst[0]
        max2 = lst[1]
    else:
        max1 = lst[1]
        max2 = lst[0]
    second_largest = find_second_largest_recursive(lst,max1, max2, 2)
    return second_largest

def find_second_largest_recursive(lst, max1, max2, index):
    if index == len(lst):
        return max2
    elif lst[index] >= max1:
        max2 = max1
        max1 = lst[index]
    elif lst[index] > max2:
        max2 = lst[index]
    return find_second_largest_recursive(lst, max1, max2, index+1)

