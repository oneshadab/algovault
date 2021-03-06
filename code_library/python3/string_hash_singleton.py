MAX_LENGTH = 10**5  # Set max_length of text here


class StringHash:
    class __Hasher:
        def __init__(self, base=997, mod=10 ** 18 + 3, max_length=MAX_LENGTH):
            self.base = base
            self.mod = mod

            n = max_length + 2
            self.power = [1] * n
            for i in range(1, n):
                self.power[i] = self.power[i - 1] * self.base % self.mod

    hasher = None

    def __init__(self, text):
        if not StringHash.hasher:
            StringHash.hasher = StringHash.__Hasher()  # Singleton pattern for speed

        n = len(text)
        base = StringHash.hasher.base
        mod = StringHash.hasher.mod

        self.prefix_hash = [0] * (n + 2)
        for i in range(1, n + 1):
            self.prefix_hash[i] = (self.prefix_hash[i - 1] * base
                                   + ord(text[i - 1]) + 13) % mod

    def get_hash(self, l, r):
        h = (self.prefix_hash[r + 1] - StringHash.hasher.power[r - l + 1] * self.prefix_hash[l]) % StringHash.hasher.mod
        return h + StringHash.hasher.mod if h < 0 else h


def main():
    sh = StringHash('abracadabra')

    print(sh.get_hash(0, 0) == sh.get_hash(3, 3))   # True
    print(sh.get_hash(0, 3) == sh.get_hash(7, 10))  # True
    print(sh.get_hash(0, 4) == sh.get_hash(5, 9))   # False


if __name__ == '__main__':
    main()
