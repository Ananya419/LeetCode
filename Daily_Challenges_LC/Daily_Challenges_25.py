
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    arr1 = [0,1,2,3,4,5,6,7,8]
    print(sol.sortByBits(arr1))  # Output: [0,1,2,4,8,3,5,6,7]