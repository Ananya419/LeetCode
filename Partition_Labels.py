class Solution:
    def partitionLabels(self, s: str):
        last = {ch: i for i, ch in enumerate(s)}
        res = []
        left = right = 0

        for i, ch in enumerate(s):
            right = max(right, last[ch])
            if i == right:
                res.append(right - left + 1)
                left = i + 1
        return res
    
# Example usage
solution = Solution()
print(solution.partitionLabels("ababcbacadefegdehijhklij"))  # Output: [9, 7, 8]