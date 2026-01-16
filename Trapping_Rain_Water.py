class Solution:
    # function to calculate trapped rain water
    def trap(self, height):
        # length of the height array
        n = len(height)
        # set up two pointers and two variables to track max heights
        left, right = 0, n - 1
        # initialize left_max and right_max
        left_max, right_max = 0, 0
        # variable to store total trapped water
        water = 0

        # iterate until the two pointers meet
        while left < right:
            # compare heights at left and right pointers
            if height[left] < height[right]:
                # check if current height is greater than or equal to left_max
                if height[left] >= left_max:
                    # update left_max
                    left_max = height[left]
                # else calculate trapped water at left pointer
                else:
                    # add trapped water to total water from left side
                    water += left_max - height[left]
                # move left pointer to the right
                left += 1
            # else move the right pointer
            else:
                # check if current height is greater than or equal to right_max
                if height[right] >= right_max:
                    # update right_max
                    right_max = height[right]
                # else calculate trapped water at right pointer
                else:
                    # add trapped water to total water from right side
                    water += right_max - height[right]
                # move right pointer to the left
                right -= 1
        # return total trapped water
        return water
    
# Example usage
solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6
