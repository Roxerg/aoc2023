

input_txt = """"""

# game_id = re.match('^Game ([0-9]+):', line).group(1)


from functools import reduce
import re
import time


def solve():
    start_time = time.time()

    total_pwr = 0
    for line in input_txt.split('\n'):
        colour_max = {'green': 0, 'blue': 0, 'red': 0}
        draws = re.findall('([0-9]+)\ (green|blue|red)', line)

        for (cnt, clr) in draws:
            cnt = int(cnt)
            if colour_max[clr] < cnt: colour_max[clr] = cnt

        total_pwr += reduce(lambda x, y: x*y, colour_max.values())

    print(total_pwr)
    return (time.time() - start_time)

iterations = 1000
total = 0.0


for __i in range(0, iterations):
    total += solve()

print("--- %s regex avg seconds (%s iterations)---" % (total/iterations, iterations))

# 0.0011014151573181153 splitsplitsplit avg seconds (1000 iterations)
# 0.001314058303833008 regex avg seconds (1000 iterations)