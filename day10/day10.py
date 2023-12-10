import unittest
import pathlib
from itertools import product
import drawsvg as draw

# Day 10:
# part 1: I keep "flooding" the grid until there's no change.
# part 2: We need to calculate if we encounter an even or odd number of
#         intersections to a random point on the outside:
#         https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule

class Day10:
    pipes = {
        "|": {(0, -1), (0, 1)},
        "-": {(-1, 0), (1, 0)},
        "L": {(0, -1), (1, 0)},
        "J": {(0, -1), (-1, 0)},
        "7": {(0, 1), (-1, 0)},
        "F": {(0, 1), (1, 0)},
        ".": {},
        "S": {(0, -1), (1, 0), (0, 1), (-1, 0)},
    }

    vectors = {
        "|": (0.5, 0, 0.5, 1),
        "-": (0, 0.5, 1, 0.5),
        "L": (0.5, 0, 1, 0.5),
        "J": (0.5, 0, 0, 0.5),
        "7": (0, 0.5, 0.5, 1),
        "F": (1, 0.5, 0.5, 1),
    }

    def part1(self, input):
        # find starting position
        self.grid = input.rstrip().split("\n")
        self.maxX = len(self.grid[0])
        self.maxY = len(self.grid)
        startX = None
        startY = None

        for x, y in product(range(self.maxX), range(self.maxY)):
            if self.grid[y][x] == "S":
                startX = x
                startY = y
                break

        # calculate reachability. This method is very slow!
        self.reachability = [[None for x in range(
            self.maxX)] for y in range(self.maxY)]
        self.reachability[startY][startX] = 0
        self.flood(startX, startY)

        # find the maximum value
        m = 0
        for x, y in product(range(self.maxX), range(self.maxY)):
            c = self.reachability[y][x]
            if c != None:
                m = max(m, c)

        return m

    def flood(self, startX, startY):
      queue = [(startX, startY, 0)]
      while len(queue) > 0:
        (currentX, currentY, currentN) = queue.pop(0)
        if self.reachability[currentY][currentX] < currentN:
          continue
        current = self.grid[currentY][currentX]
        for dir in Day10.pipes[current]:
          newX = currentX + dir[0]
          if newX < 0 or newX >= self.maxX:
            continue

          newY = currentY + dir[1]
          if newY < 0 or newY >= self.maxY:
            continue

          targetCell = self.grid[newY][newX]
          pipe = Day10.pipes[targetCell]
          if (-dir[0], -dir[1]) not in pipe:
            continue

          c2 = self.reachability[newY][newX]
          if c2 == None or c2 > currentN + 1:
            self.reachability[newY][newX] = currentN + 1
            queue.append((newX, newY, currentN + 1))

    def part2(self, input):
        # find starting position
        self.grid = input.rstrip().split("\n")
        self.maxX = len(self.grid[0])
        self.maxY = len(self.grid)
        startX = None
        startY = None

        for x, y in product(range(self.maxX), range(self.maxY)):
            if self.grid[y][x] == "S":
                startX = x
                startY = y
                break

        # calculate reachability. This method is very slow!
        self.reachability = [[None for x in range(
            self.maxX)] for y in range(self.maxY)]
        self.reachability[startY][startX] = 0
        self.flood(startX, startY)

        # # print reachability
        # for y, x in product(range(self.maxY), range(self.maxX)):
        #   if x == 0:
        #     print("\n")
        #   if self.reachability[y][x] != None:
        #     print('{0: <3}'.format(self.reachability[y][x]), end=" ")
        #   else:
        #     print("   ", end=" ")
        # print()

        # figure out which character S needs to be
        for pipe, v in Day10.pipes.items():
            ok = True
            for offset in v:
                if self.reachability[startY + offset[1]][startX + offset[0]] != 1:
                    ok = False
                    break
            if ok:
                self.grid[startY] = list(self.grid[startY])
                self.grid[startY][startX] = pipe
                break

        # # print grid
        # for y, x in product(range(self.maxY), range(self.maxX)):
        #   if x == 0:
        #     print("\n")
        #   if self.reachability[y][x] != None:
        #     print('{0: <3}'.format(self.grid[y][x]), end=" ")
        #   else:
        #     print("   ", end=" ")
        # print()

        # convert grid to vectors
        self.vectorGrid = []
        for x, y in product(range(self.maxX), range(self.maxY)):
            if self.reachability[y][x] != None:
                vector = Day10.vectors[self.grid[y][x]]
                self.vectorGrid.append(
                    ((x + vector[0], y + vector[1]), (x + vector[2], y + vector[3])))

        # compute how many intersections we have from each cell's center.
        sum = 0
        for x, y in product(range(self.maxX), range(self.maxY)):
            if self.reachability[y][x] == None:
                if self.isInside(x, y):
                    sum += 1

        return sum

    # TODO: check if intersection goes thru a point, in which case we
    # should restart with a different random point.
    def isInside(self, x, y):
        n = 0
        for v in self.vectorGrid:
            if Day10.intersects(((0, 0), (x+0.5, y+0.5)), v):
                n += 1
        return n % 2

    def intersects(s0, s1):
        dx0 = s0[1][0]-s0[0][0]
        dx1 = s1[1][0]-s1[0][0]
        dy0 = s0[1][1]-s0[0][1]
        dy1 = s1[1][1]-s1[0][1]
        p0 = dy1*(s1[1][0]-s0[0][0]) - dx1*(s1[1][1]-s0[0][1])
        p1 = dy1*(s1[1][0]-s0[1][0]) - dx1*(s1[1][1]-s0[1][1])
        p2 = dy0*(s0[1][0]-s1[0][0]) - dx0*(s0[1][1]-s1[0][1])
        p3 = dy0*(s0[1][0]-s1[1][0]) - dx0*(s0[1][1]-s1[1][1])
        return (p0*p1 <= 0) & (p2*p3 <= 0)

    def generateSvg(self):
      d = draw.Drawing(self.maxX, self.maxY)
      for x, y in product(range(self.maxX), range(self.maxY)):
        if self.grid[y][x] == ".":
          continue
        vector = Day10.vectors[self.grid[y][x]]
        if self.reachability[y][x] != None:
          d.append(draw.Lines(x + vector[0], y + vector[1], x + vector[2], y + vector[3], close=False, stroke_width=0.05, stroke='blue'))
        else:
          d.append(draw.Lines(x + vector[0], y + vector[1], x + vector[2], y + vector[3], close=False, stroke_width=0.02, stroke='black'))
      d.set_pixel_scale(10)
      d.save_svg('visualization.svg')


class TestDay10(unittest.TestCase):
    def testPart1(self):
        self.assertEqual(Day10().part1("""-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""), 4)
        self.assertEqual(Day10().part1("""7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""), 8)

    def testPart2(self):
        self.assertEqual(Day10().part2("""...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""), 4)

        self.assertEqual(Day10().part2("""..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
.........."""), 4)

        self.assertEqual(Day10().part2(""".F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""), 8)

        self.assertEqual(Day10().part2("""FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""), 10)


print("day 10, part 1: ", Day10().part1(pathlib.Path("input").read_text()))
print("day 10, part 2: ", Day10().part2(pathlib.Path("input").read_text()))
unittest.main()
