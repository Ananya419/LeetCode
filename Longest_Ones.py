class Solution:
    def longestOnes(self, nums, k):
        left = 0
        zeros = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            # Shrink window if zeros exceed k
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # Update max length
            max_len = max(max_len, right - left + 1)

        return max_len
    
# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestOnes([1, 1, 0, 0, 1, 1, 1, 0, 1], 2))  # Output: 7