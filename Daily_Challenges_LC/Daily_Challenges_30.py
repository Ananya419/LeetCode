class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Step 1: Count trailing zeros for each row
        trailing_zeros = []
        for row in grid:
            count = 0
            for j in reversed(range(n)):
                if row[j] == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)
        
        swaps = 0
        
        # Step 2: Greedy placement
        for i in range(n):
            required = n - i - 1
            j = i
            # Find a row with enough trailing zeros
            while j < n and trailing_zeros[j] < required:
                j += 1
            if j == n:  # No valid row found
                return -1
            
            # Step 3: Bring row j up to position i
            while j > i:
                trailing_zeros[j], trailing_zeros[j-1] = trailing_zeros[j-1], trailing_zeros[j]
                swaps += 1
                j -= 1
        
        return swaps
    
# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    grid = [[0,0,1],[1,0,0],[0,1,0]]
    print(sol.minSwaps(grid))  # Output: 3