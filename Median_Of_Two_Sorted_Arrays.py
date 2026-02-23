class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2
        
        lo, hi = 0, m
        
        while lo <= hi:
            i = (lo + hi) // 2   # elements taken from nums1
            j = half - i          # elements taken from nums2
            
            # Edge values (use -inf/+inf for out-of-bounds)
            nums1_left  = nums1[i - 1] if i > 0 else float('-inf')
            nums1_right = nums1[i]     if i < m else float('inf')
            nums2_left  = nums2[j - 1] if j > 0 else float('-inf')
            nums2_right = nums2[j]     if j < n else float('inf')
            
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # Found the correct partition
                if (m + n) % 2 == 1:
                    return max(nums1_left, nums2_left)
                else:
                    return (max(nums1_left, nums2_left) + 
                            min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                hi = i - 1  # took too many from nums1
            else:
                lo = i + 1  # took too few from nums1

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays([1, 3], [2]))  # Output: 2.0
    print(sol.findMedianSortedArrays([1, 2], [3, 4]))  # Output: 2.5
    print(sol.findMedianSortedArrays([0, 0], [0, 0]))  # Output: 0.0