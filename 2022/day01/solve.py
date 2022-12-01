inputs = open("input", mode="r").read().split("\n")


def get_elf_with_most_calories(inputs) -> int:
    most_calorie = 0

    elf_calories = 0
    for calorie in inputs:
        if calorie == '':
            if elf_calories > most_calorie:
                most_calorie = elf_calories
            elf_calories = 0
        else:
            elf_calories += int(calorie)

    return most_calorie


def get_top_three_elfs_with_most_calories(inputs) -> int:
    most_calories = []

    elf_calories = 0
    for calorie in inputs:
        if calorie == '':
            most_calories.append(elf_calories)
            elf_calories = 0
        else:
            elf_calories += int(calorie)

    return sum(sorted(most_calories, reverse=True)[:3])


print(get_elf_with_most_calories(inputs))
print(get_top_three_elfs_with_most_calories(inputs))
