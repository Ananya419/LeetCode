class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(c1: int, c2: int) -> int:
            return abs(c1 // 6 - c2 // 6) + abs(c1 % 6 - c2 % 6)
        
        dp = [0] * 26
        total_dist = 0
        
        for i in range(1, len(word)):
            p = ord(word[i - 1]) - 65
            c = ord(word[i]) - 65
            
            d = dist(p, c)
            total_dist += d
            
            max_save = 0
            for a in range(26):
                max_save = max(max_save, dp[a] + d - dist(a, c))
                
            dp[p] = max(dp[p], max_save)
            
        return total_dist - max(dp)


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    word = "CAKE"
    print(sol.minimumDistance(word))  # Output: 3