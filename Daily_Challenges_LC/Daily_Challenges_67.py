import math
from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        B = max(1, int(math.sqrt(n)))
        
        small_queries = [[] for _ in range(B)]
        
        for li, ri, ki, vi in queries:
            if ki >= B:
                for idx in range(li, ri + 1, ki):
                    nums[idx] = (nums[idx] * vi) % MOD
            else:
                small_queries[ki].append((li, ri, vi))
                
        for k in range(1, B):
            if not small_queries[k]:
                continue
                
            D_val = [1] * n
            D_zero = [0] * n
            
            for li, ri, vi in small_queries[k]:
                v = vi % MOD
                last = li + ((ri - li) // k) * k
                
                if v == 0:
                    D_zero[li] += 1
                    if last + k < n:
                        D_zero[last + k] -= 1
                else:
                    D_val[li] = (D_val[li] * v) % MOD
                    if last + k < n:
                        inv = pow(v, MOD - 2, MOD)
                        D_val[last + k] = (D_val[last + k] * inv) % MOD
                        
            for i in range(k, n):
                D_val[i] = (D_val[i] * D_val[i - k]) % MOD
                D_zero[i] += D_zero[i - k]
                
            for i in range(n):
                if D_zero[i] > 0:
                    nums[i] = 0
                else:
                    nums[i] = (nums[i] * D_val[i]) % MOD
                    
        ans = 0
        for x in nums:
            ans ^= x
            
        return ans


# Example Usage:

sol = Solution()
print(sol.xorAfterQueries([1, 2, 3, 4], [[0, 2, 1, 2], [1, 3, 2, 3]]))  # Output: 4
