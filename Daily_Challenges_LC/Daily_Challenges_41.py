import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        
        def max_reduction(t, wt):
            return math.floor((-1 + math.sqrt(1 + 8 * t / wt)) / 2)
        
        def feasible(t):
            total = 0
            for wt in workerTimes:
                total += max_reduction(t, wt)
                if total >= mountainHeight:
                    return True
            return False
        
        lo, hi = 1, mountainHeight * (mountainHeight + 1) // 2 * min(workerTimes)
        
        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.minNumberOfSeconds(10, [1, 2]))  # Output: 21
    print(sol.minNumberOfSeconds(15, [1, 2, 3]))  # Output: 30