class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        n = len(colors)
        left, right = 0, n - 1
        
        while colors[0] == colors[right]:
            right -= 1
            
        while colors[n - 1] == colors[left]:
            left += 1
            
        return max(right, n - 1 - left)


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    colors = [1, 1, 1, 6, 1, 1, 1]
    print(sol.maxDistance(colors))  # Output: 3