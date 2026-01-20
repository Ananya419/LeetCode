class Solution:
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        left = 0
        total = 0
        min_len = float('inf')

        for right in range(n):
            total += nums[right]

            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len
    
# Example usage:
if __name__ == "__main__":
    sol = Solution()
    target = 7
    nums = [2,3,1,2,4,3]
    print(f"The minimum length of a subarray with sum at least {target} is: {sol.minSubArrayLen(target, nums)}")