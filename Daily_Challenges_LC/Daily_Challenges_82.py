from collections import defaultdict
class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        groups = defaultdict(list)
        for i, val in enumerate(nums):
            groups[val].append(i)
        
        n = len(nums)
        ans = [0] * n
        
        for indices in groups.values():
            k = len(indices)
            total_sum = sum(indices)
            left_sum = 0
            for p, idx in enumerate(indices):
                right_sum = total_sum - left_sum - idx
                ans[idx] = (p * idx - left_sum) + (right_sum - (k - 1 - p) * idx)
                left_sum += idx
        
        return ans
    
# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 1, 3]
    print(sol.distance(nums))  # Output: [2, 0, 2, 0]