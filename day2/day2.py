

input_txt = open('input.txt', 'r').read()

import copy

cap = {
    'red' :  12,
    'green' : 13,
    'blue' : 14
}

valid_ids = []

for line in input_txt.split('\n'):
    game_idx, game_str = line.split(': ')

    _, game_idx = game_idx.split(' ')
    game_idx = int(game_idx)
    rounds = game_str.split('; ')

    all_valid = True
    for r in rounds:
        curr_cap = copy.deepcopy(cap)
        draws = r.split(', ')
        for draw in draws:
            cnt, colour = draw.split(' ')
            cnt = int(cnt)
            curr_cap[colour] -= cnt

        all_valid = all_valid and all([curr_cap[c] > -1 for c in curr_cap.keys()])

        if not all_valid:
            break

    if all_valid:
        valid_ids.append(game_idx)

print(sum(valid_ids))
