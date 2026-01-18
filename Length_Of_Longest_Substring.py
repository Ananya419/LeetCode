class Solution:
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
    
    # Example usage:
if __name__ == "__main__":
    sol = Solution()
    test_string = "abcabcbb"
    print(f"The length of the longest substring without repeating characters in '{test_string}' is: {sol.lengthOfLongestSubstring(test_string)}")