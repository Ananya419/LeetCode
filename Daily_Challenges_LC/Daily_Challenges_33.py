class Solution:
    def minOperations(self, s: str) -> int:
        mismatch1 = mismatch2 = 0
        for i, ch in enumerate(s):
            if ch != str(i % 2):      # pattern starting with '0'
                mismatch1 += 1
            if ch != str((i + 1) % 2): # pattern starting with '1'
                mismatch2 += 1
        return min(mismatch1, mismatch2)
    
# Example Usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.minOperations("1100"))  # Output: 2
    print(solution.minOperations("1001"))  # Output: 2