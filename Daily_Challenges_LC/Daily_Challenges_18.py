class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1)
        return (x & (x + 1)) == 0
    
# Example Usage:
sol = Solution()
print(sol.hasAlternatingBits(5))  # True
print(sol.hasAlternatingBits(7))  # False