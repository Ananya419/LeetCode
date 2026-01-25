class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0

        product = 1
        left = 0
        result = 0

        for right in range(len(nums)):
            product *= nums[right]

            # shrink window until product < k
            while product >= k:
                product //= nums[left]
                left += 1

            # number of valid subarrays ending at right
            result += (right - left + 1)

        return result
    
# Example usage:
if __name__ == "__main__":
    sol = Solution()
    nums = [10, 5, 2, 6]
    k = 100
    print(f"The number of contiguous subarrays where the product is less than {k} is: {sol.numSubarrayProductLessThanK(nums, k)}")