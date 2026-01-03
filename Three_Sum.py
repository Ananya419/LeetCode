class Solution(object):
    def threeSum(self, nums):
        #here i have sort the array
        nums.sort()
        # Here i have taken the length of the array
        n = len(nums)
        # here i have taken an empty array to store answers
        answer = []

        # here i have applied for loop for assigning the values of i and the i is the fixed pointer 
        for i in range(n-2):
            #here i have taken two pointer which is l and r 
            l,r = i+1 , n-1

            # here i have applied the while loop for checking the conditions
            
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                # when the value of sum is equal to zero then we will append the answer
                if sum == 0:
                    # here we have used this for reduce the duplicate values
                    if [nums[i], nums[l], nums[r]] in answer:
                        l+=1
                        r-=1
                        continue
                    answer.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                # when the value ofsum is less than zero then we will increment the left pointer 
                elif sum < 0:
                    l += 1
                # when the value ofsum is greater than zero then we will decrement the right pointer
                else:
                    r -= 1
        return answer
        

obj = Solution()
nums = obj.threeSum([-1, 0, 1, 2, -1, -4])
print(nums)