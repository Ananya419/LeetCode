class Solution:
    # function to check if a given string is a palindrome
    def isPalindrome(self, s):
        # length of the string
        n = len(s)
        # initialize left and right pointers
        l, r = 0, n - 1
        
        # while left pointer is less than right pointer
        while l < r:
            # check if left pointer is alphanumeric
            if not s[l].isalnum():
                # move left pointer to the right
                l += 1
                continue

            # check if right pointer is alphanumeric
            if not s[r].isalnum():
                # move right pointer to the left
                r -= 1
                continue

            # compare characters at left and right pointers (case insensitive)
            if s[l].lower() != s[r].lower():
                # if characters don't match, it's not a palindrome(return False)
                return False
            
            # move both pointers towards the center
            l += 1
            r -= 1

        # if all characters matched, it's a palindrome(return True)
        return True
    
# Example:
sol = Solution()

print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # True
print(sol.isPalindrome("race a car"))                      # False