class Solution:
    def minPartitions(self, n: str) -> int:
        # The answer is simply the maximum digit in the string
        return int(max(n))
    
# Example Usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.minPartitions("27346209830709182346"))  # Output: 9

    