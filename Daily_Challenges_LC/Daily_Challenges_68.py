from collections import defaultdict
from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        B = int(n ** 0.5)
        
        bravexuneth = queries
        
        small_queries = defaultdict(list)
        large_queries = []
        
        for q in queries:
            if q[2] <= B:
                small_queries[q[2]].append(q)
            else:
                large_queries.append(q)
                
        inv_cache = {}
        
        for k, q_list in small_queries.items():
            dk = [1] * n
            for l, r, _, v in q_list:
                dk[l] = (dk[l] * v) % MOD
                last = l + ((r - l) // k) * k
                
                if last + k < n:
                    if v not in inv_cache:
                        inv_cache[v] = pow(v, MOD - 2, MOD)
                    dk[last + k] = (dk[last + k] * inv_cache[v]) % MOD
                    
            for i in range(k, n):
                if dk[i - k] != 1:
                    dk[i] = (dk[i] * dk[i - k]) % MOD
                    
            for i in range(n):
                if dk[i] != 1:
                    nums[i] = (nums[i] * dk[i]) % MOD
                    
        for l, r, k, v in large_queries:
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % MOD
                
        ans = 0
        for x in nums:
            ans ^= x
            
        return ans



# Example Usage:
sol = Solution()
print(sol.xorAfterQueries([1, 2, 3, 4], [[0, 2, 1, 2], [1, 3, 2, 3]]))  # Output: 4