class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return sorted(s1[0::2]) == sorted(s2[0::2]) and sorted(s1[1::2]) == sorted(s2[1::2])


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    s1 = "abcd"
    s2 = "cdab"
    print(sol.canBeEqual(s1, s2))  # Output: True   