import unittest
import pathlib
import re


class Day03:
    def part1(input):
        # first pass, track symbols
        symbols = dict()
        for y, line in enumerate(input.rstrip().split("\n")):
            for x, c in enumerate(line):
                if c == ".":
                    continue
                if c >= '0' and c <= '9':
                    continue
                symbols[(x, y)] = True

        # second pass, add numbers
        sum = 0

        for y, line in enumerate(input.rstrip().split("\n")):
            for m in re.finditer('\d+', line):
                if Day03.isAdjacent(symbols, y, m.start(), m.end()):
                    sum += int(m.group(0))
        return sum

    def isAdjacent(dict, y, left, right):
        for j in range(y-1, y+2):
            for i in range(left-1, right+1):
                if (i, j) in dict:
                    return True
        return False

    def part2(input):
        # first pass, track symbols
        symbols = dict()
        for y, line in enumerate(input.rstrip().split("\n")):
            for x, c in enumerate(line):
                if c == ".":
                    continue
                if c >= '0' and c <= '9':
                    continue
                symbols[(x, y)] = []

        # second pass, add numbers
        for y, line in enumerate(input.rstrip().split("\n")):
            for m in re.finditer('\d+', line):
                Day03.adjacentPart2(symbols, y, m.start(),
                                    m.end(), int(m.group(0)))

        sum = 0
        for k, v in symbols.items():
            if len(v) == 2:
                sum += v[0] * v[1]
        return sum

    def adjacentPart2(dict, y, left, right, value):
        for j in range(y-1, y+2):
            for i in range(left-1, right+1):
                if (i, j) in dict:
                    dict[(i, j)].append(value)


class TestDay03(unittest.TestCase):
    def testPart1(self):
        self.assertEqual(Day03.part1("""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""), 4361)

    def testPart2(self):
        self.assertEqual(Day03.part2("""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""), 467835)


print("day 03, part 1: ", Day03.part1(pathlib.Path("input").read_text()))
print("day 03, part 2: ", Day03.part2(pathlib.Path("input").read_text()))

unittest.main()
