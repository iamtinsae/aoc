"""
Advent of Code 2022 - Day 6
"""


def part_one(inputs):
    for i in range(0, len(inputs)):
        if len(set(inputs[i : i + 4])) == 4:
            return i + 4


def part_two(inputs):
    for i in range(0, len(inputs)):
        if len(set(inputs[i : i + 14])) == 14:
            return i + 14


with open("input", mode="r") as f:
    inputs = f.read().strip()

    print(part_one(inputs))
    print(part_two(inputs))
