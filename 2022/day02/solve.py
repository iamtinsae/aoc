"""
Advent of Code 2022 - Day 2
"""

def part_one(inputs) -> int:
    opp_choices = list("ABC")
    fam_choices = list("XYZ")

    score = 0
    for opp, choice in map(lambda inp: inp.split(" "), inputs):
        opp_idx, fam_idx = [opp_choices.index(opp), fam_choices.index(choice)]
        score += fam_idx + 1

        difference = opp_idx - fam_idx
        if difference == 0:
            score += 3
        elif (abs(difference) == 1 and difference < 0) or (
            abs(difference) == 2 and difference > 0
        ):
            score += 6

    return score


def part_two(inputs) -> int:
    choices = list("ABC")

    score = 0
    for opp, sol in map(lambda inp: inp.split(" "), inputs):
        opp_idx = choices.index(opp)

        if sol == "X":
            score += choices.index(choices[opp_idx - 1]) + 1
        elif sol == "Y":
            score += (opp_idx + 1) + 3
        elif sol == "Z":
            score += choices.index(choices[opp_idx - 2]) + 1 + 6
    return score


with open("input", mode="r", encoding='ascii') as f:
    inputs = f.read().strip().split("\n")
    print(part_one(inputs))
    print(part_two(inputs))
