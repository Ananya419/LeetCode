class Solution:
    def minMirrorPairDistance(self, nums: list[int]) -> int:
        def reverse_int(n: int) -> int:
            return int(str(n)[::-1])

        target_map = {}
        min_dist = float('inf')
        found = False

        for j, val in enumerate(nums):
            if val in target_map:
                min_dist = min(min_dist, j - target_map[val])
                found = True
            
            rev_val = reverse_int(val)
            target_map[rev_val] = j
            
        return int(min_dist) if found else -1


# Example Usage:
if __name__ == "__main__": 
    sol = Solution()
    nums = [123, 321, 456, 654, 789]
    print(sol.minMirrorPairDistance(nums))  # Output: 1