from sortedcontainers import SortedList

class Solution:
    def getBiggestThree(self, grid: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        
        dp1 = [[0] * (n + 2) for _ in range(m + 2)]
        dp2 = [[0] * (n + 2) for _ in range(m + 2)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp1[i][j] = dp1[i-1][j-1] + grid[i-1][j-1]
                dp2[i][j] = dp2[i-1][j+1] + grid[i-1][j-1]
        
        top3 = SortedList()
        
        def add(val):
            if val not in top3:
                top3.add(val)
                if len(top3) > 3:
                    top3.pop(0)
        
        def diag1(r1, c1, r2, c2):
            return dp1[r2][c2] - dp1[r1-1][c1-1]
        
        def diag2(r1, c1, r2, c2):
            return dp2[r2][c2] - dp2[r1-1][c1+1]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                add(grid[i-1][j-1])
                
                for s in range(1, min(m, n)):
                    if i - s < 1 or i + s > m or j - s < 1 or j + s > n:
                        break
                    
                    top_left  = diag2(i-s, j, i, j-s)
                    top_right = diag1(i-s, j, i, j+s)
                    bot_left  = diag1(i, j-s, i+s, j)
                    bot_right = diag2(i, j+s, i+s, j)
                    
                    rhombus_sum = (top_left + top_right + bot_left + bot_right
                                   - grid[i-s-1][j-1]
                                   - grid[i+s-1][j-1]
                                   - grid[i-1][j-s-1]
                                   - grid[i-1][j+s-1])
                    
                    add(rhombus_sum)
        
        return list(reversed(top3))


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    print(sol.getBiggestThree(grid))  # Output: [20, 9, 8]