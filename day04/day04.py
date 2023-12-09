import unittest
import pathlib
import re


class Day04:
    def part1(input):
        sum = 0
        for y, line in enumerate(input.rstrip().split("\n")):
            _, numbers = line.split(":")
            winnings, yours = numbers.split("|")
            winning = re.findall("\d+", winnings)
            your = re.findall("\d+", yours)
            n = 0
            for y in your:
                for w in winning:
                    if y == w:
                        n += 1
            sum += int(2**(n-1))
        return sum

    def part2(input):
        mapping = dict()
        mapping2 = dict()

        for id, line in enumerate(input.rstrip().split("\n")):
            id += 1
            mapping[id] = Day04.score(id, line)
            mapping2[id] = 1

        while len(mapping) > 0:
            for k, v in mapping.items():
                if (len(v)) == 0:
                    Day04.remove(mapping, mapping2, k)
                    break

        sum = 0
        for k, v in mapping2.items():
            sum += v
        return sum

    def score(id, card):
        _, numbers = card.split(":")
        winnings, yours = numbers.split("|")
        winning = re.findall("\d+", winnings)
        your = re.findall("\d+", yours)
        n = 0
        for y in your:
            for w in winning:
                if y == w:
                    n += 1
        return set([*range(id+1, id+1+n)])

    def remove(mapping, mapping2, el):
        for k, v in mapping.items():
            if el in v:
                v.remove(el)
                mapping2[k] += mapping2[el]
        del mapping[el]


class TestDay04(unittest.TestCase):
    def testPart1(self):
        self.assertEqual(Day04.part1("""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""), 13)

    def testPart2(self):
        self.assertEqual(Day04.part2("""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""), 30)


print("day 04, part 1: ", Day04.part1(pathlib.Path("input").read_text()))
print("day 04, part 2: ", Day04.part2(pathlib.Path("input").read_text()))

unittest.main()
