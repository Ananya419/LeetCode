from collections import Counter

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    s1 = "abc"
    s2 = "bca"
    print(sol.checkStrings(s1, s2))  # Output: False