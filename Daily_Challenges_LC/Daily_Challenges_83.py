class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return abs(moves.count('L') - moves.count('R')) + moves.count('_')


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    moves = "L_RL__R"
    print(sol.furthestDistanceFromOrigin(moves))  # Output: 3