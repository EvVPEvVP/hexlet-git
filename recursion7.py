def find_second_largest(arr):
    largest = find_largest(arr)
    arr.remove(largest)
    return find_largest(arr)

def find_largest(arr2):
    if len(arr2) == 1:
        return arr2[0]
    return max(arr2[0], find_largest(arr2[1:]))