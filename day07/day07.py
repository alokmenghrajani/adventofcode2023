import functools

def part1(file):
  cards = []
  with open(file) as infile:
    for line in infile:
      (hand, bid) = line.split(" ")
      bid = int(bid)
      v = value(hand)
      cards.append((hand, bid, v))
  cards.sort(key=functools.cmp_to_key(cmp))
  sum = 0
  for k, v in enumerate(cards, 1):
    sum += k * v[1]
  return sum

def value(hand):
  m = {}
  for c in hand:
    if c in m:
      m[c] += 1
    else:
      m[c] = 1
  values = sorted(m.values(), reverse=True)
  if values[0] == 5:
    return 6
  if values[0] == 4:
    return 5
  if values[0] == 3 and values[1] == 2:
    return 4
  if values[0] == 3:
    return 3
  if values[0] == 2 and values[1] == 2:
    return 2
  if values[0] == 2:
    return 1
  return 0  

def cmp(this, other):
  (hand1, _, v1) = this
  (hand2, _, v2) = other
  if v1 > v2:
    return 1
  if v1 < v2:
    return -1

  values = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
  }
  for (h1, h2) in zip(hand1, hand2):
    if values[h1] > values[h2]:
      return 1
    if values[h1] < values[h2]:
      return -1

  return 0

def part2(file):
  cards = []
  with open(file) as infile:
    for line in infile:
      (hand, bid) = line.split(" ")
      bid = int(bid)
      v = valuePart2(hand)
      cards.append((hand, bid, v))
  cards.sort(key=functools.cmp_to_key(cmpPart2))
  sum = 0
  for k, v in enumerate(cards, 1):
    sum += k * v[1]
  return sum

def valuePart2(hand):
  m = {"J": 0}
  for c in hand:
    if c in m:
      m[c] += 1
    else:
      m[c] = 1
  jokers = m["J"]
  if jokers == 5:
    # much sadness at having to special case this...
    return 6

  del m["J"]
  values = sorted(m.values(), reverse=True)
  values[0] += jokers
  if values[0] == 5:
    return 6
  if values[0] == 4:
    return 5
  if values[0] == 3 and values[1] == 2:
    return 4
  if values[0] == 3:
    return 3
  if values[0] == 2 and values[1] == 2:
    return 2
  if values[0] == 2:
    return 1
  return 0  

def cmpPart2(this, other):
  (hand1, _, v1) = this
  (hand2, _, v2) = other
  if v1 > v2:
    return 1
  if v1 < v2:
    return -1

  values = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
  }
  for (h1, h2) in zip(hand1, hand2):
    if values[h1] > values[h2]:
      return 1
    if values[h1] < values[h2]:
      return -1

  return 0

print("part 1, test: ", part1("test.txt"))
print("part 1, input: ", part1("input.txt"))
print("part 2, test: ", part2("test.txt"))
print("part 2, input: ", part2("input.txt"))
