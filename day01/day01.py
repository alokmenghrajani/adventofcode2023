import unittest
import pathlib

class Day01:
  def part1(input):
      sum = 0
      for line in input.rstrip().split("\n"):
          sum += Day01.calibrationValue(line)
      return sum


  def calibrationValue(str):
      n = None

      # find first number
      for c in str:
          if c >= '0' and c <= '9':
              n = int(c) * 10
              break

      # find last number
      for c in reversed(str):
          if c >= '0' and c <= '9':
              n += int(c)
              break

      return n


  def part2(input):
      sum = 0
      for line in input.rstrip().split("\n"):
          sum += Day01.calibrationValuePart2(line)
      return sum


  def calibrationValuePart2(str):
      n = None

      # find first number
      for i in range(0, len(str)):
          t = Day01.value(str[i:])
          if t != None:
              n = t * 10
              break

      # find last number
      for i in range(len(str)-1, -1, -1):
          t = Day01.value(str[i:])
          if t != None:
              n += t
              break

      return n


  def value(str):
      c = str[0]
      if c >= '0' and c <= '9':
          return int(c)
      if str.startswith('one'):
          return 1
      if str.startswith('two'):
          return 2
      if str.startswith('three'):
          return 3
      if str.startswith('four'):
          return 4
      if str.startswith('five'):
          return 5
      if str.startswith('six'):
          return 6
      if str.startswith('seven'):
          return 7
      if str.startswith('eight'):
          return 8
      if str.startswith('nine'):
          return 9


class TestDay01(unittest.TestCase):
    def testCalibrationValue(self):
        self.assertEqual(Day01.calibrationValue("1abc2"), 12)
        self.assertEqual(Day01.calibrationValue("pqr3stu8vwx"), 38)
        self.assertEqual(Day01.calibrationValue("a1b2c3d4e5f"), 15)
        self.assertEqual(Day01.calibrationValue("treb7uchet"), 77)

    def testPart1(self):
        self.assertEqual(Day01.part1("""1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""), 142)

    def testCalibrationValuePart2(self):
        self.assertEqual(Day01.calibrationValuePart2("two1nine"), 29)
        self.assertEqual(Day01.calibrationValuePart2("eightwothree"), 83)
        self.assertEqual(Day01.calibrationValuePart2("abcone2threexyz"), 13)
        self.assertEqual(Day01.calibrationValuePart2("xtwone3four"), 24)
        self.assertEqual(Day01.calibrationValuePart2("4nineeightseven2"), 42)
        self.assertEqual(Day01.calibrationValuePart2("zoneight234"), 14)
        self.assertEqual(Day01.calibrationValuePart2("7pqrstsixteen"), 76)

    def testPart2(self):
        self.assertEqual(Day01.part2("""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""), 281)


print("day 01, part 1: ", Day01.part1(pathlib.Path("input").read_text()))
print("day 02, part 2: ", Day01.part2(pathlib.Path("input").read_text()))

unittest.main()
