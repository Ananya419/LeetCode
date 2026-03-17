class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        for row in range(1, m):
            for col in range(n):
                if matrix[row][col] == 1:
                    matrix[row][col] += matrix[row - 1][col]
        
        ans = 0
        for row in range(m):
            sorted_row = sorted(matrix[row], reverse=True)
            for j, height in enumerate(sorted_row):
                if height == 0:
                    break
                ans = max(ans, height * (j + 1))
        
        return ans


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    matrix = [[0,0,1],[1,1,1],[1,0,1]]
    print(sol.largestSubmatrix(matrix))  # Output: 4
    