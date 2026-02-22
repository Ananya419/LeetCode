class Solution:
    def binaryGap(self, n: int) -> int:
        last = -1  # position of the last seen 1
        ans = 0
        i = 0
        while n:
            if n & 1:
                if last >= 0:
                    ans = max(ans, i - last)
                last = i
            n >>= 1
            i += 1
        return ans
    
# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.binaryGap(22))  # Output: 2