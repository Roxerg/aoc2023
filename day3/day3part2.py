input_txt = open("input.txt", 'r').read()

num_map = {}
gear_locations = []


for y, input_line in enumerate(input_txt.split("\n")):
    curr_num = ''
    curr_num_coords = []
    for x, char in enumerate(input_line):
        if char.isdigit():
            curr_num += char
            curr_num_coords.append((x,y))
        else:
            if len(curr_num) != 0:
                curr_int = int(curr_num)
                if curr_int not in num_map: num_map[curr_int] = []
                num_map[curr_int].append(curr_num_coords)
                curr_num = ''
                curr_num_coords = []
            if char == '*':
                gear_locations.append((x,y))
    if len(curr_num) != 0:
        curr_int = int(curr_num)
        if curr_int not in num_map: num_map[curr_int] = []
        num_map[curr_int].append(curr_num_coords)
        curr_num = ''
        curr_num_coords = []

res_sum = 0
for gear_coords in gear_locations:
    adjecent_nums = []
    for (num, num_coord_sets) in num_map.items():
        for num_coord_set in num_coord_sets:
            for shift in [(0,1),(1,0),(1,1),(1,-1),(-1,-1),(-1,1),(0,-1),(-1,0)]:
                new_coord = (gear_coords[0]+shift[0], gear_coords[1]+shift[1])
                if new_coord in num_coord_set:
                    adjecent_nums.append(num)
                    break
    if len(adjecent_nums) == 2:
        res_sum += adjecent_nums[0] * adjecent_nums[1]
        

print(res_sum)