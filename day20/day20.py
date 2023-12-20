import unittest
import pathlib
import math


class Module:
    def __init__(self, name, destinations):
        self.destinations = destinations
        self.type = None
        self.name = name
        self.state = None
        self.last_signal = None

        if name[0] == "%":
            self.name = name[1:]
            self.type = "flip-flop"
            self.state = 0
        elif name[0] == "&":
            self.name = name[1:]
            self.type = "conjunction"
            self.state = {}
        elif name == "broadcaster":
            self.type = "broadcaster"

    def record_input(self, module_name):
        if self.type == "conjunction":
            self.state[module_name] = 0

    def reinit(self):
        if self.type == "flip-flop":
            self.state = 0
        elif self.type == "conjunction":
            for k in self.state:
                self.state[k] = 0

    def process(self, signal_value, signal_from, queue):
        if self.type == "broadcaster":
            for destination in self.destinations:
                queue.append((destination, signal_value, self.name))
            self.last_signal = signal_value
        if self.type == "flip-flop" and signal_value == 0:
            self.state = 1 - self.state
            for destination in self.destinations:
                queue.append((destination, self.state, self.name))
            self.last_signal = self.state
        if self.type == "conjunction":
            self.state[signal_from] = signal_value
            if all(v == 1 for v in self.state.values()):
                for destination in self.destinations:
                    queue.append((destination, 0, self.name))
                self.last_signal = 0
            else:
                for destination in self.destinations:
                    queue.append((destination, 1, self.name))
                self.last_signal = 1


class Day20:
    def part1(self, input):
        self.modules = {}

        # parse input
        for line in input.rstrip().split("\n"):
            module, destinations = line.split(" -> ")
            m = Module(module, destinations.split(", "))
            self.modules[m.name] = m

        # find all untyped outputs
        to_add = []
        for module_name, module in self.modules.items():
            for destination in module.destinations:
                if destination not in self.modules:
                    to_add.append(Module(destination, []))
        for m in to_add:
            self.modules[m.name] = m

        # initialize the conjunctions
        for module_name, module in self.modules.items():
            for destination in module.destinations:
                self.modules[destination].record_input(module_name)

        self.outputs = [0, 0]
        for i in range(0, 1000):
            self.process()
        return self.outputs[0] * self.outputs[1]

    def part2(self, input):
        self.modules = {}

        # parse input
        for line in input.rstrip().split("\n"):
            module, destinations = line.split(" -> ")
            m = Module(module, destinations.split(", "))
            self.modules[m.name] = m

        # find all untyped outputs
        to_add = []
        for module_name, module in self.modules.items():
            for destination in module.destinations:
                if destination not in self.modules:
                    to_add.append(Module(destination, []))
        for m in to_add:
            self.modules[m.name] = m

        # initialize the conjunctions
        for module_name, module in self.modules.items():
            for destination in module.destinations:
                self.modules[destination].record_input(module_name)

        xn = self.findCycle("th", "xn")
        qn = self.findCycle("th", "qn")
        xf = self.findCycle("th", "xf")
        zl = self.findCycle("th", "zl")
        return math.lcm(xn, qn, xf, zl)

    def process(self):
        queue = [("broadcaster", 0, "button")]
        while len(queue) > 0:
            module_name, signal_value, signal_from = queue.pop(0)
            self.outputs[signal_value] += 1
            module = self.modules[module_name]
            module.process(signal_value, signal_from, queue)

    def findCycle(self, last_conjunction, last_conjunction_input):
        for m in self.modules.values():
            m.reinit()
        queue = []
        n = 0
        while True:
            if len(queue) == 0:
                queue.append(("broadcaster", 0, "button"))
                n += 1
            module_name, signal_value, signal_from = queue.pop(0)
            module = self.modules[module_name]
            module.process(signal_value, signal_from, queue)

            m = self.modules[last_conjunction]
            if m.state[last_conjunction_input] == 1:
                return n


class TestDay20(unittest.TestCase):
    def testPart1(self):
        self.assertEqual(
            Day20().part1(
                """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""
            ),
            32000000,
        )
        self.assertEqual(
            Day20().part1(
                """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""
            ),
            11687500,
        )


print("day 20, part 1: ", Day20().part1(pathlib.Path("input").read_text()))
print("day 20, part 2: ", Day20().part2(pathlib.Path("input").read_text()))
unittest.main()
