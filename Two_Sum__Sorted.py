class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1 ]
            elif current_sum < target:
                left += 1
            else:
                right -= 1 


obj = Solution()   # create an object of Solution

numbers = [2, 7, 11, 15]
target = 13

obj = Solution()   
result = obj.twoSum(numbers, target)   
print(result)     