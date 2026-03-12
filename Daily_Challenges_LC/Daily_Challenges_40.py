from typing import List

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        
        parent = list(range(n))
        rank = [0] * n
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True
        
        def reset_dsu():
            for i in range(n):
                parent[i] = i
                rank[i] = 0
        
        def is_feasible(min_strength: int) -> bool:
            reset_dsu()
            edges_in_tree = 0
            upgrades_used = 0
            
            for u, v, s, must in edges:
                if must == 1:
                    if s < min_strength:
                        return False
                    if not union(u, v):
                        return False
                    edges_in_tree += 1
            
            for u, v, s, must in edges:
                if must == 0 and s >= min_strength:
                    if union(u, v):
                        edges_in_tree += 1
            
            for u, v, s, must in edges:
                if must == 0 and s < min_strength and 2 * s >= min_strength:
                    if union(u, v):
                        edges_in_tree += 1
                        upgrades_used += 1
                        if upgrades_used > k:
                            return False
            
            return edges_in_tree == n - 1
        
        candidates = set()
        for u, v, s, must in edges:
            candidates.add(s)
            if must == 0:
                candidates.add(2 * s)
        candidates = sorted(candidates)
        
        lo, hi = 0, len(candidates) - 1
        result = -1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if is_feasible(candidates[mid]):
                result = candidates[mid]
                lo = mid + 1
            else:
                hi = mid - 1
        
        return result


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    n = 4
    edges = [[0, 1, 3, 1], [1, 2, 2, 0], [2, 3, 4, 0], [0, 3, 1, 0]]
    k = 1
    print(sol.maxStability(n, edges, k))  # Output: 3