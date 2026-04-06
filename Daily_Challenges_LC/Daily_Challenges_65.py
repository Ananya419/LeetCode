class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0 
        obstacle_set = set(map(tuple, obstacles))
        x, y = 0, 0
        max_dist_sq = 0
        
        for cmd in commands:
            if cmd == -2:
                direction = (direction - 1) % 4
            elif cmd == -1:
                direction = (direction + 1) % 4
            else:
                dx, dy = moves[direction]
                for _ in range(cmd):
                    if (x + dx, y + dy) in obstacle_set:
                        break 
                    x += dx
                    y += dy
                max_dist_sq = max(max_dist_sq, x*x + y*y)
                
        return max_dist_sq


# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    commands = [4, -1, 3]
    obstacles = [[2, 4]]
    print(sol.robotSim(commands, obstacles))  # Output: 17