import copy


def part1(file):
    with open(file) as infile:
        sum = 0
        for line in infile:
            data = map(int, line.rstrip().split(" "))
            n = computeNext(data)
            sum += n
    return sum


def computeNext(data):
    # convert data to a dict, this makes memoization easier without having
    # to deal with a sparse 2D array.
    d = {}
    size = 0
    for i, n in enumerate(data):
        d[(i, 0)] = n
        size += 1

    s = 0
    x = size - 1
    y = 0

    # We don't know when to stop, so we go size steps
    for y in range(0, size):
        t = computeExisting(d, x, y)
        s += t
        x -= 1

    return s


def computeExisting(d, x, y):
    if x < 0:
        raise Exception("Oops")
    if (x, y) in d:
        return d[(x, y)]
    t = computeExisting(d, x+1, y-1) - computeExisting(d, x, y-1)
    d[(x, y)] = t
    return t


def part2(file):
    with open(file) as infile:
        sum = 0
        for line in infile:
            data = map(int, reversed(line.rstrip().split(" ")))
            n = computeNext(data)
            sum += n
    return sum


print("part 1, test: ", part1("test.txt"))
print("part 1, input: ", part1("input.txt"))
print("part 2, test: ", part2("test.txt"))
print("part 2, input: ", part2("input.txt"))
