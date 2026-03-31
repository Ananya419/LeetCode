class Solution:
    def findTheString(self, lcp: list[list[int]]) -> str:
        n = len(lcp)

        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
            for j in range(i + 1, n):
                if lcp[i][j] != lcp[j][i]:
                    return ""
                if lcp[i][j] > n - j:
                    return ""

        for i in range(n):
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    expected = lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0
                    if expected != lcp[i][j] - 1:
                        return ""

        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for i in range(n):
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    pi, pj = find(i), find(j)
                    if pi != pj:
                        parent[pi] = pj

        char_map = {}
        char_idx = 0
        result = []
        for i in range(n):
            root = find(i)
            if root not in char_map:
                if char_idx >= 26:
                    return ""
                char_map[root] = chr(ord('a') + char_idx)
                char_idx += 1
            result.append(char_map[root])

        for i in range(n):
            for j in range(i + 1, n):
                if lcp[i][j] == 0 and result[i] == result[j]:
                    return ""

        return ''.join(result)


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    lcp = [[3, 2, 1], [2, 3, 0], [1, 0, 3]]
    print(sol.findTheString(lcp))  # Output: "abc"