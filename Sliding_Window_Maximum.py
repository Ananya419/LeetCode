from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()   # will store indices of elements
        result = []
        
        for i in range(len(nums)):
            # 1. Remove indices that are out of the current window
            if dq and dq[0] == i - k:
                dq.popleft()
            
            # 2. Remove elements smaller than current from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # 3. Add current index
            dq.append(i)
            
            # 4. Append max (front of deque) once window is valid
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result


# Example usage:
if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(f"The maximums of each sliding window are: {sol.maxSlidingWindow(nums, k)}")