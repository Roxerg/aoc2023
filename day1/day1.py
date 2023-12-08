import re

res_sum = 0

mapping = {
        'one' : '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

pattern = '|'.join(mapping.keys())+'|[0-9]'
pattern_rev = '|'.join([k[::-1] for k in mapping.keys()])+'|[0-9]'

with open('input.txt', 'r') as file:
    for line in file.read().split("\n"):

        a,b = re.search(pattern, line).group(0), re.search(pattern_rev, line[::-1]).group(0)[::-1]
        res_sum += int((mapping.get(a) or a) + (mapping.get(b) or b))

print(res_sum)