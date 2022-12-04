def part_one(inputs):
    t = 0
    for line in inputs:
        f1, f2 = line.split(",")

        f1 = list(map(int, f1.split("-")))
        f2 = list(map(int, f2.split("-")))

        f1x, f1y = f1
        f2x, f2y = f2

        if (f1x <= f2x and f1y >= f2y) or (f2x <= f1x and f2y >= f1y):
            t += 1
    return t


def part_two(inputs):
    overlaps = 0
    for line in inputs:
        f1, f2 = line.split(",")

        f1 = list(map(int, f1.split("-")))
        f2 = list(map(int, f2.split("-")))

        x = max(f1[0], f2[0])
        y = min(f1[1], f2[1])
        if x <= y:
            overlaps += 1

    return overlaps


with open("input", mode="r") as f:
    inputs = f.read().strip().split("\n")

    print(part_one(inputs))
    print(part_two(inputs))
