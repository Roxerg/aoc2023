from functools import cmp_to_key, partial

hand_rankings = ['5', '4', 'house', '3', '2x2', '2', 'high']

def get_hand_rank(hand):
    seen = set()
    has_dupes = {}
    for c in hand:
        if c in seen:
            if c in has_dupes: has_dupes[c] += 1
            else: has_dupes[c] = 2
        seen.add(c)

    sets_cnt = len(has_dupes)
    set_sizes = set(has_dupes.values())

    if sets_cnt == 1:
        hand_rank = str(has_dupes[list(has_dupes)[0]])
    elif sets_cnt == 2:
        if 3 in set_sizes:
            hand_rank = 'house' if 2 in set_sizes else '3'
        elif 2 in set_sizes:
            hand_rank = '2x2' if len(set_sizes) == 1 else '2'
    else:
        hand_rank = hand_rankings[-1]

    return hand_rank

def compare(card_rankings, a, b):
    a,b = a[0], b[0]
    if a[0] < b[0]: return -1
    elif a[0] > b[0]: return 1
    else:
        for i in range(len(a[1])):
            a_rank = card_rankings.find(a[1][i])
            b_rank = card_rankings.find(b[1][i])
            if a_rank < b_rank: return -1
            elif a_rank > b_rank: return 1
    return 0


def solve(card_rankings, jonkler):
    bet_map = {}

    for line in input:
        hand, bet = line

        hand_rank = hand_rankings[-1]

        if jonkler and 'J' in hand:
            for c in card_rankings:
                _hand_rank = get_hand_rank(hand.replace('J', c))
                if hand_rankings.index(_hand_rank) < hand_rankings.index(hand_rank):
                    hand_rank = _hand_rank
        else: hand_rank = get_hand_rank(hand)

        hand_rank = hand_rankings.index(hand_rank)

        bet_map[(hand_rank, hand)] = bet

    cmp_fun = cmp_to_key(partial(compare, card_rankings))
    res = sum([int(v)*(i+1) for i, (_,v) in enumerate(sorted(bet_map.items(), key=cmp_fun, reverse=True))])
    print(res)

input = [line.split(' ') for line in open('input.txt').read().split('\n')]

solve('AKQJT98765432', False) # Part 1
solve('AKQT98765432J', True)  # Part 2