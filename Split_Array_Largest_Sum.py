class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        
        def canSplit(maxSum: int) -> bool:
            splits = 1
            currentSum = 0
            for num in nums:
                if currentSum + num > maxSum:
                    splits += 1
                    currentSum = num
                    if splits > k:
                        return False
                else:
                    currentSum += num
            return True
        
        lo = max(nums)      
        hi = sum(nums)      
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if canSplit(mid):
                hi = mid      
            else:
                lo = mid + 1  
        
        return lo
    
# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.splitArray([7, 2, 5, 10, 8], 2))  # Output: 18
    print(sol.splitArray([1, 2, 3, 4, 5], 2))   # Output: 9
    print(sol.splitArray([1, 4, 4], 3))         # Output: 4