class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        ans = []

        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):
                vals = []
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        vals.append(grid[r][c])
                
                vals.sort()
                min_diff = float('inf')
                for x in range(1, len(vals)):
                    if vals[x] != vals[x - 1]:
                        min_diff = min(min_diff, vals[x] - vals[x - 1])
                
                row.append(0 if min_diff == float('inf') else min_diff)
            ans.append(row)
        
        return ans


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    k = 2
    print(sol.minAbsDiff(grid, k))  # Output: [[1, 1], [1, 1]]