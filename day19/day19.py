import unittest
import pathlib
import re
import copy


class Day19:
    def part1(self, input):
        input_workflows, input_parts = input.rstrip().split("\n\n")
        self.workflows = {}

        # Parse workflows
        for line in input_workflows.split("\n"):
            m = re.match("(.+){(.*)}", line)
            name = m[1]
            rules = []
            for r in m[2].split(","):
                m = re.match("(.+)([<>])(\d+):(.+)", r)
                if m:
                    rules.append(((m[1], m[2], m[3]), m[4]))
                else:
                    rules.append((None, r))
            self.workflows[name] = rules

        # Parse parts
        accepted = 0
        for line in input_parts.split("\n"):
            m = re.match("{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}", line)
            part = {}
            part["x"] = int(m[1])
            part["m"] = int(m[2])
            part["a"] = int(m[3])
            part["s"] = int(m[4])
            if self.accepted(part, "in"):
                accepted += part["x"] + part["m"] + part["a"] + part["s"]
        return accepted

    def part2(self, input):
        input_workflows, input_parts = input.rstrip().split("\n\n")
        self.workflows = {}

        # Parse workflows
        for line in input_workflows.split("\n"):
            m = re.match("(.+){(.*)}", line)
            name = m[1]
            rules = []
            for r in m[2].split(","):
                m = re.match("(.+)([<>])(\d+):(.+)", r)
                if m:
                    rules.append(((m[1], m[2], m[3]), m[4]))
                else:
                    rules.append((None, r))
            self.workflows[name] = rules

        # Starting from "in" count the number of possible parts
        part = {}
        part["x"] = (1, 4000)
        part["m"] = (1, 4000)
        part["a"] = (1, 4000)
        part["s"] = (1, 4000)
        return self.possible(part, "in")

    def accepted(self, part, workflow_name):
        if workflow_name == "A":
            return True
        if workflow_name == "R":
            return False
        for condition, effect in self.workflows[workflow_name]:
            if condition == None:
                return self.accepted(part, effect)
            left, op, right = condition
            if op == "<":
                if part[left] < int(right):
                    return self.accepted(part, effect)
            if op == ">":
                if part[left] > int(right):
                    return self.accepted(part, effect)
        raise Exception("hmm")

    def possible(self, part, workflow_name):
        min_value_x, max_value_x = part["x"]
        if min_value_x > max_value_x:
            return 0

        min_value_m, max_value_m = part["m"]
        if min_value_m > max_value_m:
            return 0

        min_value_a, max_value_a = part["a"]
        if min_value_a > max_value_a:
            return 0

        min_value_s, max_value_s = part["s"]
        if min_value_s > max_value_s:
            return 0

        if workflow_name == "A":
            return (max_value_x - min_value_x + 1) * \
                (max_value_m - min_value_m + 1) * \
                (max_value_a - min_value_a + 1) * \
                (max_value_s - min_value_s + 1)
        if workflow_name == "R":
            return 0

        total = 0
        for condition, effect in self.workflows[workflow_name]:
            if condition == None:
                return total + self.possible(part, effect)
            left, op, right = condition
            if op == "<":
                new_part = copy.copy(part)
                min_value, max_value = part[left]
                new_part[left] = (min_value, int(right) - 1)
                total += self.possible(new_part, effect)
                part[left] = (int(right), max_value)
            if op == ">":
                new_part = copy.copy(part)
                min_value, max_value = part[left]
                new_part[left] = (int(right) + 1, max_value)
                total += self.possible(new_part, effect)
                part[left] = (min_value, int(right))
        raise Exception("hmm")


class TestDay19(unittest.TestCase):
    def testPart1(self):
        self.assertEqual(Day19().part1("""px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""), 19114)

    def testPart2(self):
        self.assertEqual(Day19().part2("""px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""), 167409079868000)


print("day 19, part 1: ", Day19().part1(pathlib.Path("input").read_text()))
print("day 19, part 2: ", Day19().part2(pathlib.Path("input").read_text()))
unittest.main()
