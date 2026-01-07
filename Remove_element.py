class Solution:
    #function to remove all 'val' numbers from the list 'nums'
    def removeElement(self,nums, val):
        #initialize a pointer 'k' to track the position of the next non-'val' element
        k = 0
        #iterate through the list 'nums'
        for i in nums:
            #if the current element is not equal to 'val'
            if i != val:
                #put at at the front of the list
                nums[k] = i
                #increment the pointer 'k'
                k += 1
        #return the count of elements which are not equal to 'val'
        return k

# Example usage:
#the list of numbers
nums = [3, 2, 2, 3, 4, 2]
#the value to be removed
val = 2
# make an object of Solution class
a = Solution()
# call the function
k = a.removeElement(nums, val)
# print how many elements are not equal to 'val'
print("k ", k) 
# print the new list without 'val'         
print("new nums =", nums[:k])  