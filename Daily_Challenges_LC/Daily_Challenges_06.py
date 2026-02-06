class Solution:
    def minRemoval(self, nums, k):
        nums.sort()
        n = len(nums)
        left = 0
        max_len = 1  # at least one element is always balanced

        for right in range(n):
            while nums[right] > k * nums[left]:
                left += 1
            max_len = max(max_len, right - left + 1)

        return n - max_len
    
# Example Usage:
sol = Solution()
print(sol.minRemoval([1, 3, 6, 8, 10], 2))  # Output: 2