class PowerSet:

    def __init__(self):
        self.slots = []

    def size(self):
        return len(self.slots)

    def put(self, value):
        if self.get(value) is True:
            return None
        self.slots.append(value)

    def get(self, value):
        if value in self.slots:
            return True
        return False

    def remove(self, value):
        if self.get(value) is True:
            self.slots.remove(value)
            return True
        return False

    def intersection(self, set2):
        set1 = PowerSet()
        for i in set2.slots:
            if self.get(i) is True:
                set1.put(i)
        return set1

    def union(self, set2):
        set1 = PowerSet()
        if len(set2.slots) == 0 and self.size() == 0:
            return set1
        for i in self.slots:
            set1.put(i)
        for j in set2.slots:
            set1.put(j)
        return set1

    def difference(self, set2):
        set1 = PowerSet()
        for i in self.slots:
            if set2.get(i) is False:
                set1.put(i)
        return set1

    def issubset(self, set2):
        count = 0
        for i in self.slots:
            for j in set2.slots:
                if i == j:
                    count += 1
        if count == len(set2.slots):
            return True
        return False
