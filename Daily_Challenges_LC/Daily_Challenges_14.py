class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # dp[j] = total champagne poured into glass j of the current row
        dp = [0.0] * (query_row + 1)
        dp[0] = poured

        for i in range(query_row):
            new_dp = [0.0] * (query_row + 1)
            for j in range(i + 1):
                overflow = dp[j] - 1.0
                if overflow > 0:
                    new_dp[j]     += overflow / 2.0
                    new_dp[j + 1] += overflow / 2.0
            dp = new_dp

        return min(1.0, dp[query_glass])
    
# Example Usage:
sol = Solution()
print(sol.champagneTower(1, 1, 1))  # Output: 0.0
print(sol.champagneTower(2, 1, 1))  # Output: 0.5
print(sol.champagneTower(100000009, 33, 17))  # Output: 1.0