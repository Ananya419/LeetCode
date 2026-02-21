class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Precompute prime set bits up to 32 (enough for int range)
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        
        count = 0
        for num in range(left, right + 1):
            # Count set bits using built-in method
            if num.bit_count() in primes:
                count += 1
        return count
    
# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.countPrimeSetBits(6, 10))  # Output: 4
    print(sol.countPrimeSetBits(10, 15))  # Output: 5