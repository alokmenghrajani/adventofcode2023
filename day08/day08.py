import re
import math
import itertools

def part1(file):
  with open(file) as infile:
    data = infile.read().rstrip().split("\n\n")
  moves = data[0]
  mapping = {}
  for line in data[1].split("\n"):
    m = re.match("(...) = \((...), (...)\)", line)
    mapping[m.group(1)] = (m.group(2), m.group(3))

  current = "AAA"
  for step, move in enumerate(itertools.cycle(moves)):
    if current == "ZZZ":
      return step
    if move == "L":
      current = mapping[current][0]
    elif move == "R":
      current = mapping[current][1]
    else:
      raise Exception("hmm: " + move)

def part2(file):
  with open(file) as infile:
    data = infile.read().rstrip().split("\n\n")
  moves = data[0]
  mapping = {}
  ghosts = []
  for line in data[1].split("\n"):
    m = re.match("(...) = \((...), (...)\)", line)
    mapping[m.group(1)] = (m.group(2), m.group(3))
    if m.group(1)[-1] == "A":
      ghosts.append(m.group(1))
  
  lengths = []
  for ghost in ghosts:
    lengths.append(compute_length(ghost, moves, mapping))
  
  # LCM only works if the paths have specific properties...
  return math.lcm(*lengths)

def compute_length(current, moves, mapping):
  for step, move in enumerate(itertools.cycle(moves)):
    if current[-1] == "Z":
      return step
    if move == "L":
      current = mapping[current][0]
    elif move == "R":
      current = mapping[current][1]
    else:
      raise Exception("hmm: " + move)

print("part 1, test 1: ", part1("test1.txt"))
print("part 1, test 2: ", part1("test2.txt"))
print("part 1, input: ", part1("input.txt"))
print("part 2, test 3: ", part2("test3.txt"))
print("part 2, input: ", part2("input.txt"))