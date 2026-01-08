class Solution:
    def moveZeroes(self, nums):
        # pointer for the position of the next non-zero element
        j = 0
        # for loop to iterate through the list
        for i in range(len(nums)):
            # check whether the current element is equal to zero or not
            if nums[i] != 0:
                # Move the non-zero element to the j-th position
                nums[j] = nums[i]
                # Increment the position for the next non-zero element
                j += 1

        # it checks whether j is less than the length of the nums list
        while j < len(nums):
            # fill the remaining positions with zeros
            nums[j] = 0
            # Increment the position for the next zero element
            j += 1


# Example usage:
# it defines a list of numbers
nums = [0, 1, 0, 3, 12]
# it calls the moveZeroes method to move zeros to the end
Solution().moveZeroes(nums)
# print the new list
print(nums)
