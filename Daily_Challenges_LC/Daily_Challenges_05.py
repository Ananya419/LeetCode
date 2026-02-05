class Solution:
    def constructTransformedArray(self, nums):
        n = len(nums)
        # Copy original values to avoid overwriting before use
        original = nums[:]
        
        for i in range(n):
            if original[i] == 0:
                nums[i] = 0
            else:
                new_index = (i + original[i]) % n
                nums[i] = original[new_index]
        
        return nums
    
    # Example Used:

if __name__ == "__main__":
    sol = Solution()
    nums = [2, 0, 1, 3]
    print("Original:", nums)
    transformed = sol.constructTransformedArray(nums[:])  # use copy to preserve original
    print("Transformed:", transformed)

