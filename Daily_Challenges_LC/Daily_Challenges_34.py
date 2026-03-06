class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s
    
# Example Usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.checkOnesSegment("1100"))  # Output: False
    print(solution.checkOnesSegment("1111"))  # Output: True
    print(solution.checkOnesSegment("101"))   # Output: False