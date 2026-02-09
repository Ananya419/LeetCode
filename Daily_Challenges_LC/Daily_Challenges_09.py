from typing import List
from math import inf


class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        ans = -inf
        
        while i < n:
            l = i
            i += 1
            
            # Phase 1: Find strictly increasing part (l to p)
            while i < n and nums[i - 1] < nums[i]:
                i += 1
            
            # Need at least 2 elements for increasing part
            if i == l + 1:
                continue
            
            p = i - 1  # Peak position
            s = nums[p - 1] + nums[p]  # Start with last 2 elements of inc phase
            
            # Phase 2: Find strictly decreasing part (p to q)
            while i < n and nums[i - 1] > nums[i]:
                s += nums[i]
                i += 1
            
            # Need at least 2 elements for decreasing part, and must be able to continue
            if i == p + 1 or i == n or nums[i - 1] == nums[i]:
                continue
            
            q = i - 1  # Valley position
            s += nums[i]  # Add first element of second increasing part
            i += 1
            
            # Phase 3: Find strictly increasing part (q to r)
            # Track maximum sum we can add from extending right
            mx = t = 0
            while i < n and nums[i - 1] < nums[i]:
                t += nums[i]
                i += 1
                mx = max(mx, t)
            s += mx
            
            # Optimize left extension: check if we can extend left for more sum
            mx = t = 0
            for j in range(p - 2, l - 1, -1):
                t += nums[j]
                mx = max(mx, t)
            s += mx
            
            ans = max(ans, s)
            i = q  # Continue from valley for next potential trionic
        
        return ans

# Example Usage:

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: From LeetCode example
    nums1 = [0, -2, -1, -3, 0, 2, -1]
    # Expected: -4 (indices 1,2,3,5: [-2,-1,-3,0,2])
    print(f"Test 1: {nums1}")
    print(f"Result: {sol.maxSumTrionic(nums1)}")
    print(f"Expected: -4")
    print()
    
    