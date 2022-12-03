def part_one(inputs) -> int:
    total_square_feet = 0
    for box in inputs:
        l, w, h = map(int, box.split("x"))
        a, b = sorted([l, w, h])[:2]
        total_square_feet += (2*l*w + 2*w*h + 2*h*l) + (a * b)

    return total_square_feet


def part_two(inputs) -> int:
    total_feet = 0
    for box in inputs:
        l, w, h = map(int, box.split("x"))
        a, b = sorted([l, w, h])[:2]

        total_feet += (2*a + 2*b) + (l * w * h)

    return total_feet


with open("input", mode="r") as f:
    inputs = f.read().strip().split("\n")
    print(part_one(inputs))
    print(part_two(inputs))
