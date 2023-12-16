import unittest
import pathlib


class Day15:
    def part1(input):
        sum = 0
        for s in input.rstrip().split(","):
            sum += Day15.hash(s)
        return sum

    def part2(input):
        focal = {}
        boxes = [None] * 256
        boxes = list(map(lambda x: [], boxes))
        for s in input.rstrip().split(","):
            Day15.processPart2(boxes, focal, s)

        sum = 0
        for k, v in enumerate(boxes):
            for offset, label in enumerate(v):
                p = k + 1
                p = p * (offset + 1)
                p = p * focal[label]
                sum += p
        return sum

    def hash(str):
        r = 0
        for c in str:
            r += ord(c)
            r *= 17
            r = r % 256
        return r

    def processPart2(boxes, focal, str):
        if str[-1] == "-":
            label = str[:-1]
            box_id = Day15.hash(label)
            if label in boxes[box_id]:
                boxes[box_id].remove(label)
        else:
            label, f = str.split("=")
            focal[label] = int(f)
            box_id = Day15.hash(label)
            if label not in boxes[box_id]:
                boxes[box_id].append(label)


class TestDay15(unittest.TestCase):
    def testHash(self):
        self.assertEqual(Day15.hash("rn=1"), 30)
        self.assertEqual(Day15.hash("cm-"), 253)
        self.assertEqual(Day15.hash("qp=3"), 97)
        self.assertEqual(Day15.hash("cm=2"), 47)
        self.assertEqual(Day15.hash("qp-"), 14)
        self.assertEqual(Day15.hash("pc=4"), 180)
        self.assertEqual(Day15.hash("ot=9"), 9)
        self.assertEqual(Day15.hash("ab=5"), 197)
        self.assertEqual(Day15.hash("pc-"), 48)
        self.assertEqual(Day15.hash("pc=6"), 214)
        self.assertEqual(Day15.hash("ot=7"), 231)

    def testPart1(self):
        self.assertEqual(Day15.part1(
            "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"), 1320)

    def testPart2(self):
        self.assertEqual(Day15.part2(
            "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"), 145)


print("day 15, part 1: ", Day15.part1(pathlib.Path("input").read_text()))
print("day 15, part 2: ", Day15.part2(pathlib.Path("input").read_text()))
unittest.main()
