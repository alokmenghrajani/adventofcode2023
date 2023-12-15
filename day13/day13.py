import unittest
import pathlib
import numpy


class Day13:
    def part1(self, input):
        r = 0
        patterns = input.rstrip().split("\n\n")
        for pattern in patterns:
            arr = numpy.asarray(list(map(list, pattern.split("\n"))))
            vert = self.findReflection(arr, 0)
            for v in vert:
                r += (v + 1)
            arr = arr.transpose()
            horz = self.findReflection(arr, 0)
            for h in horz:
                r += (h + 1) * 100
        return r

    def part2(self, input):
        r = 0
        patterns = input.rstrip().split("\n\n")
        for pattern in patterns:
            arr = numpy.asarray(list(map(list, pattern.split("\n"))))
            vert = self.findReflection(arr, 1)
            for v in vert:
                r += (v + 1)
            arr = arr.transpose()
            horz = self.findReflection(arr, 1)
            for h in horz:
                r += (h + 1) * 100
        return r

    def findReflection(self, arr, mismatches):
        r = []
        for i in range(0, len(arr[0])-1):
            if self.isReflection(arr, i, mismatches):
                r.append(i)
        return r

    def isReflection(self, arr, offset, mismatches):
        m = 0
        for i in range(0, offset+1):
            j = 2 * offset + 1 - i
            if j >= len(arr[0]):
                continue

            for k in range(0, len(arr)):
                if arr[k][i] != arr[k][j]:
                    m += 1
                    if m > mismatches:
                        return False
        return m == mismatches


class TestDay13(unittest.TestCase):
    def testPart1(self):
        self.assertEqual(Day13().part1("""#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""), 405)

    def testPart2(self):
        self.assertEqual(Day13().part2("""#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""), 400)


print("day 13, part 1: ", Day13().part1(pathlib.Path("input").read_text()))
print("day 13, part 2: ", Day13().part2(pathlib.Path("input").read_text()))
unittest.main()
