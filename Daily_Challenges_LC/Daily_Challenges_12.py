class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        prefix = [[0] * 26 for _ in range(n+1)]
        
        # Build prefix frequency
        for i in range(n):
            for j in range(26):
                prefix[i+1][j] = prefix[i][j]
            prefix[i+1][ord(s[i]) - ord('a')] += 1
        
        max_len = 0
        
        # Check substrings
        for i in range(n):
            for j in range(i+1, n+1):
                freq = [prefix[j][k] - prefix[i][k] for k in range(26)]
                nonzero = [f for f in freq if f > 0]
                if nonzero and len(set(nonzero)) == 1:
                    max_len = max(max_len, j - i)
        
        return max_len
    
# Example Usage:
if __name__ == "__main__": 
    sol = Solution()
    print(sol.longestBalanced("aabbcc")) # Output: 6 print(sol.longestBalanced("abcde")) # Output: 2