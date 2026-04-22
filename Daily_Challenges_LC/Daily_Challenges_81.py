class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        res = []
        for q in queries:
            for d in dictionary:
                diff = 0
                for char_q, char_d in zip(q, d):
                    if char_q != char_d:
                        diff += 1
                        if diff > 2:
                            break
                else:
                    res.append(q)
                    break
        return res


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    queries = ["word1", "word2", "word3"]
    dictionary = ["word1", "word4", "word5"]
    print(sol.twoEditWords(queries, dictionary))  # Output: ['word1', 'word2', 'word3']