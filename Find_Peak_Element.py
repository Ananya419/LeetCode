class Solution:
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left  # or right, since left == right
    
# # Example Usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.findPeakElement([1, 2, 3, 1]))  # Output: 2
    print(sol.findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # Output: 5