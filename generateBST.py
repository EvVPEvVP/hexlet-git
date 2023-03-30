def GenerateBBSTArray(a):
    sorted_a = sorted(a)
    bst = [None] * len(sorted_a)

    def build_bst(start, end, parent_index):
        if start > end:
            return None

        mid_index = (start + end) // 2

        bst[parent_index] = sorted_a[mid_index]

        build_bst(start, mid_index - 1, 2 * parent_index + 1)
        build_bst(mid_index + 1, end, 2 * parent_index + 2)

    build_bst(0, len(sorted_a) - 1, 0)

    return bst


