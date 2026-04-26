from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        R, C = len(grid), len(grid[0])
        parent = list(range(R * C))
        rank = [0] * (R * C)

        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        for r in range(R):
            row_offset = r * C
            for c in range(C):
                val = grid[r][c]
                curr = row_offset + c
                
                if c + 1 < C and grid[r][c + 1] == val:
                    root1, root2 = find(curr), find(curr + 1)
                    if root1 == root2: return True
                    if rank[root1] < rank[root2]: parent[root1] = root2
                    elif rank[root1] > rank[root2]: parent[root2] = root1
                    else:
                        parent[root1] = root2
                        rank[root2] += 1
                
                if r + 1 < R and grid[r + 1][c] == val:
                    root1, root2 = find(curr), find(curr + C)
                    if root1 == root2: return True
                    if rank[root1] < rank[root2]: parent[root1] = root2
                    elif rank[root1] > rank[root2]: parent[root2] = root1
                    else:
                        parent[root1] = root2
                        rank[root2] += 1
                        
        return False


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
    print(sol.containsCycle(grid))  # Output: False