class Solution:
    def reverseSubmatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        top, bottom = x, x + k - 1

        while top < bottom:
            for col in range(y, y + k):
                grid[top][col], grid[bottom][col] = grid[bottom][col], grid[top][col]
            top += 1
            bottom -= 1

        return grid


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    x, y, k = 0, 0, 2
    print(sol.reverseSubmatrix(grid, x, y, k))  # Output: [[4, 5, 3], [1, 2, 6], [7, 8, 9]]