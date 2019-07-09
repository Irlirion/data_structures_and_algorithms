class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = bytearray(f_len)

    def hash1(self, str1):
        # 17
        s = 0
        for c in str1:
            code = ord(c)
            s = (s * 17 + code) % self.filter_len
        return s

    def hash2(self, str1):
        # 223
        s = 0
        for c in str1:
            code = ord(c)
            s = (s * 223 + code) % self.filter_len
        return s

    def add(self, str1):
        self.filter[self.hash1(str1)] = 1
        self.filter[self.hash2(str1)] = 1

    def is_value(self, str1):
        return self.filter[self.hash1(str1)] and self.filter[self.hash2(str1)]
