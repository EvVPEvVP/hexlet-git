class Deque:

    def __init__(self):
        self.stack = []

    def addFront(self, item):
        if self.size() == 0:
            self.stack.append(item)
        else:
            self.stack.insert(0, item)

    def addTail(self, item):
        self.stack.append(item)

    def removeFront(self):
        if self.size() == 0:
            return None
        x = self.stack[0]
        self.stack.pop(0)
        return x

    def removeTail(self):
        if self.size() == 0:
            return None
        y = self.stack[-1]
        self.stack.pop()
        return y

    def size(self):
        return len(self.stack)

    def palindrome(self):
        if self.size() == 0 or self.size() == 1:
            return True
        while self.size() > 1:
            if self.removeFront() != self.removeTail():
                return False
        return True
