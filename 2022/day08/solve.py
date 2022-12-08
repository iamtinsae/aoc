"""
Advent of Code 2022 - Day 8
"""
from functools import reduce


def part_one(inputs):
    """
    Part One Solution
    """
    visible_trees = 0
    for i, row in enumerate(inputs):
        for j, tree in enumerate(map(int, row)):
            norths = [inputs[x][j] for x in range(i)]
            souths = [inputs[x][j] for x in range(i + 1, len(inputs))]
            wests = [row[x] for x in range(j)]
            easts = [row[x] for x in range(j + 1, len(row))]

            if any(len(surrounding) == 0 for surrounding in (norths, souths, wests, easts)):
                visible_trees += 1
                continue
            if any([
                all(tree > int(x) for x in norths),
                all(tree > int(x) for x in souths),
                all(tree > int(x) for x in wests),
                all(tree > int(x) for x in easts)
            ]):
                visible_trees += 1
                continue

    return visible_trees


def get_scenic_score(tree, trees):
    score = 0

    for tr in trees:
        if int(tr) < tree:
            score += 1
        else:
            score += 1
            break

    return score


def part_two(inputs):
    """
    Part Two Solution
    """
    scenic_scores = []
    for i, row in enumerate(inputs):
        for j, tree in enumerate(map(int, row)):
            norths = [inputs[x][j] for x in range(i)]
            souths = [inputs[x][j] for x in range(i + 1, len(inputs))]
            wests = [row[x] for x in range(j)]
            easts = [row[x] for x in range(j + 1, len(row))]

            if any(
                len(surrounding) == 0 for surrounding in (norths, souths, wests, easts)
            ):
                continue
            sums = reduce( lambda a, b: a*b,
                [scenic_score for scenic_score in
                map(
                    lambda trees: get_scenic_score(tree, trees),
                    [norths[::-1], souths, wests[::-1], easts]
                )]
            )
            scenic_scores.append(sums)

    return list(sorted(scenic_scores))[-1]


with open("input", mode="r", encoding="utf-8") as f:
    inps = f.read().strip().splitlines()

    print("Part One:", part_one(inps))
    print("Part Two:", part_two(inps))
