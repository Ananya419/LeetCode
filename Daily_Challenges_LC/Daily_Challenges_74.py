class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_dist = float('inf')

        for i, word in enumerate(words):
            if word == target:
                clockwise = (i - startIndex + n) % n
                counter   = n - clockwise
                min_dist  = min(min_dist, clockwise, counter)

        return min_dist if min_dist != float('inf') else -1


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    words = ["hello", "i", "am", "leetcode", "hello"]
    target = "hello"
    startIndex = 1
    print(sol.closestTarget(words, target, startIndex))  # Output: 1