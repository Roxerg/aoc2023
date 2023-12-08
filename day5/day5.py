input_txt = open("input.txt", 'r').read()


lines = input_txt.split('\n')
seeds = [int(num) for num in lines.pop(0).split(': ')[1].split(' ')]


_seeds = []
while len(seeds) > 0:
    start, span = seeds.pop(0), seeds.pop(0)
    _seeds.append((start, start+span))

seeds = _seeds

print(seeds)


conversions = {}
curr_key = None

for line in lines:
    if len(line) == 0:
        continue
    elif line[0].isalpha():
        curr_key, _ = line.split(' ')
        conversions[curr_key] = []
    elif line[0].isnumeric():
        # dest_range, src_range, size
        conversions[curr_key].append([int(n) for n in line.split(' ')])



def part1():
    min_loc = 10000000000000000000000000000000000
    for v in seeds:
        for title, conversion in conversions.items():
            for c in conversion:
                if c[1] <= v <= c[1] + c[2]:
                    diff = v - c[1]
                    v = c[0] + diff 
                    break
        min_loc = min(min_loc, v)
    print(min_loc)


def convert(conversion_row, val):
    c = conversion_row
    v_lo, v_hi = val

    # print("C", conversion_row)
    # print("BEFORE", v_lo, v_hi)
    v_lo, v_hi = max(v_lo, c[1]), min(v_hi, c[1] + c[2])
    # print("FIT RANGE", v_lo, v_hi)
    diff_lo, diff_hi = v_lo - c[1], v_hi - c[1]
    # print("DIFF", diff_lo, diff_hi)
    v_lo, v_hi = max(c[0] + diff_lo, c[0]), min(c[0] + diff_hi, c[0] + c[2])
    # print("CONVERTED", v_lo, v_hi)

    return v_lo, v_hi

def get_unconverted(conversion_row, val):
    c = conversion_row
    v_lo, v_hi = val

    lower_bound = c[1]
    upper_bound = c[1] + c[2]

    res = []

    if (v_lo < lower_bound and v_hi < lower_bound) or (upper_bound < v_lo and upper_bound < v_hi):
        res.append((v_lo, v_hi))
    elif v_lo < lower_bound:
        res.append((v_lo, lower_bound-1))
    elif upper_bound < v_hi:
        res.append((upper_bound+1, v_hi))

    return res

def prune_unconverted(conversion_row, unconverted):
    c = conversion_row

    lower_bound = c[1]
    upper_bound = c[1] + c[2]

    to_remove = set()
    to_add = set()
    for u in unconverted:
        v_lo, v_hi = u

        if lower_bound < v_lo and v_hi < upper_bound:
            to_remove.add((v_lo, v_hi))
        elif v_lo < lower_bound and v_hi > lower_bound:
            to_remove.add((v_lo, v_hi))
            to_add.add((v_lo, lower_bound-1))
        elif upper_bound < v_hi and v_lo < upper_bound:
            to_remove.add((v_lo, v_hi))
            to_add.add((upper_bound+1, v_hi))
    
    # print("REMOVE", to_remove, c"BECAUSE", c)
    unconverted = unconverted | to_add
    unconverted = unconverted - to_remove

    
    return unconverted



def part2():

    leftovers = []
    items_at_curr_conversion = []
    items_for_next_conversion = []
    min_loc = 10000000000000000000000000000000000
    for (v_lo, v_hi) in seeds:
        items_for_next_conversion.append((v_lo, v_hi))
        for title, conversion in conversions.items():
            items_at_curr_conversion = items_for_next_conversion
            items_for_next_conversion = []
            for (v_lo, v_hi) in items_at_curr_conversion:
                matched_at_least_once = False
                unconverted = set()
                for c in conversion:
                    original = (v_lo, v_hi)
                    # print("FROM", (v_lo,v_hi))
                    if c[1] <= v_lo <= c[1] + c[2] or c[1] <= v_hi <= c[1] + c[2]:
                        (v_lo, v_hi) = convert(c, (v_lo, v_hi))
                        items_for_next_conversion.append((v_lo, v_hi))
                    # print("TO", (v_lo,v_hi))
                    uncov = get_unconverted(c, original)
                    # print("UNCOV ",uncov)
                    for u in uncov:
                        unconverted.add(u)
                    # print("conversion:", title, c, "unconverted:", unconverted, "next:", items_for_next_conversion)

                before_len = len(unconverted)
                after_len = 0
                prune_cnt = 0
                while before_len != after_len:
                    before_len = len(unconverted)
                    for c in conversion:
                        unconverted = prune_unconverted(c, unconverted)
                    after_len = len(unconverted)
                    prune_cnt += 1
                    if prune_cnt % 100 == 0:
                        print(prune_cnt)
                for u in unconverted:
                    if u not in items_for_next_conversion:
                        items_for_next_conversion.append(u)

                # print("after pruning | unconverted:", unconverted, "next:", items_for_next_conversion)

        min_loc = min(min_loc, min([x[0] for x in items_for_next_conversion]))
        items_for_next_conversion = []
    print(min_loc)


part2()

# 13 20
# 10 50 7


#           13 14 15 16 17 18 19 20
# 10 11 12 (13 14 15 16 17)
# 50 51 52  53 54 55 56 57

# 13 - 10 = 3
# 17 - 10 = 7


# 7 12
# 10 50 7

# 7 8 9  10 11 12          
#       (10 11 12) 13 14 15 16 17
#        50 51 52 53 54 55 56 
       
# 10 - 10 = 0
# 12 - 10 = 2


# In the above example, the lowest location number can be obtained from seed number 82, 
# which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, 
# humidity 46, and location 46. So, the lowest location number is 46.