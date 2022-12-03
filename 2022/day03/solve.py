import string
import textwrap

ascii_letters = string.ascii_lowercase + string.ascii_uppercase


def get_common_item_of_list(compartments):
    for chr in "".join(compartments):
        if all([compartment.count(chr) for compartment in compartments]):
            return chr


def get_common_item(compartment) -> str:
    p1, p2 = textwrap.wrap(compartment, len(compartment)//2)

    for chr in p2:
        if p1.count(chr):
            return chr


def get_priority_index(common_items):
    return sum([ascii_letters.index(s) + 1 for s in common_items])


def part_one(inputs) -> int:
    common_items = [get_common_item(compartment) for compartment in inputs]
    return get_priority_index(common_items)


def part_two(inputs) -> int:
    priorities_sum = []
    compartments = []

    for idx, value in enumerate(inputs):
        compartments.append(value)

        if (idx + 1) % 3 == 0:
            priorities_sum.append(
                get_priority_index(get_common_item_of_list(compartments))
            )
            compartments = []

    return sum(priorities_sum)
        

with open("input", mode="r") as f:
    inputs = f.read().strip().split("\n")

    print(part_one(inputs))
    print(part_two(inputs))
