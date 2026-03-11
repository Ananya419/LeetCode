class Solution:
    def bitwiseComplement(self, n: int) -> int:
        mask = (1 << max(n.bit_length(), 1)) - 1
        return n ^ mask


# Example Usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.bitwiseComplement(5))  # Output: 2
    print(solution.bitwiseComplement(7))  # Output: 0
    print(solution.bitwiseComplement(10)) # Output: 5