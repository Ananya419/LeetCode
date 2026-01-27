class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        need = Counter(t)
        missing = len(t)   # total chars we still need
        left = start = end = 0

        for right, ch in enumerate(s, 1):  # right is 1-based index
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            if missing == 0:  # all chars matched
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                if end == 0 or right - left < end - start:
                    start, end = left, right

        return s[start:end]
    
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(solution.minWindow(s, t))  # Output: "BANC"