import unittest
import pathlib

# Useful reading:
# - https://en.wikipedia.org/wiki/Pick%27s_theorem
# - https://en.wikipedia.org/wiki/Shoelace_formula


class Day18:
    def part1(self, input):
        currentX = 0
        currentY = 0
        nodes = [(currentX, currentY)]
        totalAmount = 0
        for line in input.rstrip().split("\n"):
            dir, amount, hex = line.split(" ")
            amount = int(amount)
            if dir == "R":
                currentX += amount
            elif dir == "L":
                currentX -= amount
            elif dir == "U":
                currentY -= amount
            elif dir == "D":
                currentY += amount
            nodes.append((currentX, currentY))
            totalAmount += amount

        area = 0
        for i in range(0, len(nodes)-1):
            x1, y1 = nodes[i]
            x2, y2 = nodes[i+1]
            area += x1 * y2 - x2 * y1
        area = int(area / 2)
        inside = area - int(totalAmount / 2) + 1
        return totalAmount + inside

    def part2(self, input):
        currentX = 0
        currentY = 0
        nodes = [(currentX, currentY)]
        totalAmount = 0
        for line in input.rstrip().split("\n"):
            _, _, hex = line.split(" ")
            amount = int(hex[2:-2], 16)
            dir = hex[-2]
            if dir == "0":
                currentX += amount
            elif dir == "2":
                currentX -= amount
            elif dir == "3":
                currentY -= amount
            elif dir == "1":
                currentY += amount
            nodes.append((currentX, currentY))
            totalAmount += amount

        area = 0
        for i in range(0, len(nodes)-1):
            x1, y1 = nodes[i]
            x2, y2 = nodes[i+1]
            area += x1 * y2 - x2 * y1
        area = int(area / 2)
        inside = area - int(totalAmount / 2) + 1
        return totalAmount + inside


class TestDay18(unittest.TestCase):
    def testPart1(self):
        self.assertEqual(Day18().part1("""R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""), 62)

    def testPart2(self):
        self.assertEqual(Day18().part2("""R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""), 952408144115)


print("day 18, part 1: ", Day18().part1(pathlib.Path("input").read_text()))
print("day 18, part 2: ", Day18().part2(pathlib.Path("input").read_text()))
unittest.main()
