class PowerSet:

    def __init__(self):
        self.size1 = 15
        self.step = 3
        self.slots = [None] * self.size1

    def size(self):
        count = 0
        for i in self.slots:
            if i is not None:
                count += 1
        return count

    def hash_fun(self, value: str):
        x = 0
        for i in value:
            x += ord(i)
        x = x % self.size1
        return x

    def put(self, value):
        indx = self.hash_fun(value)
        count = 0
        if value in self.slots:
            return None
        while None in self.slots:
            if self.slots[indx] is None:
                self.slots[indx] = value
                return None
            if self.slots[indx] is not None:
                indx += self.step
            if indx > self.size1 - 1:
                indx = count
                count += 1
        return None

    def get(self, value):
        if value in self.slots:
            return True
        return False

    def remove(self, value):
        if self.get(value) is True:
            indx = self.hash_fun(value)
            self.slots[indx] = None
            return True
        return False

    def intersection(self, set2):
        lst = []
        for i in self.slots:
            if i in set2:
                lst.append(i)
        result = set(lst)
        return result

    def union(self, set2):
        for i in set2:
            if i in self.slots:
                continue
            self.put(i)
        return self.slots

    def difference(self, set2):
        lst = []
        for i in self.slots:
            if i not in set2 and i is not None:
                lst.append(i)
        result = set(lst)
        return result

    def issubset(self, set2):
        count = 0
        for i in set2:
            if i in self.slots and i is not None:
                count += 1
        if count == len(set2):
            return True
        return False