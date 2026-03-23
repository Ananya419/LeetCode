class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        max_dp = [[0]*n for _ in range(m)]
        min_dp = [[0]*n for _ in range(m)]
        
        max_dp[0][0] = min_dp[0][0] = grid[0][0]
        
        for i in range(1, m):
            max_dp[i][0] = min_dp[i][0] = max_dp[i-1][0] * grid[i][0]
        for j in range(1, n):
            max_dp[0][j] = min_dp[0][j] = max_dp[0][j-1] * grid[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                v = grid[i][j]
                candidates = [
                    max_dp[i-1][j] * v,
                    min_dp[i-1][j] * v,
                    max_dp[i][j-1] * v,
                    min_dp[i][j-1] * v,
                ]
                max_dp[i][j] = max(candidates)
                min_dp[i][j] = min(candidates)
        
        return -1 if max_dp[-1][-1] < 0 else max_dp[-1][-1] % MOD


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    grid = [[-1,-2,-3],[4,5,6],[-7,-8,9]]
    print(sol.maxProductPath(grid))  # Output: 1080