class Solution:
    def minimumCost(self, nums):
        n = len(nums)
        
        # Running suffix minimum
        suffix_min = nums[-1]
        ans = float('inf')
        
        # Traverse backwards for possible second subarray starts
        for i in range(n-2, 0, -1):  # i from n-2 down to 1
            suffix_min = min(suffix_min, nums[i+1])
            ans = min(ans, nums[0] + nums[i] + suffix_min)
        
        return ans
    
    # Example usage:


if __name__ == "__main__":
    sol = Solution()
    
    nums1 = [3, 4, 1, 2, 5]
    print(sol.minimumCost(nums1))  # Expected output: 6
