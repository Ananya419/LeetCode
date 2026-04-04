class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText:
            return ""
        
        cols = len(encodedText) // rows
        stride = cols + 1
        
        return "".join(
            encodedText[c : c + min(rows, cols - c) * stride : stride] 
            for c in range(cols)
        ).rstrip()


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    encodedText = "ch   ie   pr"
    rows = 3
    print(sol.decodeCiphertext(encodedText, rows))  # Output: "cipher"