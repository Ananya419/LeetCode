class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 1

        # Case 1: single-char runs
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            ans = max(ans, j - i)
            i = j

        # Case 2: exactly 2 distinct chars, equal counts
        chars = "abc"
        for ci in range(3):
            exclude = chars[ci]
            c1 = chars[(ci + 1) % 3]
            seg_start = 0
            for i in range(n + 1):
                if i == n or s[i] == exclude:
                    if i > seg_start:
                        diff = 0
                        first_seen = {0: seg_start - 1}
                        for j in range(seg_start, i):
                            diff += 1 if s[j] == c1 else -1
                            if diff in first_seen:
                                ans = max(ans, j - first_seen[diff])
                            else:
                                first_seen[diff] = j
                    seg_start = i + 1

        # Case 3: all 3 chars, equal counts
        d1 = d2 = 0
        first_seen = {(0, 0): -1}
        for i in range(n):
            if s[i] == 'a':
                d1 += 1
            elif s[i] == 'b':
                d1 -= 1
                d2 += 1
            else:
                d2 -= 1
            key = (d1, d2)
            if key in first_seen:
                ans = max(ans, i - first_seen[key])
            else:
                first_seen[key] = i

        return ans
    
# Example Usage:
sol = Solution()
print(sol.longestBalanced("aabbcc"))  # Output: 6
print(sol.longestBalanced("abcabc"))   # Output: 6
print(sol.longestBalanced("aaabbbccc"))# Output: 9