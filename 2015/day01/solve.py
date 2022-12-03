def part_one(inputs) -> int:
    return sum(1 if c == '(' else -1 for c in inputs)


def part_two(inputs) -> int:
    floor = 0
    
    for idx, pos in enumerate(inputs):
        if pos == '(':
            floor += 1
        else:
            floor -= 1

        if floor == -1:
            return idx + 1


with open("input", mode="r") as f:
    inputs = f.read().strip()

    print(part_one(inputs))
    print(part_two(inputs))
