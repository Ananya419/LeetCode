from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Sort the array
        nums.sort()
        result = []
        
        # Step 2: Iterate through the array
        for i in range(len(nums)):
            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two pointers
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        
        return result


# ✅ Create object of Solution class
sol = Solution()

# ✅ Call the method with an example input
nums = [-1, 0, 1, 2, -1, -4]
output = sol.threeSum(nums)

print("Triplets that sum to zero:", output)