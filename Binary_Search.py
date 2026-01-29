class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2  # avoid overflow in other languages

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
    
# Example usage:
if __name__ == "__main__":
    sol = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    print(f"Index of target {target} in array: {sol.search(nums, target)}")