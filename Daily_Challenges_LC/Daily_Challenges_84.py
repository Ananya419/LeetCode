from bisect import bisect_left

class Solution:
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        # Special case for k=2 as Manhattan distance can exceed perimeter distance logic
        if k == 2:
            mx1, mn1 = -float('inf'), float('inf')
            mx2, mn2 = -float('inf'), float('inf')
            for x, y in points:
                mx1, mn1 = max(mx1, x + y), min(mn1, x + y)
                mx2, mn2 = max(mx2, x - y), min(mn2, x - y)
            return int(max(mx1 - mn1, mx2 - mn2))

        res = []
        for x, y in points:
            if x == 0:
                res.append(y)
            elif y == side:
                res.append(side + x)
            elif x == side:
                res.append(side * 3 - y)
            else:
                res.append(side * 4 - x)
        res.sort()
        
        n_points = len(res)

        def check(n: int) -> bool:
            # Initial greedy selection starting from the first point
            idx = [0] * k
            curr = res[0]
            for i in range(1, k):
                j = bisect_left(res, curr + n)
                if j == n_points:
                    return False
                idx[i] = j
                curr = res[j]
            
            # Check circular distance for the first starting point
            if res[idx[-1]] - res[idx[0]] <= side * 4 - n:
                return True
            
            # Use two pointers to check all other possible starting points
            # This is efficient because each index in idx only moves forward
            for start_idx in range(1, idx[1]):
                idx[0] = start_idx
                for j in range(1, k):
                    while idx[j] < n_points and res[idx[j]] < res[idx[j - 1]] + n:
                        idx[j] += 1
                    if idx[j] == n_points:
                        return False
                if res[idx[-1]] - res[idx[0]] <= side * 4 - n:
                    return True
            return False
        
        # Binary search for the maximum possible minimum distance
        # Range is 1 to 2*side (max Manhattan distance in a square)
        left, right = 1, 2 * side + 1
        ans = 1
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid
        return ans

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    side = 5
    points = [[0, 1], [5, 5], [3, 0], [0, 4]]
    k = 3
    print(sol.maxDistance(side, points, k))  # Output: 4
