class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k  # 2^k
        if len(s) < k + need - 1:
            return False
        
        seen = set()
        mask = need - 1  # bitmask of k bits (e.g., k=3 → 0b111)
        num = 0
        
        for i in range(len(s)):
            num = ((num << 1) | int(s[i])) & mask
            if i >= k - 1:  # we have a full window of size k
                seen.add(num)
                if len(seen) == need:
                    return True
        
        return False
    
# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.hasAllCodes("00110110", 2))  # True
    print(sol.hasAllCodes("0110", 1))      # True
    print(sol.hasAllCodes("0110", 2))      # False