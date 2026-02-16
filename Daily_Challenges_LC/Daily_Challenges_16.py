class Solution:
    # Precompute reversed bytes
    lookup = [0] * 256
    for i in range(256):
        val = i
        rev = 0
        for j in range(8):
            rev <<= 1
            rev |= (val & 1)
            val >>= 1
        lookup[i] = rev

    def reverseBits(self, n: int) -> int:
        return (self.lookup[n & 0xff] << 24) | \
               (self.lookup[(n >> 8) & 0xff] << 16) | \
               (self.lookup[(n >> 16) & 0xff] << 8) | \
               (self.lookup[(n >> 24) & 0xff])
    
# Example Usage:
sol = Solution()
print(sol.reverseBits(43261596))  # Output: 964176192
print(sol.reverseBits(4294967293))  # Output: 3221225471