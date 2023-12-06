import re
import math 

# little bit of math today...

def part1(file):
  with open(file) as infile:
    data = infile.read().rstrip()
  (time, distance) = data.split("\n")
  times = map(int, re.findall("\d+", time))
  distances = map(int, re.findall("\d+", distance))
  result = 1
  for (t, d) in zip(times, distances):
    min = math.floor((t - math.sqrt(t*t - 4 * d))/2)+1
    max = math.ceil((t + math.sqrt(t*t - 4 * d))/2)-1
    result *= max - min + 1
  return result

def part2(file):
  with open(file) as infile:
    data = infile.read().rstrip()
  (time, distance) = data.split("\n")
  t = int("".join(re.findall("\d+", time)))
  d = int("".join(re.findall("\d+", distance)))
  min = math.floor((t - math.sqrt(t*t - 4 * d))/2)+1
  max = math.ceil((t + math.sqrt(t*t - 4 * d))/2)-1
  return max - min + 1

print("part 1, test: ", part1("test.txt"))
print("part 1, input: ", part1("input.txt"))
print("part 2, test: ", part2("test.txt"))
print("part 2, input: ", part2("input.txt"))
