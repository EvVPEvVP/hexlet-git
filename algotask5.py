class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        return self.queue.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        x = self.queue[0]
        self.queue.pop(0)
        return x

    def size(self):
        return len(self.queue)

