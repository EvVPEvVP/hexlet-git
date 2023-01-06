class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.slots = [0] * f_len

    def hash1(self, str1):
        x = 0
        for c in str1:
            code = ord(c)
            x = (code + (x * 17)) % self.filter_len
        x = self.dec_bin(x)
        return x

    def hash2(self, str1):
        x1 = 0
        for c in str1:
            code = ord(c)
            x1 = (code + (x1 * 223)) % self.filter_len
        x1 = self.dec_bin(x1)
        return x1

    def add(self, str1):
        l1 = self.hash1(str1)
        l2 = self.hash2(str1)
        self.slots[self.bin_dec(l1)] = 1
        self.slots[self.bin_dec(l2)] = 1

    def is_value(self, str1):
        l1 = self.hash1(str1)
        l2 = self.hash2(str1)
        if self.slots[self.bin_dec(l1)] == 1 and self.slots[self.bin_dec(l2)] == 1:
            return True
        return False

    def dec_bin(self, y):
        b = ''
        while y > 0:
            b = str(y % 2) + b
            y = y // 2
        return b

    def bin_dec(self, y1):
        num = 0
        len_dat = len(y1)
        for i in range(0, len_dat):
            num += int(y1[i]) * (2 ** (len_dat - i - 1))
        return num




