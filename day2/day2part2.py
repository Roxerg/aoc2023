

input_txt = """"""


def solve():
    start_time = time.time()

    cap_pows = []

    valid_ids = []

    for line in input_txt.split('\n'):
        game_idx, game_str = line.split(': ')

        _, game_idx = game_idx.split(' ')
        game_idx = int(game_idx)
        rounds = game_str.split('; ')

        curr_cap = {}
        for r in rounds:
            draws = r.split(', ')
            for draw in draws:
                cnt, colour = draw.split(' ')
                cnt = int(cnt)
                if colour not in curr_cap:
                    curr_cap[colour] = cnt
                else:
                    if curr_cap[colour] < cnt:
                        curr_cap[colour] = cnt
        pwr = reduce(lambda x, y: x*y, curr_cap.values())
        cap_pows.append(pwr)
    print(sum(cap_pows))
    return (time.time() - start_time)



import copy
from functools import reduce
import time
iterations = 1000
total = 0.0


for __i in range(0, iterations):
    total += solve()

print("--- %s splitsplitsplit avg seconds (%s iterations)---" % (total/iterations, iterations))
