from collections import defaultdict
from bisect import bisect_left
from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        index_map = defaultdict(list)
        for i, v in enumerate(nums):
            index_map[v].append(i)
        
        answer = []
        for q in queries:
            indices = index_map[nums[q]]
            if len(indices) == 1:
                answer.append(-1)
                continue
            
            pos = bisect_left(indices, q)
            min_dist = float('inf')
            
            for neighbor in [(pos - 1) % len(indices), (pos + 1) % len(indices)]:
                d = abs(q - indices[neighbor])
                min_dist = min(min_dist, min(d, n - d))
            
            answer.append(min_dist)
        
        return answer


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 2, 1]
    queries = [0, 1, 2, 3, 4]
    print(sol.solveQueries(nums, queries))  # Output: [1, 2, -1, 2, 1]