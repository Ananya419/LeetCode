"""
LeetCode 3013: Divide an Array Into Subarrays With Minimum Cost II

Problem:
- Divide nums into k disjoint contiguous subarrays
- Cost of subarray = its first element
- Constraint: ik-1 - i1 <= dist (all k-1 chosen indices within dist+1 range)
- Return minimum sum of costs
"""
import heapq
from collections import defaultdict

class Solution:
    def minimumCost(self, nums: list[int], k: int, dist: int) -> int:
        n, need = len(nums), k - 1
        small, large = [], []
        removed = defaultdict(int)
        small_sum = small_size = 0
        
        def prune():
            while small and removed[-small[0]]: removed[-small[0]] -= 1; heapq.heappop(small)
            while large and removed[large[0]]: removed[large[0]] -= 1; heapq.heappop(large)
        
        def balance():
            nonlocal small_sum, small_size
            prune()
            while small_size > need:
                x = -heapq.heappop(small); small_sum -= x; small_size -= 1
                heapq.heappush(large, x); prune()
            while small_size < need and large:
                x = heapq.heappop(large)
                heapq.heappush(small, -x); small_sum += x; small_size += 1; prune()
        
        def add(x):
            nonlocal small_sum, small_size
            if small_size < need or (small and x <= -small[0]):
                heapq.heappush(small, -x); small_sum += x; small_size += 1
            else:
                heapq.heappush(large, x)
            balance()
        
        def remove(x):
            nonlocal small_sum, small_size
            removed[x] += 1
            if small and x <= -small[0]: small_sum -= x; small_size -= 1
            balance()
        
        for i in range(1, min(n, 2 + dist)): add(nums[i])
        ans = nums[0] + small_sum
        for i in range(2 + dist, n):
            add(nums[i]); remove(nums[i - dist - 1])
            ans = min(ans, nums[0] + small_sum)
        return ans


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    nums1 = [1, 3, 2, 6, 4, 2]
    k1 = 3
    dist1 = 3
    result1 = sol.minimumCost(nums1, k1, dist1)
    print(f"Test 1: nums={nums1}, k={k1}, dist={dist1}")
    print(f"Result: {result1}, Expected: 5")
    print()
    
    