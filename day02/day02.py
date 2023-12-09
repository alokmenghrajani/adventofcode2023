import unittest
import pathlib
import re


class Day02:
    def part1(input):
        sum = 0
        for line in input.rstrip().split("\n"):
            m = re.match('Game (\d+):', line)
            id = m.group(1)
            line = line[len(m.group(0)):]
            if Day02.isOk(line):
                sum += int(id)
        return sum

    def isOk(str):
        matches = re.findall('(\d+) (red|green|blue)', str)
        for m in matches:
            if m[1] == "red" and int(m[0]) > 12:
                return False
            if m[1] == "green" and int(m[0]) > 13:
                return False
            if m[1] == "blue" and int(m[0]) > 14:
                return False
        return True

    def part2(input):
        sum = 0
        for line in input.rstrip().split("\n"):
            m = re.match('Game (\d+):', line)
            id = m.group(1)
            line = line[len(m.group(0)):]
            games = line.split(";")
            power = [0, 0, 0]
            for game in games:
                Day02.calcPower(game, power)
            sum += power[0] * power[1] * power[2]
        return sum

    def calcPower(str, power):
        matches = re.findall('(\d+) (red|green|blue)', str)
        for m in matches:
            if m[1] == "red":
                power[0] = max(power[0], int(m[0]))
            if m[1] == "green":
                power[1] = max(power[1], int(m[0]))
            if m[1] == "blue":
                power[2] = max(power[2], int(m[0]))


class TestDay02(unittest.TestCase):
    def testIsOk(self):
        self.assertTrue(Day02.isOk(
            "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"))

    def testPart1(self):
        self.assertEqual(Day02.part1("""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""), 8)

    def testPower(self):
        t = [0, 0, 0]
        Day02.calcPower("3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", t)
        self.assertEqual(t, [4, 2, 6])

        t = [0, 0, 0]
        Day02.calcPower(
            "1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", t)
        self.assertEqual(t, [1, 3, 4])

        t = [0, 0, 0]
        Day02.calcPower(
            "8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", t)
        self.assertEqual(t, [20, 13, 6])

        t = [0, 0, 0]
        Day02.calcPower(
            "1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", t)
        self.assertEqual(t, [14, 3, 15])

        t = [0, 0, 0]
        Day02.calcPower("6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", t)
        self.assertEqual(t, [6, 3, 2])

    def testPart2(self):
        self.assertEqual(Day02.part2("""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""), 2286)


print("day 02, part 1: ", Day02.part1(pathlib.Path("input").read_text()))
print("day 02, part 2: ", Day02.part2(pathlib.Path("input").read_text()))

unittest.main()
