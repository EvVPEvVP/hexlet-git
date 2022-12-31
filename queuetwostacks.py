class Queue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def size1(self):
        return len(self.s1)

    def size2(self):
        return len(self.s2)

    def enqueue(self, x):
        for i in range(self.size1()):
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(x)
        for j in range(self.size2()):
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def dequeue(self):
        if len(self.s1) == 0:
            return None
        x = self.s1[-1]
        self.s1.pop()
        return x
