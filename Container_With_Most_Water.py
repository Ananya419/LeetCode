class Solution:
    # function to calculate maximum area of water container
    def maxArea(self, nums):
        # initialize variables
        max_height = 0                  
        max_a = 0                  
        l = 0                 
        r = len(nums) - 1 

        # while left pointer is less than right pointer
        while l < r:
            # calculate width
            w = r - l
            # calculate height
            height = min(nums[l], nums[r])
            # calculate area
            area = w * height

            # update maximum area if current area is greater
            if area > max_a:
                max_a = area


            # update maximum height if current height is greater
            if height > max_height:
                max_height = height

            # move the pointer pointing to the shorter line
            if nums[l] < nums[r]:
                # move left pointer to the right
                l += 1
            #  else if nums[l] > nums[r]:
            else:
                # move right pointer to the left
                r -= 1

        # return the maximum area found
        return max_a
# Example usage
solution = Solution()
heights = [1,8,6,2,5,4,8,3,7]
print(solution.maxArea(heights))  # Output: 49