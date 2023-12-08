import re
from collections import deque

input = [l.split(": ")[1] for l in open('input.txt','r').read().split('\n')]

def part1():
    res = 0
    for nums in input:
        lucky, all = [set([int(n) for n in x.split(" ") if len(n) > 0]) for x in nums.replace('  ', ' ').split(" | ")]

        pow_val = len(lucky.intersection(all)) -1
        if pow_val >= 0:
            res += pow(2, pow_val)

    print(res)

# TODO: BAD, IMPROVE 
def part2():
    repeat = deque([1])
    counter = 0

    for nums in input:
        lucky, all = [set([int(n) for n in x.split(" ") if len(n) > 0]) for x in nums.replace('  ', ' ').split(" | ")]

        if len(repeat) == 0:
            repeat.append(1)

        curr_repeats = repeat.popleft()

        for _ in range(0, curr_repeats):

            counter += 1

            matches = len(lucky.intersection(all))

            if matches >= 0:
                new_entries = max(matches - len(repeat), 0)
                for idx in range(0, matches-new_entries):
                    repeat[idx] += 1
                if new_entries > 0:
                    for _ in range(0, new_entries):
                        repeat.append(2)

    print(counter)

part1()
part2()