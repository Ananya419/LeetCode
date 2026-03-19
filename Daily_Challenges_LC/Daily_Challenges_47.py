class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        cntX = [[0] * n for _ in range(m)]
        cntY = [[0] * n for _ in range(m)]
        ans = 0
        
        for i in range(m):
            for j in range(n):
                x = 1 if grid[i][j] == 'X' else 0
                y = 1 if grid[i][j] == 'Y' else 0
                
                top  = cntX[i-1][j]   if i > 0 else 0
                left = cntX[i][j-1]   if j > 0 else 0
                diag = cntX[i-1][j-1] if i > 0 and j > 0 else 0
                cntX[i][j] = x + top + left - diag
                
                top  = cntY[i-1][j]   if i > 0 else 0
                left = cntY[i][j-1]   if j > 0 else 0
                diag = cntY[i-1][j-1] if i > 0 and j > 0 else 0
                cntY[i][j] = y + top + left - diag
                
                if cntX[i][j] == cntY[i][j] and cntX[i][j] >= 1:
                    ans += 1
        
        return ans


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    grid = [["X","Y"],["Y","X"]]
    print(sol.numberOfSubmatrices(grid))  # Output: 3
