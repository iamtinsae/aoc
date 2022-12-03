from collections import defaultdict
import textwrap


def part_one(inputs) -> int:
    x, y = 0, 0
    d = defaultdict(int)

    for i in inputs:
        if i == '>':
            x += 1
        elif i == '<':
            x += -1
        elif i == '^':
            y += 1
        elif i == 'v':
            y += -1

        d[(x, y)] += 1

    return 1 + len(d.keys())


def part_two(inputs) -> int:
    cmds = textwrap.wrap(inputs, 2)
    d = defaultdict(int)
    sx, sy = 0, 0
    rx, ry = 0, 0

    for cmd in cmds:
        santa, robo_santa = list(cmd)

        if santa == '>':
            sx += 1
        elif santa == '<':
            sx -= 1
        elif santa == '^':
            sy += 1
        elif santa == 'v':
            sy -= 1

        if robo_santa == '>':
            rx += 1
        elif robo_santa == '<':
            rx -= 1
        elif robo_santa == '^':
            ry += 1
        elif robo_santa == 'v':
            ry -= 1

        d[(sx, sy)] += 1
        d[(rx, ry)] += 1

    return len(d.keys())


with open("input", mode="r") as f:
    inputs = f.read().strip()

    print(part_one(inputs))
    print(part_two(inputs))
