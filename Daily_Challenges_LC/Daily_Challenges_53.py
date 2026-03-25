class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = sum(grid[i][j] for i in range(m) for j in range(n))

        prefix = 0
        for i in range(m - 1):
            prefix += sum(grid[i])
            if prefix * 2 == total:
                return True

        prefix = 0
        for j in range(n - 1):
            for i in range(m):
                prefix += grid[i][j]
            if prefix * 2 == total:
                return True

        return False

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 2], [3, 4]]
    print(sol.canPartitionGrid(grid))  # Output: True