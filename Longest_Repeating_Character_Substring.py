from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        max_count = 0
        result = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count, count[s[right]])

            # If more than k replacements needed, shrink window
            if (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
    
# Example usage:
if __name__ == "__main__":
    sol = Solution()
    test_string = "AABABBA"
    k = 1
    print(f"The length of the longest substring after {k} replacements in '{test_string}' is: {sol.characterReplacement(test_string, k)}")