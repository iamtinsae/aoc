"""
Advent of Code 2022 - Day 5

            [C]         [N] [R]    
[J] [T]     [H]         [P] [L]    
[F] [S] [T] [B]         [M] [D]    
[C] [L] [J] [Z] [S]     [L] [B]    
[N] [Q] [G] [J] [J]     [F] [F] [R]
[D] [V] [B] [L] [B] [Q] [D] [M] [T]
[B] [Z] [Z] [T] [V] [S] [V] [S] [D]
[W] [P] [P] [D] [G] [P] [B] [P] [V]
"""

crates = [
    ["J", "F", "C", "N", "D", "B", "W"],
    ["T", "S", "L", "Q", "V", "Z", "P"],
    ["T", "J", "G", "B", "Z", "P"],
    ["C", "H", "B", "Z", "J", "L", "T", "D"],
    ["S", "J", "B", "V", "G"],
    ["Q", "S", "P"],
    ["N", "P", "M", "L", "F", "D", "V", "B"],
    ["R", "L", "D", "B", "F", "M", "S", "P"],
    ["R", "T", "D", "V"]
]

crates = list(map(list, map(reversed, crates)))


def part_one(inputs) -> str:
    crates_cpy = crates[:]

    for cmd in inputs:
        _, no_, _, from_, _, to_ = cmd.split()
        no_ = int(no_)
        from_ = int(from_)
        to_ = int(to_)

        from_items = crates_cpy[from_ - 1][len(crates_cpy[from_ - 1]) - no_:]
        crates_cpy[from_ - 1] = crates_cpy[from_ - 1][:len(crates_cpy[from_ - 1]) - no_]
        crates_cpy[to_ - 1] = crates_cpy[to_ - 1] + list(reversed(from_items))

    return ''.join(crates_cpy[x][-1] for x in range(len(crates_cpy)))


def part_two(inps) -> str:
    crates_cpy = crates[:]

    for cmd in inps:
        _, no_, _, from_, _, to_ = cmd.split()
        no_ = int(no_)
        from_ = int(from_)
        to_ = int(to_)

        from_items = crates_cpy[from_ - 1][len(crates_cpy[from_ - 1]) - no_:]
        crates_cpy[from_ - 1] = crates_cpy[from_ - 1][:len(crates_cpy[from_ - 1]) - no_]
        crates_cpy[to_ - 1] = crates_cpy[to_ - 1] + from_items

    return ''.join(crates_cpy[x][-1] for x in range(len(crates_cpy)))

with open("input", mode="r", encoding="ascii") as f:
    inputs = f.read().strip().split("\n")

    print(part_one(inputs))
    print(part_two(inputs))
