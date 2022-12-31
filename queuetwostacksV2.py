class Queue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, item):
        self.s1.append(item)

    def size1(self):
        return len(self.s1)

    def size2(self):
        return len(self.s2)

    def transfer(self):
        for i in range(self.size1()):
            self.s2.append(self.s1[-1])
            self.s1.pop()

    def dequeue(self):
        if self.size1() == 0 and self.size2() == 0:
            return None
        if self.size2() == 0:
            self.transfer()
        self.s2.pop()
