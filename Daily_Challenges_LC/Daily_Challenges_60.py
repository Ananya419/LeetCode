class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
       
        # Bundle robots with their original index
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
        stack = []

        for pos, health, dirr, idx in robots:
            if dirr == "R":
                # Right-moving robots always go on stack
                stack.append([pos, health, dirr, idx])
            else:  # dirr == "L"
                # Resolve collisions with right-moving robots in stack
                while stack and stack[-1][2] == "R" and health > 0:
                    if stack[-1][1] < health:
                        # Right robot dies
                        stack.pop()
                        health -= 1
                    elif stack[-1][1] > health:
                        # Left robot dies
                        stack[-1][1] -= 1
                        health = 0
                    else:
                        # Both die
                        stack.pop()
                        health = 0
                if health > 0:
                    stack.append([pos, health, dirr, idx])

        # Sort survivors back to original index order
        stack.sort(key=lambda x: x[3])
        return [robot[1] for robot in stack]
    
# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    positions = [1, 3, 5]
    healths = [10, 10, 10]
    directions = "RRR"
    print(sol.survivedRobotsHealths(positions, healths, directions))  # Output: [10, 10, 10]