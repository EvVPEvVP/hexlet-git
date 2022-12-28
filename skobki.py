class Stack:

    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() == 0:
            return None
        return self.stack.pop()

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() == 0:
            return None
        return self.stack[-1]

    def brackets(self, x: str) -> bool:
        for i in x:
            if i == ')' and self.size() == 0:
                return False
            elif i == '(':
                self.push(i)
            elif i == ')':
                self.pop()
        if self.size() == 0:
            return True
        return False
