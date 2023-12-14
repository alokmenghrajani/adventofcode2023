import unittest
import pathlib
import functools

# Day 12:
# The process of computing permutations feel very much like implementing a
# regular expression engine. I bet there's a way to build a finite state machine
# and efficiently calculate permutations without having to backtrack or memoize
# things.


class Day12:
    def part1(input):
        sum = 0
        for line in input.rstrip().split("\n"):
            sum += Day12().permutations(line)
        return sum

    def permutations(self, line):
        self.cache = {}
        springs, groups = line.split(" ")
        self.groups = list(map(int, groups.split(",")))
        return self.computePermutations(springs + ".", 0, 0)

    def part2(input):
        sum = 0
        for line in input.rstrip().split("\n"):
            sum += Day12().permutationsPart2(line)
        return sum

    def permutationsPart2(self, line):
        self.cache = {}
        springs, groups = line.split(" ")
        springs = "?".join([springs] * 5)
        groups = ",".join([groups] * 5)
        self.groups = list(map(int, groups.split(",")))
        r = self.computePermutations(springs + ".", 0, 0)
        return r

    # We recursively consume springs and groups. We keep track of how many "#"
    # we have just consumed. When we encounter a "." after a "#", we check
    # to see if the number of consumed "#" matches the consumed group.
    @functools.cache
    def computePermutations(self, springs, groupsIndex, processed):
        if springs == "":
            if groupsIndex == len(self.groups):
                # we are done!
                return 1
            else:
                return 0

        if springs[0] == ".":
            if processed != 0:
                if processed != self.groups[groupsIndex]:
                    return 0
                return self.computePermutations(springs[1:], groupsIndex+1, 0)
            else:
                return self.computePermutations(springs[1:], groupsIndex, 0)

        if springs[0] == "#":
            if groupsIndex == len(self.groups) or processed > self.groups[groupsIndex]:
                # Early exit, this group won't succeed
                return 0
            return self.computePermutations(springs[1:], groupsIndex, processed + 1)

        if springs[0] == "?":
            r = self.computePermutations(
                "#" + springs[1:], groupsIndex, processed)
            r += self.computePermutations("." +
                                          springs[1:], groupsIndex, processed)
            return r

        raise Exception("unexpected input: " + springs[0])


class TestDay12(unittest.TestCase):
    def testPermutations(self):
        self.assertEqual(Day12.permutations("???.### 1,1,3"), 1)
        self.assertEqual(Day12.permutations(".??..??...?##. 1,1,3"), 4)
        self.assertEqual(Day12.permutations("?#?#?#?#?#?#?#? 1,3,1,6"), 1)
        self.assertEqual(Day12.permutations("????.#...#... 4,1,1"), 1)
        self.assertEqual(Day12.permutations("????.######..#####. 1,6,5"), 4)
        self.assertEqual(Day12.permutations("?###???????? 3,2,1"), 10)

    def testPart1(self):
        self.assertEqual(Day12.part1("""???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""), 21)

    def testPermutations(self):
        self.assertEqual(Day12().permutationsPart2("???.### 1,1,3"), 1)
        self.assertEqual(Day12().permutationsPart2(
            ".??..??...?##. 1,1,3"), 16384)
        self.assertEqual(Day12().permutationsPart2(
            "?#?#?#?#?#?#?#? 1,3,1,6"), 1)
        self.assertEqual(Day12().permutationsPart2("????.#...#... 4,1,1"), 16)
        self.assertEqual(Day12().permutationsPart2(
            "????.######..#####. 1,6,5"), 2500)
        self.assertEqual(Day12().permutationsPart2(
            "?###???????? 3,2,1"), 506250)


print("day 12, part 1: ", Day12.part1(pathlib.Path("input").read_text()))
print("day 12, part 2: ", Day12.part2(pathlib.Path("input").read_text()))
unittest.main()
