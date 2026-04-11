class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        history = {}
        min_dist = float('inf')
        
        for i, num in enumerate(nums):
            if num in history:
                prev2, prev1 = history[num]
                if prev2 is not None and i - prev2 < min_dist:
                    min_dist = i - prev2
                history[num] = (prev1, i)
            else:
                history[num] = (None, i)
                
        return min_dist * 2 if min_dist != float('inf') else -1



# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1, 2, 3]
    print(sol.minimumDistance(nums))  # Output: -1