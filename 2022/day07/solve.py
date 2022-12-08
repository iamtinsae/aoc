"""
Advent of Code 2022 - Day 7
"""
from collections import defaultdict


def part_one(inputs):
    """
    Part One Solution
    """
    dirs = []
    dirs_sizes = defaultdict(int)
    inputs_len = len(inputs)

    i = 0
    while i < inputs_len:
        line = inputs[i]
        cmd, *args = line.split(" ")[1:]
        arg = args[0] if len(args) else None

        if cmd == "cd":
            if arg == "..":
                dirs.pop()
            else:
                dirs.append(arg)
        path = "/".join(dirs)
        if cmd == "ls":
            dir_items = []

            while True:
                idx = i + 1
                if idx >= inputs_len or inputs[idx].startswith("$"):
                    break

                dir_items.append(inputs[idx])
                i += 1

            for item in dir_items:
                if item.startswith("dir"):
                    continue
                size, _ = item.split(" ")
                dirs_sizes[path] += int(size)
                for j in range(len(dirs)):
                    dirs_sizes["/".join(dirs[:j])] += int(size)
        i += 1

    return sum(v for v in dirs_sizes.values() if v <= 100000)


def part_two(inputs):
    """
    Part Two Solution
    """
    dirs = []
    dirs_sizes = defaultdict(int)
    inputs_len = len(inputs)

    i = 0
    while i < inputs_len:
        line = inputs[i]
        cmd, *args = line.split(" ")[1:]
        arg = args[0] if len(args) else None

        if cmd == "cd":
            if arg == "..":
                dirs.pop()
            else:
                dirs.append(arg)
        path = "/".join(dirs)
        if cmd == "ls":
            dir_items = []

            while True:
                idx = i + 1
                if idx >= inputs_len or inputs[idx].startswith("$"):
                    break

                dir_items.append(inputs[idx])
                i += 1

            for item in dir_items:
                if item.startswith("dir"):
                    continue
                size, _ = item.split(" ")
                dirs_sizes[path] += int(size)
                for j in range(len(dirs)):
                    dirs_sizes["/".join(dirs[:j])] += int(size)
        i += 1

    disk_size = 70000000
    root_size = dirs_sizes["/"]
    required_free_space = 30000000 - (disk_size - root_size)

    for dir_size in sorted(v for v in dirs_sizes.values()):
        if dir_size >= required_free_space:
            return dir_size


with open("input", mode="r", encoding="utf-8") as f:
    inps = f.read().strip().splitlines()

    print("Part One:", part_one(inps))
    print("Part Two:", part_two(inps))
