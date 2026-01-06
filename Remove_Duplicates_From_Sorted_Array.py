# Define a class named Solution (required by LeetCode driver)
class Solution: 
# Define the method removeDuplicates that takes a list 'nums'
    def removeDuplicates(self, nums): 
         # Check if the list is empty     
        if len(nums) == 0:
            # If empty, return 0 (no unique elements)                  
            return 0   
        # Initialize pointer 'i' to track the last unique element's index                     
        i = 0 
        # Iterate through the list starting from index 1                              
        for j in range(1, len(nums)): 
            # If current element is different from the last unique element      
            if nums[j] != nums[i]:
                # Move pointer 'i' forward          
                i += 1   
                # Place the new unique element at position 'i'                   
                nums[i] = nums[j] 
                # Return the count of unique elements (index + 1)          
        return i + 1 
                           
nums = [0,0,1,1,1,2,2,3,3,4]              
# Input sorted list with duplicates
k = Solution().removeDuplicates(nums)              
 # Call the function and store the number of unique elements
print("Number of unique elements:", k)   
 # Print the count of unique elements
print("Array after removing duplicates:", nums[:k])  
# Print the array up to 'k' (unique elements only)