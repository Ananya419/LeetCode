# Simulated API (LeetCode provides this automatically)
def isBadVersion(version: int) -> bool:
    FIRST_BAD = 4   # set the first bad version here
    return version >= FIRST_BAD


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid   # first bad version is at mid or before
            else:
                left = mid + 1  # first bad version is after mid
        return left


if __name__ == "__main__":
    n = 5   # total versions
    print("First bad version is:", Solution().firstBadVersion(n))