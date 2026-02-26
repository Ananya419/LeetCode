class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        
        # Traverse from right to left (excluding the first bit)
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i]) + carry
            if bit % 2 == 0:  # even
                steps += 1
            else:  # odd
                steps += 2
                carry = 1  # propagate carry
        
        # Finally, add carry if needed
        return steps + carry
    
# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    s1 = "1101"
    print(sol.numSteps(s1))  # Output: 6
    s2 = "10"
    print(sol.numSteps(s2))  # Output: 1
    s3 = "1"
    print(sol.numSteps(s3))  # Output: 0