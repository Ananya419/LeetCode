class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        # Build frequency arrays
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        if count1 == count2:
            return True

        # Sliding window
        for i in range(len(s1), len(s2)):
            count2[ord(s2[i]) - ord('a')] += 1              # add new char
            count2[ord(s2[i - len(s1)]) - ord('a')] -= 1    # remove old char

            if count1 == count2:
                return True

        return False


# Example usage:
if __name__ == "__main__":
    sol = Solution()
    s1 = "ab"
    s2 = "eidbaooo"
    print(f"Does s2 contain a permutation of s1? {sol.checkInclusion(s1, s2)}")