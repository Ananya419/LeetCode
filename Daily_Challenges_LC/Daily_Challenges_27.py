from collections import deque
class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z = s.count('0')

        if z == 0:
            return 0

       
        parent = [list(range(n + 4)), list(range(n + 4))]

        def find(p, i):
            if i > n:          
                return i
            while parent[p][i] != i:
                parent[p][i] = parent[p][parent[p][i]]
                i = parent[p][i]
            return i

        def skip(p, i):
            parent[p][i] = find(p, i + 2)

        queue = deque([(z, 0)])
        skip(z % 2, z)

        while queue:
            z, ops = queue.popleft()

            lo = max(0, k - (n - z))
            hi = min(k, z)

            if lo > hi:
                continue

            min_z = z + k - 2 * hi
            max_z = z + k - 2 * lo
            p = (z + k) % 2

            cur = find(p, max(0, min_z))
            while cur <= min(n, max_z):
                if cur == 0:
                    return ops + 1
                queue.append((cur, ops + 1))
                skip(p, cur)
                cur = find(p, cur)

        return -1


# Example Usage:
if __name__ == "__main__":
    solution = Solution()
    s = "1100"
    k = 2
    result = solution.minOperations(s, k)
    print(f"Minimum operations required: {result}")

