class Solution:
    def isTrionic(self, nums):
        n = len(nums)
        if n < 3:
            return False

        i = 0

        # Phase 1: strictly increasing
        while i+1 < n and nums[i+1] > nums[i]:
            i += 1
        # must have at least one increasing step
        if i == 0:
            return False

        # Phase 2: strictly decreasing
        while i+1 < n and nums[i+1] < nums[i]:
            i += 1
        # must have at least one decreasing step
        if i == 1 or i == n-1:
            return False

        # Phase 3: strictly increasing again
        while i+1 < n and nums[i+1] > nums[i]:
            i += 1

        # if we reached the end, it's trionic
        return i == n-1
    
# example usage:

sol = Solution()

print(sol.isTrionic([1, 3, 2, 4, 5]))   # True → inc [1,3], dec [3,2], inc [2,4,5]
print(sol.isTrionic([1, 2, 3, 4]))      # False → no decreasing part
