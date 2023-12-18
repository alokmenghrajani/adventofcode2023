import unittest
import pathlib
import astar

# Day 17:
# using astar because I couldn't find a dijkstar library with an API I liked.


class Day17(astar.AStar):
    def part1(self, input):
        lines = input.rstrip().split("\n")
        self.grid = list(map(lambda line: list(map(int, line)), lines))
        self.maxX = len(self.grid[0])
        self.maxY = len(self.grid)
        self.part = "part1"

        solution = list(self.astar((0, 0, None, 0), None))
        solution.pop(0)  # ignore first cell

        r = 0
        for x, y, dir, count in solution:
            r += self.grid[y][x]
        return r

    def part2(self, input):
        lines = input.rstrip().split("\n")
        self.grid = list(map(lambda line: list(map(int, line)), lines))
        self.maxX = len(self.grid[0])
        self.maxY = len(self.grid)
        self.part = "part2"

        solution = list(self.astar((0, 0, None, 0), None))
        solution.pop(0)  # ignore first cell

        r = 0
        for x, y, dir, count in solution:
            r += self.grid[y][x]
        return r

    def neighbors(self, node):
        x, y, dir, count = node
        r = []
        if dir == None:
            # first cell
            return [(1, 0, 1, 1), (0, 1, 2, 1)]
        if dir == 0:
            # up
            r.append((x, y-1, 0, count+1))  # straight
            if self.part == "part1" or count >= 4:
                r.append((x-1, y, 3, 1))  # turn left
                r.append((x+1, y, 1, 1))  # turn right
        elif dir == 1:
            # right
            r.append((x+1, y, 1, count+1))  # straight
            if self.part == "part1" or count >= 4:
                r.append((x, y-1, 0, 1))  # turn left
                r.append((x, y+1, 2, 1))  # turn right
        elif dir == 2:
            # down
            r.append((x, y+1, 2, count+1))  # straight
            if self.part == "part1" or count >= 4:
                r.append((x+1, y, 1, 1))  # turn left
                r.append((x-1, y, 3, 1))  # turn right
        elif dir == 3:
            # left
            r.append((x-1, y, 3, count+1))  # straight
            if self.part == "part1" or count >= 4:
                r.append((x, y+1, 2, 1))  # turn left
                r.append((x, y-1, 0, 1))  # turn right
        return r

    def distance_between(self, n1, n2):
        x2, y2, _, count2 = n2
        if x2 < 0 or x2 >= self.maxX:
            return float("inf")
        if y2 < 0 or y2 >= self.maxY:
            return float("inf")
        if self.part == "part1" and count2 > 3:
            return float("inf")
        if self.part == "part2" and count2 > 10:
            return float("inf")
        return self.grid[y2][x2]

    def heuristic_cost_estimate(self, current, goal):
        x, y, _, _ = current
        dx = abs(self.maxX - x)
        dy = abs(self.maxY - y)
        return dx + dy

    def is_goal_reached(self, current, goal):
        x, y, _, count = current
        if self.part == "part1":
            return (x == self.maxX - 1) and (y == self.maxY - 1)
        return (x == self.maxX - 1) and (y == self.maxY - 1) and (count >= 4)


class TestDay17(unittest.TestCase):
    def testPart1(self):
        self.assertEqual(Day17().part1("""2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""), 102)

    def testPart2(self):
        self.assertEqual(Day17().part2("""2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""), 94)
        self.assertEqual(Day17().part2("""111111111111
999999999991
999999999991
999999999991
999999999991"""), 71)


print("day 17, part 1: ", Day17().part1(pathlib.Path("input").read_text()))
print("day 17, part 2: ", Day17().part2(pathlib.Path("input").read_text()))
unittest.main()
