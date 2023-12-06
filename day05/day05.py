import unittest
import pathlib
import re


class Day05:
    def part1(input):
        pieces = input.rstrip().split("\n\n")
        seeds = re.findall("\d+", pieces[0])

        m = float("inf")
        for seed in seeds:
            n = Day05.compute(int(seed), pieces[1:])
            m = min(m, n)
        return m

    def compute(id, remainingRules):
        if len(remainingRules) == 0:
            return id
        rules = remainingRules[0].split("\n")[1:]
        for rule in rules:
            (dest, source, l) = rule.split(" ")
            t = id - int(source)
            if t >= 0 and t < int(l):
                return Day05.compute(int(dest) + t, remainingRules[1:])
        return Day05.compute(id, remainingRules[1:])

    def part2(input):
        pieces = input.rstrip().split("\n\n")
        seeds = re.findall("\d+", pieces[0])

        m = float("inf")
        for i in range(0, len(seeds), 2):
            start = int(seeds[i])
            length = int(seeds[i+1])

            n = Day05.computePart2(start, length, pieces[1:])
            m = min(m, n)
        return m

    def computePart2(current, length, remainingRules):
        if length < 0:
            raise Exception("length is negative!")
        if length == 0:
            raise Exception("length is zero!")
        if len(remainingRules) == 0:
            return current
        rules = remainingRules[0].split("\n")[1:]
        for rule in rules:
            (dest, source, l) = rule.split(" ")
            dest = int(dest)
            source = int(source)
            l = int(l)

            # check for overlapping ranges
            left = max(current, source)
            right = min(current + length, source + l)
            if left >= right:
                # case 1:        current
                #         rule

                # case 2:  current
                #                   rule
                continue

            # [left, right[ represents the overlap between the two regions
            v1 = float("inf")
            v2 = float("inf")
            v3 = float("inf")
            if current < left:
                # we have a bit of region to the left
                v1 = Day05.computePart2(
                    current, left - current, remainingRules)
            if current + length > right:
                # we have a bit of region to the right
                v2 = Day05.computePart2(right, current + length -
                                        right, remainingRules)
            v3 = Day05.computePart2(left + dest - source, right -
                                    left, remainingRules[1:])
            return min(v1, v2, v3)
        return Day05.computePart2(current, length, remainingRules[1:])


class TestDay05(unittest.TestCase):
    def testPart1(self):
        self.assertEqual(Day05.part1("""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""), 35)

    def testPart2(self):
        self.assertEqual(Day05.part2("""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""), 46)


print("day 05, part 1: ", Day05.part1(pathlib.Path("input").read_text()))
print("day 05, part 2: ", Day05.part2(pathlib.Path("input").read_text()))

unittest.main()
