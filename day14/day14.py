import unittest
import pathlib
import numpy
import math


class Day14:
    def part1(input):
        grid = Day14.parse(input)
        Day14.moveUp(grid)
        return Day14.totalLoad(grid)

    def part2(input):
        grid = Day14.parse(input)
        seen = {}
        i = 0
        while i < 1000000000:
            Day14.cycle(grid)
            s = Day14.str(grid)
            if s in seen:
                delta = i - seen[s]
                t = math.floor((1000000000 - i) / delta)
                i += t * delta
            seen[s] = i
            i += 1
        return Day14.totalLoad(grid)

    def parse(input):
        return numpy.asarray(list(map(list, input.rstrip().split("\n"))))

    def moveUp(grid):
        for x in range(0, len(grid[0])):
            count = 0
            prevY = 0
            for y in range(0, len(grid)):
                if grid[y][x] == "O":
                    count += 1
                    grid[y][x] = "."
                elif grid[y][x] == "#":
                    for y2 in range(prevY, prevY + count):
                        grid[y2][x] = "O"
                    count = 0
                    prevY = y+1
            for y2 in range(prevY, prevY + count):
                grid[y2][x] = "O"

    def totalLoad(grid):
        sum = 0
        for j in range(0, len(grid)):
            for i in range(0, len(grid[0])):
                if grid[j][i] == "O":
                    sum += len(grid) - j
        return sum

    def cycle(grid):
        for i in range(0, 4):
            Day14.moveUp(grid)
            grid = numpy.rot90(grid, k=-1)

    def str(grid):
        r = "\n".join(map("".join, grid))
        return r


class TestDay14(unittest.TestCase):
    def testMoveUp(self):
        grid = Day14.parse("""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""")
        Day14.moveUp(grid)
        self.assertEqual(Day14.str(grid), """OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....""")

    def testPart1(self):
        self.assertEqual(Day14.part1("""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""), 136)

    def testPart2(self):
        grid = Day14.parse("""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""")

        # After 1 cycle
        Day14.cycle(grid)
        self.assertEqual(Day14.str(grid), """.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....""")

        # After 2 cycles
        Day14.cycle(grid)
        self.assertEqual(Day14.str(grid), """.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O""")

        # After 3 cycles
        Day14.cycle(grid)
        self.assertEqual(Day14.str(grid), """.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O""")

        self.assertEqual(Day14.part2("""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""), 64)


print("day 14, part 1: ", Day14.part1(pathlib.Path("input").read_text()))
print("day 14, part 2: ", Day14.part2(pathlib.Path("input").read_text()))
unittest.main()
