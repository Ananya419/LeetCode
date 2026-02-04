class Solution:
    def maxSumTrionic(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0
        ans = float('-inf')  # Changed from -inf
        
        while i < n:
            l = i
            i += 1
            
            # Phase 1: Find strictly increasing part
            while i < n and nums[i - 1] < nums[i]:
                i += 1
            if i == l + 1:
                continue
            
            p = i - 1  # Peak
            s = nums[p - 1] + nums[p]
            
            # Phase 2: Find strictly decreasing part
            while i < n and nums[i - 1] > nums[i]:
                s += nums[i]
                i += 1
            if i == p + 1 or i == n or nums[i - 1] == nums[i]:
                continue
            
            q = i - 1  # Valley
            s += nums[i]
            i += 1
            
            # Phase 3: Extend right (maximize gain)
            mx = t = 0
            while i < n and nums[i - 1] < nums[i]:
                t += nums[i]
                i += 1
                mx = max(mx, t)
            s += mx
            
            # Optimize left extension
            mx = t = 0
            for j in range(p - 2, l - 1, -1):
                t += nums[j]
                mx = max(mx, t)
            s += mx
            
            ans = max(ans, s)
            i = q
        
        return ans


if __name__ == "__main__":
    sol = Solution()
    
    nums1 = [1, 3, 2, 1, 2, 4]
    print("Test 1:", nums1, "=>", sol.maxSumTrionic(nums1))