class Fancy:
    MOD = 10**9 + 7

    def __init__(self):
        self.seq = []
        self.add = 0
        self.mul = 1

    def append(self, val: int) -> None:
        self.seq.append((val - self.add) * pow(self.mul, self.MOD - 2, self.MOD) % self.MOD)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = self.mul * m % self.MOD
        self.add = self.add * m % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mul + self.add) % self.MOD

# Example Usage:
if __name__ == "__main__":
    fancy = Fancy()
    fancy.append(2)
    fancy.addAll(3)
    fancy.append(7)
    fancy.multAll(2)
    print(fancy.getIndex(0))  # Output: 10
    print(fancy.getIndex(1))  # Output: 13
    print(fancy.getIndex(2))  # Output: 14