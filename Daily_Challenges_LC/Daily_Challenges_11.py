from typing import List
from collections import defaultdict


class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        sz = 1
        while sz < n:
            sz *= 2

        mn = [0] * (2 * sz)
        mx = [0] * (2 * sz)
        lz = [0] * (2 * sz)

        def push(i):
            if lz[i]:
                for c in (2*i, 2*i+1):
                    mn[c] += lz[i]; mx[c] += lz[i]; lz[c] += lz[i]
                lz[i] = 0

        def update(i, lo, hi, ql, qr, v):
            if ql > hi or qr < lo: return
            if ql <= lo and hi <= qr:
                mn[i] += v; mx[i] += v; lz[i] += v; return
            push(i); mid = (lo+hi)//2
            update(2*i, lo, mid, ql, qr, v)
            update(2*i+1, mid+1, hi, ql, qr, v)
            mn[i] = min(mn[2*i], mn[2*i+1])
            mx[i] = max(mx[2*i], mx[2*i+1])

        def query(i, lo, hi, ql, qr):
            if ql > hi or qr < lo or mn[i] > 0 or mx[i] < 0:
                return -1
            if lo == hi:
                return lo if mn[i] == 0 else -1
            push(i); mid = (lo+hi)//2
            res = query(2*i, lo, mid, ql, qr)
            if res != -1: return res
            return query(2*i+1, mid+1, hi, ql, qr)

        last = {}
        ans = 0
        for r in range(n):
            v = nums[r]
            s = 1 if v % 2 == 0 else -1
            p = last.get(v, -1)
            update(1, 0, sz-1, p+1, r, s)
            last[v] = r
            l = query(1, 0, sz-1, 0, r)
            if l != -1:
                ans = max(ans, r - l + 1)
        return ans
    
# Example Usage:
sol = Solution()
print(sol.longestBalanced([1, 2, 3, 4, 5]))  # Output: 2