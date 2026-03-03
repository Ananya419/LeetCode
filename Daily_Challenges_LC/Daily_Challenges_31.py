class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Base case
        if n == 1:
            return "0"
        
        mid = 1 << (n - 1)  # 2^(n-1)
        
        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            # Mirror position in left half
            mirrored = mid - (k - mid)
            bit = self.findKthBit(n - 1, mirrored)
            # Invert
            return "1" if bit == "0" else "0"
        
# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthBit(3, 1))  # Output: "0"
    print(sol.findKthBit(4, 11)) # Output: "1"
    print(sol.findKthBit(1, 1))  # Output: "0"