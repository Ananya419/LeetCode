class Solution:
    def numSpecial(self, mat):
        m, n = len(mat), len(mat[0])
        
        # Step 1: Compute row sums and column sums
        rowSum = [sum(row) for row in mat]
        colSum = [sum(mat[i][j] for i in range(m)) for j in range(n)]
        
        # Step 2: Count special positions
        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and rowSum[i] == 1 and colSum[j] == 1:
                    count += 1
        return count
    
# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    mat1 = [[1,0,0],[0,0,1],[1,0,0]]
    print(sol.numSpecial(mat1))  # Output: 1

    mat2 = [[1,0,0],[0,1,0],[0,0,1]]
    print(sol.numSpecial(mat2))  # Output: 3

    mat3 = [[0,0,0],[0,0,0],[0,0,0]]
    print(sol.numSpecial(mat3))  # Output: 0