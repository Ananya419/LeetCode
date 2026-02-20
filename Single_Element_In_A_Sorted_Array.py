class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            # Ensure mid is even (start of a pair)
            if mid % 2 == 1:
                mid -= 1
            
            if nums[mid] == nums[mid + 1]:
                # Pair is intact → single element is to the RIGHT
                lo = mid + 2
            else:
                # Pair is broken → single element is at mid or to the LEFT
                hi = mid
        
        return nums[lo]
    
# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))  # Output: 2
    print(sol.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))   # Output: 10