class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1

        # If array is not rotated
        if nums[left] <= nums[right]:
            return nums[left]

        while left <= right:
            mid = (left + right) // 2

            # Check if mid is the pivot (minimum)
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # Decide which half to search
            if nums[mid] > nums[right]:
                # Minimum is in the right half
                left = mid + 1
            else:
                # Minimum is in the left half
                right = mid - 1

# Example Usage:
sol = Solution()
print(sol.findMin([3, 4, 5, 1, 2]))  # Output: 1
print(sol.findMin([4, 5, 6, 7, 0, 1, 2]))  # Output: 0