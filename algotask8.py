class HashTable:

    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value: str):
        x = 0
        for i in value:
            x += ord(i)
        x = x % self.size
        return x

    def seek_slot(self, value):
        indx = self.hash_fun(value)
        count = 0
        while None in self.slots:
            if self.slots[indx] is None:
                return indx
            if self.slots[indx] is not None:
                indx += self.step
            if indx > self.size - 1:
                indx = count
                count += 1
        return None

    def put(self, value):
        indx = self.seek_slot(value)
        if indx is not None:
            self.slots[indx] = value
            return indx
        return None

    def find(self, value):
        count = 0
        indx = self.hash_fun(value)
        while value in self.slots:
            if self.slots[indx] == value:
                return indx
            if self.slots[indx] != value:
                indx += self.step
            if indx > self.size - 1:
                indx = count
                count += 1
        return None