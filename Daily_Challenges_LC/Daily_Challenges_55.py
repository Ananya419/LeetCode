class Solution:
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        n = len(mat[0])
        k %= n
        if k == 0:
            return True
        for row in mat:
            for j in range(n):
                if row[j] != row[(j + k) % n]:
                    return False
        return True


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    mat = [[1, 2, 3], [4, 5, 6]]
    k = 1
    print(sol.areSimilar(mat, k))  # Output: False
    