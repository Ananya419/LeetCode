class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # Base case
        if len(s) <= 2:
            return s
        
        # Find all top-level special substrings
        subs = []
        count = 0  # balance counter: +1 for '1', -1 for '0'
        start = 0
        
        for i, ch in enumerate(s):
            count += 1 if ch == '1' else -1
            if count == 0:
                # s[start:i+1] is a top-level special substring
                # Recursively process the INNER part (s[start+1:i])
                inner = self.makeLargestSpecial(s[start + 1 : i])
                subs.append("1" + inner + "0")
                start = i + 1
        
        # Sort in reverse order → lexicographically largest
        subs.sort(reverse=True)
        
        return "".join(subs)
    
# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.makeLargestSpecial("11011000"))  # Output: "11100100"
    print(sol.makeLargestSpecial("10"))         # Output: "10"
    