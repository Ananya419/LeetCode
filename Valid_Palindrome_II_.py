class Solution:
    # function to check whether a string can be a palindrome by removing at most one character
    def validPalindrome(self, s: str) -> bool:
        # helper function to check if a substring is a palindrome
        def is_palindrome(l, r):
            # while loop to check characters from both ends
            while l < r:
                # if characters don't match
                if s[l] != s[r]:
                    # return false
                    return False
                # move towards the center
                l += 1
                r -= 1
            # if we reached here, it means the substring is a palindrome thus return true
            return True
        
        # initialize two pointers
        left, right = 0, len(s) - 1
        # while loop to check characters from both ends
        while left < right:
            # if characters don't match
            if s[left] != s[right]:
                # check by removing one character either from left or right
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            # move towards the center
            left += 1
            right -= 1
        # if we reached here, it means the string is already a palindrome thus return true
        return True
    
# Example usage
solution = Solution()
print(solution.validPalindrome("abca"))  # Output: True