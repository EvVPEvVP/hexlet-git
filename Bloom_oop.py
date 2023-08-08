class BloomFilter:
    def __init__(self, size, num_hashes):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [False] * size

    def _hash(self, item, seed):
        # Простая хэш-функция
        hash_val = 0
        for char in item:
            hash_val = (hash_val * seed + ord(char)) % self.size
        return hash_val

    # Postcondition: add item in array
    def add(self, item):
        for i in range(self.num_hashes):
            index = self._hash(item, i)
            self.bit_array[index] = True

    # Postcondition: is array contains the item. Return True or False
    def contains(self, item):
        for i in range(self.num_hashes):
            index = self._hash(item, i)
            if not self.bit_array[index]:
                return False
        return True