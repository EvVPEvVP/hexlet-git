class NativeCache:
    
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        x = 0
        for i in key:
            x += ord(i)
        x = x % self.size
        return x

    def find(self, key):
        num = self.hash_fun(key)
        count = 0
        step_find = 3
        while True:
            if None not in self.slots:
                dlt = self.hits.index(min(self.hits))
                self.hits[dlt] = 0
                self.slots[dlt] = None
                self.values[dlt] = None
            if self.slots[num] is None:
                return num
            if self.slots[num] is not None:
                num += step_find
            if num > self.size - 1:
                num = count
                count += 1

    def put(self, key, value):
        num = self.find(key)
        self.slots[num] = key
        self.values[num] = value
        self.hits[num] += 1
