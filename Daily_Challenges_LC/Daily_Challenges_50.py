class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        n = len(mat)
        
        def rotate90(m):
            return [[m[n - 1 - j][i] for j in range(n)] for i in range(n)]
        
        for _ in range(4):
            if mat == target:
                return True
            mat = rotate90(mat)
        
        return False


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    mat = [[0,1],[1,0]]
    target = [[1,0],[0,1]]
    print(sol.findRotation(mat, target))  # Output: True
    