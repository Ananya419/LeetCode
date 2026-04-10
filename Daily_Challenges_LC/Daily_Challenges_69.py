class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        last1 = {}
        last2 = {}
        min_dist = float('inf')
        
        for i, x in enumerate(nums):
            if x in last1:
                if x in last2:
                    min_dist = min(min_dist, i - last2[x])
                last2[x] = last1[x]
            last1[x] = i
            
        return min_dist * 2 if min_dist != float('inf') else -1


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1, 2, 3]
    print(sol.minimumDistance(nums))  # Output: -1
