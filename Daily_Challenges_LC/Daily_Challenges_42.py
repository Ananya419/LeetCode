class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * (1 << (n - 1)):
            return ""
        
        chars = ['a', 'b', 'c']
        result = []
        group_size = 1 << (n - 1)
        k -= 1
        
        first_idx = k // group_size
        result.append(chars[first_idx])
        k %= group_size
        
        for i in range(1, n):
            group_size >>= 1
            available = [c for c in chars if c != result[-1]]
            idx = k // group_size
            result.append(available[idx])
            k %= group_size
        
        return "".join(result)


# Example Usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.getHappyString(1, 3))  # Output: "c"
    print(solution.getHappyString(2, 7))  # Output: ""
    print(solution.getHappyString(3, 9))  # Output: "cab"