class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.slots = 0

    def hash1(self, str1):
        x = 0
        for c in str1:
            code = ord(c)
            x = (code + (x * 17)) % self.filter_len
        return x

    def hash2(self, str1):
        x1 = 0
        for c in str1:
            code = ord(c)
            x1 = (code + (x1 * 223)) % self.filter_len
        return x1

    def add(self, str1):
        a = self.dec_bin(self.slots)
        a[self.hash1(str1)] = 1
        a[self.hash2(str1)] = 1
        self.slots = self.bin_dec(a)

    def is_value(self, str1):
        a1 = self.dec_bin(self.slots)
        if a1[self.hash1(str1)] == 1 and a1[self.hash2(str1)] == 1:
            return True
        return False

    def dec_bin(self, y):
        z = []
        z1 = []
        b = ''
        while y > 0:
            b = str(y % 2) + b
            y = y // 2
        for i in b:
            z.append(int(i))
        for i in range(self.filter_len - len(z)):
            z1.append(0)
        z1 += z
        return z1

    def bin_dec(self, y1):
        num = 0
        len_dat = len(y1)
        for i in range(0, len_dat):
            num += int(y1[i]) * (2 ** (len_dat - i - 1))
        return num

