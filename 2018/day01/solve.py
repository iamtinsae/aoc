from functools import reduce

inp = list(map(int, open("input", mode="r").read().strip().split('\n')))

def get_resulting_frequence(inp: list[int]):
    return reduce(lambda a, b: a+b, inp)

def get_first_reached_twice_freq(inp: list[int]):
    seen_freqs = []
    resulting_freq = 0
    idx = 0

    while True:
        idx = idx % len(inp)
        resulting_freq += inp[idx]
        if resulting_freq in seen_freqs:
            break
        seen_freqs.append(resulting_freq)
        idx += 1

    return resulting_freq

if __name__ == '__main__':
    part_one_ans = get_resulting_frequence(inp)
    print ("Answer to part one: {}".format(part_one_ans))

    part_two_ans = get_first_reached_twice_freq(inp)
    print ("Answer to part two: {}".format(part_two_ans))
