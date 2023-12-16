import unittest
import pathlib
import numpy
import copy


class Cell:
    def __init__(self, type):
        self.type = type
        self.beams = [False, False, False, False]


class Day16:
    def part1(self, input):
        t = input.rstrip().split("\n")

        self.grid = {}
        self.maxY = len(t)
        self.maxX = len(t[0])
        for j in range(0, self.maxY):
            for i in range(0, self.maxX):
                self.grid[(i, j)] = Cell(t[j][i])

        self.grid[(0, 0)].beams[3] = True
        self.queue = [(0, 0)]
        self.populate()

        return self.energized()

    def part2(self, input):
        t = input.rstrip().split("\n")

        grid = {}
        self.maxY = len(t)
        self.maxX = len(t[0])
        for j in range(0, self.maxY):
            for i in range(0, self.maxX):
                grid[(i, j)] = Cell(t[j][i])

        m = 0
        # from top
        for i in range(0, self.maxX):
            self.grid = copy.deepcopy(grid)
            self.grid[(i, 0)].beams[0] = True
            self.queue = [(i, 0)]
            self.populate()
            m = max(m, self.energized())

        # from bottom
        for i in range(0, self.maxX):
            self.grid = copy.deepcopy(grid)
            self.grid[(i, self.maxY-1)].beams[2] = True
            self.queue = [(i, self.maxY-1)]
            self.populate()
            m = max(m, self.energized())

        # from left
        for j in range(0, self.maxY):
            self.grid = copy.deepcopy(grid)
            self.grid[(0, j)].beams[3] = True
            self.queue = [(0, j)]
            self.populate()
            m = max(m, self.energized())

        # from right
        for j in range(0, self.maxY):
            self.grid = copy.deepcopy(grid)
            self.grid[(self.maxX-1, j)].beams[1] = True
            self.queue = [(self.maxX-1, j)]
            self.populate()
            m = max(m, self.energized())

        return m

    def populate(self):
        while len(self.queue) > 0:
            pos = self.queue.pop(0)
            c = self.grid[pos]
            if c.beams[0]:
                # beam arriving from top
                if c.type == "." or c.type == "|":
                    self.propagate(pos[0], pos[1]+1, 0)
                if c.type == "\\" or c.type == "-":
                    self.propagate(pos[0]+1, pos[1], 3)
                if c.type == "/" or c.type == "-":
                    self.propagate(pos[0]-1, pos[1], 1)
            if c.beams[1]:
                # beam arriving from right
                if c.type == "." or c.type == "-":
                    self.propagate(pos[0]-1, pos[1], 1)
                if c.type == "\\" or c.type == "|":
                    self.propagate(pos[0], pos[1]-1, 2)
                if c.type == "/" or c.type == "|":
                    self.propagate(pos[0], pos[1]+1, 0)
            if c.beams[2]:
                # beam arriving from bottom
                if c.type == "." or c.type == "|":
                    self.propagate(pos[0], pos[1]-1, 2)
                if c.type == "\\" or c.type == "-":
                    self.propagate(pos[0]-1, pos[1], 1)
                if c.type == "/" or c.type == "-":
                    self.propagate(pos[0]+1, pos[1], 3)
            if c.beams[3]:
                # beam arriving from left
                if c.type == "." or c.type == "-":
                    self.propagate(pos[0]+1, pos[1], 3)
                if c.type == "\\" or c.type == "|":
                    self.propagate(pos[0], pos[1]+1, 0)
                if c.type == "/" or c.type == "|":
                    self.propagate(pos[0], pos[1]-1, 2)

    def propagate(self, i, j, dir):
        pos = (i, j)
        if pos not in self.grid:
            return
        if self.grid[pos].beams[dir]:
            return
        self.grid[pos].beams[dir] = True
        self.queue.append(pos)

    def energized(self):
        sum = 0
        for j in range(0, self.maxY):
            for i in range(0, self.maxX):
                c = self.grid[(i, j)]
                if True in c.beams:
                    sum += 1
        return sum


class TestDayXX(unittest.TestCase):
    def testPart1(self):
        self.assertEqual(Day16().part1(""".|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|...."""), 46)

    def testPart2(self):
        self.assertEqual(Day16().part2(""".|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|...."""), 51)


print("day 16, part 1: ", Day16().part1(pathlib.Path("input").read_text()))
print("day 16, part 2: ", Day16().part2(pathlib.Path("input").read_text()))
unittest.main()
