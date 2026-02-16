import math
class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            hours = sum(math.ceil(p / mid) for p in piles)
            
            if hours <= h:
                right = mid  # try smaller speed
            else:
                left = mid + 1  # need faster speed
        
        return left
    
# Example Usage:
sol = Solution()
print(sol.minEatingSpeed([3, 6, 7, 11], 8))  # Output: 4
print(sol.minEatingSpeed([30, 11, 23, 4, 20], 5))  # Output: 30