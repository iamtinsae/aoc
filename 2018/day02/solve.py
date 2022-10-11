inp = open("input", mode="r").read().strip().split('\n')

def check_box_id(box_id: list|str):
    repeats_twice = False
    repeats_trice = False
    unique_letters = set(box_id)

    for l in unique_letters:
        count = box_id.count(l)
        if count == 2:
            repeats_twice = True

        if count == 3:
            repeats_trice = True

    return repeats_twice, repeats_trice

def calculate_checksum(inp: list[str]) -> int:
    twices = 0
    trices = 0
   
    for tw, tr in map(check_box_id, inp):
        twices += int(tw)
        trices += int(tr)

    return twices * trices

def get_matching_ids(id1, id2) -> tuple:
    difference = 0
    common_letters = []

    for a, b in zip(id1, id2):
        if a != b: 
            difference += 1
        else:
            common_letters.append(a)
    
    return difference, common_letters

def find_common_letters_btwn_box_ids(inp: list[str]) -> str | None:
    for idx, id1 in enumerate(inp):
        for id2 in inp[idx + 1:]:
            diff, common_letters = get_matching_ids(id1, id2)

            if diff == 1:
                return ''.join(common_letters)


if __name__ == '__main__':
    part_one_ans = calculate_checksum(inp)
    print ("Answer to part one: {}".format(part_one_ans))

    part_two_ans = find_common_letters_btwn_box_ids(inp)
    print ("Answer to part two: {}".format(part_two_ans))

