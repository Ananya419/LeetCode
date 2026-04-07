class Robot:
    def __init__(self, width: int, height: int):
        self.W = width
        self.H = height
        self.P = 2 * (width - 1) + 2 * (height - 1)
        self.pos = 0
        self.moved = False

    def step(self, num: int) -> None:
        self.pos = (self.pos + num) % self.P
        self.moved = True

    def getPos(self) -> list[int]:
        if self.pos <= self.W - 1:
            return [self.pos, 0]
        elif self.pos <= self.W + self.H - 2:
            return [self.W - 1, self.pos - (self.W - 1)]
        elif self.pos <= 2 * self.W + self.H - 3:
            return [self.W - 1 - (self.pos - (self.W + self.H - 2)), self.H - 1]
        else:
            return [0, self.H - 1 - (self.pos - (2 * self.W + self.H - 3))]

    def getDir(self) -> str:
        if self.pos == 0:
            return "South" if self.moved else "East"
        if self.pos <= self.W - 1:
            return "East"
        elif self.pos <= self.W + self.H - 2:
            return "North"
        elif self.pos <= 2 * self.W + self.H - 3:
            return "West"
        return "South"


# Example Usage:
if __name__ == "__main__":
    robot = Robot(4, 3)
    robot.step(2)
    print(robot.getPos())  # Output: [2, 0]
    print(robot.getDir())  # Output: "East"
    robot.step(2)
    print(robot.getPos())  # Output: [3, 1]
    print(robot.getDir())  # Output: "East"
    robot.step(1)
    print(robot.getPos())  # Output: [3, 2]
    print(robot.getDir())  # Output: "North"