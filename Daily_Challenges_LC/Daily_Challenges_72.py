class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        n = len(nums)
        for i in range(n):
            if start + i < n and nums[start + i] == target:
                return i
            if start - i >= 0 and nums[start - i] == target:
                return i
        return -1


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5]
    target = 3
    start = 0
    print(sol.getMinDistance(nums, target, start))  # Output: 2
