class Stack:

    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() == 0:
            return None
        return self.stack.pop()

    def peek(self):
        if self.size() == 0:
            return None
        return self.stack[-1]

class Queue:

    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def transfer(self):
        for i in range(self.stack_1.size()):
            self.stack_2.push(self.stack_1.peek())
            self.stack_1.pop()

    def enqueue(self, item):
        self.stack_1.push(item)

    def dequeue(self):
        if self.stack_1.size() == 0 and self.stack_2.size() == 0:
            return None
        elif self.stack_2.size() == 0:
            self.transfer()
        x = self.stack_2.pop()
        return x
