class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            digitA = int(a[i]) if i >= 0 else 0
            digitB = int(b[j]) if j >= 0 else 0

            total = digitA + digitB + carry
            result.append(str(total % 2))
            carry = total // 2

            i -= 1
            j -= 1

        return ''.join(reversed(result))
    
# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    a1, b1 = "11", "1"
    print(sol.addBinary(a1, b1))  # Output: "100"

    a2, b2 = "1010", "1011"
    print(sol.addBinary(a2, b2))  # Output: "10101"