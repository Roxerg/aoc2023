import re 

res_sum = 0
mapping = {
    'one' : 'on1ne', 
    'two': 'tw2wo', 
    'three': 'thre3thre', 
    'four': 'fo4ur', 
    'five': 'fi5ve', 
    'six': 'si6ix', 
    'seven': 'sev7ven', 
    'eight': 'eigh8ght', 
    'nine': 'ni9ne'
}

with open("input.txt", 'r') as file:
    for line in file.read().split("\n"):
    
        _line = ''
        for c in line:
            _line += c
            for w in mapping.keys():
                _line = re.sub(w, mapping[w], _line)
        line = _line

        num = re.sub('[a-z]', '', line)
        num1, num2 = num[0], num[-1]
        _num = int(num1 + num2)
        print(num, num1,num2, _num)

        res_sum += _num

print(res_sum)
