from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        res = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                res = max(res, j - i)
                j += 1
            else:
                i += 1
        return res


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 2, 3]
    nums2 = [3, 4, 5]
    print(sol.maxDistance(nums1, nums2))  # Output: 2