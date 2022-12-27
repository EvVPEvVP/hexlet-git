import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        if i == self.__len__():
            self.append(itm)
            return None
        self.__getitem__(i)
        self.append(itm)
        for k in range(self.count - 1, i,-1):
            self.array[k - 1], self.array[k] = self.array[k], self.array[k - 1]

    # def delete(self, i):
    #     if self.count == 0:
    #         return None
    #     self.__getitem__(i)
    #     if i == self.count - 1:
    #         self.array[i] = 0
    #         self.count -= 1
    #         return None
    #     for k in range(i, self.count - 1):
    #         self.array[k] = self.array[k + 1]
    #     self.array[self.count-1] = 0
    #     self.count -= 1

    def delete(self, i):
        new_array = self.make_array(self.capacity)
        x = 0
        for k in range(self.count):
            if k + x == self.count:
                self.array = new_array
                return None
            if k != i:
                new_array[k] = self.array[k + x]
            elif k == i:
                x += 1
                new_array[k] = self.array[k + x]
