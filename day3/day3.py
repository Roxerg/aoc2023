class GridParser:

    def __init__(self):
        self.reset_curr_num()
        self.num_map = {}
        self.sym_map = {} # reverse map

    def reset_curr_num(self):
        self.curr_num = ''
        self.curr_num_coords = []

    def finish_number(self):
        curr_int = int(self.curr_num)
        if curr_int not in self.num_map: self.num_map[curr_int] = []
        self.num_map[curr_int].append(self.curr_num_coords)
        self.reset_curr_num()

    def return_parsed(self):
        return num_map, sym_map

    def parse(self, input_txt):
        for y, input_line in enumerate(input_txt.split("\n")):
    
            for x, char in enumerate(input_line):
                if char.isdigit():
                    p.curr_num += char
                    p.curr_num_coords.append((x,y))
                else:
                    if len(p.curr_num) != 0: p.finish_number()
                    if char != '.': p.sym_map[(x,y)] = char
            if len(p.curr_num) != 0:
                p.finish_number()
        
        return self.num_map, self.sym_map

    def get_gear_locations(self):
        return [coords for (coords, sym) in self.sym_map.items() if sym=='*']


def part1(num_map, sym_map):

    res_sum = 0

    for (num, num_coord_sets) in num_map.items():
        for num_coord_set in num_coord_sets:
            num_done = False
            for num_coord in num_coord_set:
                for r in [(0,1),(1,0),(1,1),(1,-1),(-1,-1),(-1,1),(0,-1),(-1,0)]:
                    new_coord = (num_coord[0]+r[0], num_coord[1]+r[1])
                    if not new_coord in num_coord_set:
                        if new_coord in sym_map.keys():
                            res_sum += num
                            num_done = True
                            break
                if num_done: break

    return res_sum

def part2(num_map, sym_map, gear_locations):

    res_sum = 0

    for gear_coords in gear_locations:
        adjecent_nums = []
        for (num, num_coord_sets) in num_map.items():
            for num_coord_set in num_coord_sets:
                for r in [(0,1),(1,0),(1,1),(1,-1),(-1,-1),(-1,1),(0,-1),(-1,0)]:
                    new_coord = (gear_coords[0]+r[0], gear_coords[1]+r[1])
                    if new_coord in num_coord_set:
                        adjecent_nums.append(num)
                        break
        if len(adjecent_nums) == 2:
            res_sum += adjecent_nums[0] * adjecent_nums[1]

    return res_sum

input_txt = open("input.txt", 'r').read()

p = GridParser()
num_map, sym_map = p.parse(input_txt)
gear_locs = p.get_gear_locations()

print(part1(num_map, sym_map))
print(part2(num_map, sym_map, gear_locs))

