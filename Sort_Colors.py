class Solution:
    # function to sort colors in-place
    def sortColors(self, nums):
        # initialize pointers for low, mid, and high
        low, mid, high = 0, 0, len(nums) - 1
        # process elements until mid pointer exceeds high pointer
        while mid <= high:
            # check the value at mid pointer
            if nums[mid] == 0:
                # swap values at low and mid pointers
                nums[low], nums[mid] = nums[mid], nums[low]
                # increment both low and mid pointers
                low += 1
                mid += 1
            # check if the value at mid pointer is 1
            elif nums[mid] == 1:
                # increment mid pointer
                mid += 1
            # if the value at mid pointer is 2
            else:     # nums[mid] == 2
                # swap values at mid and high pointers
                nums[mid], nums[high] = nums[high], nums[mid]
                # decrement high pointer
                high -= 1

# Example:
sol = Solution()
colors = [2, 0, 2, 1, 1, 0]
sol.sortColors(colors)
print(colors)  # Output: [0, 0, 1, 1, 2, 2]