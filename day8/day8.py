

import math
import functools

input = open('input.txt', 'r').read().split("\n")

instructions = [0 if c=='L' else 1 for c in input[0]]
input = input[2:]

def while_check(PART_TWO, curr_nodes, idx):
    if PART_TWO:
        return curr_nodes[idx][-1] != 'Z'
    else:
        return curr_nodes[idx] != 'ZZZ'

def solve(PART_TWO):
    tree = {}
    for line in input:
        root, paths = line.split(' = ')
        paths = paths.split(', ')
        left, right = paths[0][1:], paths[1][:-1]
        tree[root] = (left, right)

    curr_nodes = [n for n in tree.keys() if 'A' == n[-1]] if PART_TWO else ['AAA']
    move_idx = 0
    steps = {}
    for idx, curr_node in enumerate(curr_nodes):
        steps[idx] = 0
        while while_check(PART_TWO, curr_nodes, idx):
            move = instructions[move_idx]
            curr_node = tree[curr_node][move]
            curr_nodes[idx] = curr_node
            move_idx = 0 if move_idx+1 > len(instructions)-1 else move_idx+1
            steps[idx] += 1


    if not PART_TWO:
        res = list(steps.values())[0]
    else:
        res = functools.reduce(lambda a, b: math.lcm(a,b), list(steps.values()))
    print(res)

solve(False)
solve(True)