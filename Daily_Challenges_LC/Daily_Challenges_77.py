class Solution:
    def mirrorDistance(self, n: int) -> int:
        temp = n
        rev = 0
        while temp > 0:
            rev = rev * 10 + (temp % 10)
            temp //= 10
        return abs(n - rev)


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    n = 123
    print(sol.mirrorDistance(n))  # Output: 198