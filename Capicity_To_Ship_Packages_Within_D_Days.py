class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def canShip(capacity: int) -> bool:
            used_days = 1
            current_load = 0
            for w in weights:
                if current_load + w > capacity:
                    used_days += 1
                    current_load = 0
                current_load += w
            return used_days <= days

        low, high = max(weights), sum(weights)
        while low < high:
            mid = (low + high) // 2
            if canShip(mid):
                high = mid
            else:
                low = mid + 1
        return low
    
# Example Usage:
sol = Solution()
print(sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))  # Output: 15
print(sol.shipWithinDays([3,2,2,4,1,4], 3))  # Output: 6

