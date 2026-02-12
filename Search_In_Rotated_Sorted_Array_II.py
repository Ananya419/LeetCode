class Solution:
    # Function to search for a target in a rotated sorted array that may contain duplicates
    def search(self, nums, target):
        # 
        left, right = 0, len(nums) - 1
        # Use binary search to find the target
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2
            # Check if the middle element is the target
            if nums[mid] == target:
                # If found, return True
                return True

            # Handle duplicates
            #If the left, middle, and right elements are the same, we cannot determine which half is sorted 
            if nums[left] == nums[mid] == nums[right]:
                # Move the left pointer to the right to skip duplicates
                left += 1
                # Move the right pointer to the left to skip duplicates
                right -= 1
            # If the left half is sorted
            elif nums[left] <= nums[mid]:  # Left half sorted
                # If the target is in the left half
                if nums[left] <= target < nums[mid]:
                    # Move the right pointer to the left to search in the left half
                    right = mid - 1
                # If the target is not in the left half, move the left pointer to the right to search in the right half
                else:
                    # Move the left pointer to the right to search in the right half
                    left = mid + 1
            else: 
                # If the target is in the right half
                if nums[mid] < target <= nums[right]:
                    # Move the left pointer to the right to search in the right half
                    left = mid + 1
                else:
                    # Move the right pointer to the left to search in the left half
                    right = mid - 1
        # If the target is not found after exhausting the search space, return False
        return False
    
# Example Usage:
if __name__ == "__main__": 
    sol = Solution()
    nums1 = [2,5,6,0,0,1,2] 
    target1 = 0 
    print(sol.search(nums1, target1))     # Output: True