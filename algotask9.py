class NativeDictionary:

    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key: str):
        x = 0
        for i in key:
            x += ord(i)
        x = x % self.size
        return x

    def is_key(self, key):
        if key in self.slots:
            return True
        return False

    def put(self, key, value):
        indx = self.hash_fun(key)
        self.slots[indx] = key
        self.values[indx] = value

    def get(self, key):
        indx = self.hash_fun(key)
        if key in self.slots:
            return self.values[indx]
        return None
