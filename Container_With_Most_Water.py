class Solution:
    def maxArea(self, nums):
        max_height = 0                  
        max_a = 0                  
        l = 0                 
        r = len(nums) - 1 

        while l < r:
            w = r - l
            height = min(nums[l], nums[r])
            area = w * height

            if area > max_a:
                max_a = area

            if height > max_height:
                max_height = height

            if nums[l] < nums[r]:
                l += 1
            else:
                r -= 1

        return max_a

obj = Solution()

heights = [1,8,6,2,5,4,8,3,7]
print(obj.maxArea(heights))
