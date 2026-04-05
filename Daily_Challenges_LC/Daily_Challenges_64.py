class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    moves = "UDLR"
    print(sol.judgeCircle(moves))  # Output: True