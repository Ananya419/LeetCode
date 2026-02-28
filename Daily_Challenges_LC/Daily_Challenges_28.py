class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        result = 0
        for i in range(1, n + 1):
            result = ((result << i.bit_length()) | i) % MOD
        return result


# Example Usage:
if __name__ == "__main__":
    solution = Solution()
    n = 3
    print(solution.concatenatedBinary(n))  # Output: 27