class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        total = n * m

        p = [[0] * m for _ in range(n)]

        prefix = 1
        for k in range(total):
            i, j = divmod(k, m)
            p[i][j] = prefix
            prefix = prefix * grid[i][j] % MOD

        suffix = 1
        for k in range(total - 1, -1, -1):
            i, j = divmod(k, m)
            p[i][j] = p[i][j] * suffix % MOD
            suffix = suffix * grid[i][j] % MOD

        return p


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 2], [3, 4]]
    print(sol.constructProductMatrix(grid))  # Output: [[24, 12], [8, 6]]