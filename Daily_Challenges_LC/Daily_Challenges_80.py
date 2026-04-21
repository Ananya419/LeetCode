from collections import Counter, defaultdict

class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)
        parent = list(range(n))
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
        
        for a, b in allowedSwaps:
            union(a, b)
            
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)
            
        hamming_distance = 0
        for root in groups:
            indices = groups[root]
            source_elements = [source[i] for i in indices]
            target_elements = [target[i] for i in indices]
            
            source_counts = Counter(source_elements)
            target_counts = Counter(target_elements)
            
            matches = 0
            for val in source_counts:
                if val in target_counts:
                    matches += min(source_counts[val], target_counts[val])
            
            hamming_distance += (len(indices) - matches)
            
        return hamming_distance


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    source = [1, 2, 3, 4]
    target = [2, 1, 4, 5]
    allowedSwaps = [[0, 1], [2, 3]]
    print(sol.minimumHammingDistance(source, target, allowedSwaps))  # Output: 1