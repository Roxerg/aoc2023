import re

input = [l.split(': ')[1] for l in open('input.txt', 'r').read().split('\n')]

def wins(distance, time, held):
    return distance < (time-held)*held

def part1():
    res = 1

    times, distances = [re.findall('[0-9]+', l) for l in input]
    times, distances = [int(n) for n in times], [int(n) for n in distances]

    for time, distance in zip(times,distances):
        ways = 0
        for held in range(1, time):
            if wins(distance, time, held): ways += 1
        res *= ways

    print(res)

def part2():

    time, distance = [int(''.join(n)) for n in [re.findall('[0-9]+', l) for l in input]]

    left, right = time, int(time/2)

    something_ran = True
    increment = right
    while something_ran:
        something_ran = False
        while wins(distance, time, left-increment):
            something_ran = True
            left -= increment
        while wins(distance, time, right+increment):
            something_ran = True
            right += increment
        if not something_ran and increment != 1:
            something_ran = True
            increment = max(int(increment / 2), 1)

    ways = right-left+1

    print(ways)

part1()
part2()