class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        prefix = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                prefix[r][c] = grid[r][c]
                if r > 0:
                    prefix[r][c] += prefix[r-1][c]
                if c > 0:
                    prefix[r][c] += prefix[r][c-1]
                if r > 0 and c > 0:
                    prefix[r][c] -= prefix[r-1][c-1]
                if prefix[r][c] <= k:
                    count += 1

        return count


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    grid = [[1,0,1],[0,1,0],[1,0,1]]
    k = 2
    print(sol.countSubmatrices(grid, k))  # Output: 14