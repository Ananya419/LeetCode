class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, curr, result = 0, 1, 0

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr += 1
            else:
                result += min(prev, curr)
                prev, curr = curr, 1

        result += min(prev, curr)
        return result
    
# Example Usage:
sol = Solution()
print(sol.countBinarySubstrings("00110011"))  # Output: 6
print(sol.countBinarySubstrings("10101"))     # Output: 4   