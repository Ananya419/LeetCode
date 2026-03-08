class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        n = len(nums)
        res = []
        for i in range(n):
            # Flip the i-th bit of the i-th string
            res.append('1' if nums[i][i] == '0' else '0')
        return "".join(res)
    

# Example Usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.findDifferentBinaryString(["01", "10"]))  # Output: "11"
    print(solution.findDifferentBinaryString(["00", "01"]))  # Output: "10"
    print(solution.findDifferentBinaryString(["111", "011", "001"]))  # Output: "000"