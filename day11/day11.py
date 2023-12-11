import unittest
import pathlib
from itertools import product

# Day 11:
# I initially implemented part1 with code that expanded the grid (quite
# painful to implement). I then simplified everything for part2.


class Day11:
    def part1(input, expansion=2):
        return Day11.common(input, expansion)

    def part2(input, expansion=1000000):
        return Day11.common(input, expansion)

    def common(input, expansion):
        grid = []
        for line in input.rstrip().split("\n"):
            grid.append(list(line))
        maxY = len(grid)
        maxX = len(grid[0])

        rows = []
        for y in range(maxY):
            empty = True
            for x in range(maxX):
                if grid[y][x] != ".":
                    empty = False
                    break
            if empty:
                rows.append(y)

        cols = []
        for x in range(maxX):
            empty = True
            for y in range(maxY):
                if grid[y][x] != ".":
                    empty = False
                    break
            if empty:
                cols.append(x)

        galaxies = []
        for x, y in product(range(maxX), range(maxY)):
            if grid[y][x] == '#':
                newX = x
                for i in cols:
                    if x > i:
                        newX += expansion-1

                newY = y
                for j in rows:
                    if y > j:
                        newY += expansion-1

                galaxies.append((newX, newY))

        sum = 0
        for i in range(len(galaxies)):
            for j in range(i+1, len(galaxies)):
                g1 = galaxies[i]
                g2 = galaxies[j]
                d = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
                sum += d
        return sum


class TestDay11(unittest.TestCase):
    def testPart1(self):
        self.assertEqual(Day11.part1("""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""), 374)

    def testPart2(self):
        self.assertEqual(Day11.part2("""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""", expansion=10), 1030)
        self.assertEqual(Day11.part2("""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""", expansion=100), 8410)


print("day 11, part 1: ", Day11.part1(pathlib.Path("input").read_text()))
print("day 11, part 2: ", Day11.part2(pathlib.Path("input").read_text()))
unittest.main()
