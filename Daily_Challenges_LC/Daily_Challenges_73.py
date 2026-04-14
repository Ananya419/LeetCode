class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        robot.sort()
        factory.sort(key=lambda x: x[0])
        m = len(robot)
        dp = [0] + [10**20] * m
        for p, l in factory:
            for i in range(m, 0, -1):
                cur = 0
                for k in range(1, min(l, i) + 1):
                    cur += abs(robot[i - k] - p)
                    if dp[i - k] + cur < dp[i]:
                        dp[i] = dp[i - k] + cur
        return dp[m]



# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    robot = [0, 4, 6]
    factory = [[2, 2], [6, 2]]
    print(sol.minimumTotalDistance(robot, factory))  # Output: 4
    