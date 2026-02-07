class Solution:
    def minimumDeletions(self, s: str) -> int:
        count_b = 0  # Count of 'b's seen so far
        deletions = 0  # Minimum deletions needed
        
        for char in s:
            if char == 'b':
                count_b += 1
            else:  # char == 'a'
                # We can either delete this 'a' or delete all 'b's before it
                # Choose the minimum cost
                deletions = min(deletions + 1, count_b)
        
        return deletions
    

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    s1 = "aababbab"
    print(sol.minimumDeletions(s1))  # Output: 2