class Solution:
    def findAnagrams(self, s: str, p: str):
        res = []
        len_s, len_p = len(s), len(p)
        if len_p > len_s:
            return res

        # frequency arrays for 26 lowercase letters
        pCount = [0] * 26
        sCount = [0] * 26

        # build initial counts
        for ch in p:
            pCount[ord(ch) - ord('a')] += 1

        for i in range(len_p):
            sCount[ord(s[i]) - ord('a')] += 1

        # check first window
        if sCount == pCount:
            res.append(0)

        # slide the window
        for i in range(len_p, len_s):
            sCount[ord(s[i]) - ord('a')] += 1          # add new char
            sCount[ord(s[i - len_p]) - ord('a')] -= 1  # remove old char

            if sCount == pCount:
                res.append(i - len_p + 1)

        return res


# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.findAnagrams("cbaebabacd", "abc"))  # Output: [0, 6]