class Solution:
    # function to return a sorted array of squares of the input sorted array
    def sortedSquares(self, nums):
        # Get the length of the input array
        n = len(nums)
        # Create a result array to store the squares
        result = [0] * n
        # Initialize two pointers at the start and end of the input array
        left, right = 0, n - 1
        # Loop through the result array from the end to the beginning
        for result_index in range(n - 1, -1, -1):
            # Compare the absolute values at the two pointers
            if abs(nums[left]) > abs(nums[right]):
                # Square the value at the left pointer and store it in the result array
                result[result_index] = nums[left] * nums[left]
                # Move the left pointer to the right
                left += 1    
            else:
                # Square the value at the right pointer and store it in the result array
                result[result_index] = nums[right] * nums[right]
                # Move the right pointer to the left
                right -= 1
        # Return the result array
        return result
    

# Example usage:
# it defines a sorted array of integers
nums = [-4, -1, 0, 3, 10]
# it creates an instance of the Solution class
sol = Solution()
# it calls the sortedSquares method to get the sorted squares of the array
print(sol.sortedSquares(nums))