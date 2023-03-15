def generate_balanced_parentheses(n):
    result = []

    def generate(s, left, right):
        if left == right and right == n:
            result.append(s)
            return
        if left < n:
            generate(s + '(', left + 1, right)
        if right < left:
            generate(s + ')', left, right + 1)

    generate('', 0, 0)
    return result
