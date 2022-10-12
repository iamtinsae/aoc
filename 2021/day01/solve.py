inputs = open("input", mode="r").read().strip().split('\n')

"""
199
200
208
210
200
207
240
269
260
263

199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
"""

def depth_measurement_increase_count(inputs: list) -> int:
    inputs = list(map(int, inputs))
    increased = 0

    for i in range(0, len(inputs)-1):
        if inputs[i+1] > inputs[i]:
            increased += 1

    return increased


"""
199  A
200  A B
208  A B C
210    B C D
200  E   C D
207  E F   D
240  E F G
269    F G H
260      G H
263        H

A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)
"""

def depth_three_measurement_sliding_window(inputs: list) -> int:
    inputs = list(map(int, inputs))
    increased = 0
    last = None

    for i in range(0, len(inputs), 4):
        A = inputs[i: i+3]
        B = inputs[i+1: i+4]
        C = inputs[i+2: i+5]
        D = inputs[i+3: i+6]

        A = sum(map(lambda i: int(i), A))
        B = sum(map(lambda i: int(i), B))
        C = sum(map(lambda i: int(i), C))
        D = sum(map(lambda i: int(i), D))
        if last and A > last:
            increased += 1

        if B > A:
            increased += 1

        if C > B:
            increased += 1

        if D > C:
            increased += 1

        last = D

    return increased
if __name__ == '__main__':
    ans1 = depth_measurement_increase_count(inputs)
    print (f"Answer for problem 1 is: {ans1}")
    ans2 = depth_three_measurement_sliding_window(inputs)
    print (f"Answer for problem 2 is: {ans2}")


