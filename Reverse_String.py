# LeetCode Problem 344: Reverse String
class Solution:
    # Function to reverse a list of characters in place
    def reverseString(self, s: list[str]) -> None:
        # Initialize two pointers at the start and end of the list
        l,r = 0, (len(s))-1
        # Loop until the two pointers meet in the middle
        while l < r:
            # Swap the characters at the two pointers
            s[l] , s[r] =  s[r] , s[l]
            # Move the left pointer to the right
            l = l+1
            # Move the right pointer to the left
            r = r-1
# Example usage:
# it defines a list of characters
s = ["h","e","l","l","o"]
# it creates an instance of the Solution class
sol = Solution()
# it calls the reverseString method to reverse the list
sol.reverseString(s)
# print the reversed list
print(s)  # Output: ["o","l","l","e","h"]