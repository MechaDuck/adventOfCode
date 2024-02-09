from enum import Enum

input_path = ""


class Cave:
    def __init__(self,cave: list[str]) -> None:
        val = self.get_horizontal_lines(cave)
        self.horizontal_lines: list[str] = val[0]
        self.vertical_lines: list[str] = val[1]
        pass

    def get_horizontal_lines(self, cave: list[str])-> tuple[list[str], list[str]]:
        tmp_hor = []
        tmp_ver = []
        for cave_line_horizontal in cave:
            tmp_hor.append(cave_line_horizontal.strip())
        for x in range(len(tmp_hor[0])):
            hor_str = ""
            for y in range(len(tmp_hor)):                 
                hor_str = hor_str + tmp_hor[y][x]
            tmp_ver.append(hor_str)
        return (tmp_hor, tmp_ver)
    def get_symmetry(self)-> int:
        return self.find_symmetry(self.horizontal_lines)*100 + self.find_symmetry(self.vertical_lines)
    def get_smudge_symmetry(self)->int:
        smudge_horizontals = self.find_smudge_symmetry(self.horizontal_lines)
        if  smudge_horizontals > 0:
            return smudge_horizontals * 100
        smudge_verticals = self.find_smudge_symmetry(self.vertical_lines)
        if smudge_verticals > 0:
            return smudge_verticals
        return self.get_symmetry()

        
    def find_symmetry(self, cave_structure: list[str])-> int:
        for index, line in enumerate(reversed(cave_structure)):
            if line == cave_structure[len(cave_structure)-2-index]:
                right = cave_structure[len(cave_structure)-index:]
                left = cave_structure[:len(cave_structure)-index-2][::-1]
                len_right = len(right)
                len_left = len(left)
                if len_right > len_left:
                    right = right[:len_left]
                else:
                    left = left[:len_right]
                if right == left:
                    return len(cave_structure)-index-1
        return 0
    def find_smudge_symmetry(self, cave_structure: list[str])-> int:
        for index, line in enumerate(reversed(cave_structure)):
            matches, miss_used = self.match_similarities_with_miss(cave_structure[len(cave_structure)-2-index], line, 1)
            if matches:
                right = cave_structure[len(cave_structure)-index:]
                left = cave_structure[:len(cave_structure)-index-2][::-1]
                len_right = len(right)
                len_left = len(left)
                if len_right > len_left:
                    right = right[:len_left]
                else:
                    left = left[:len_right]
                for right_line, left_line in zip(right,left):
                    matches, miss_used_next = self.match_similarities_with_miss(right_line, left_line, 1-miss_used)
                    miss_used += miss_used_next
                if matches and miss_used > 0:
                    return len(cave_structure)-index-1
        return 0
    
    def match_similarities_with_miss(self, string1: str, string2: str, count_miss:int) -> tuple[bool, int]:
        string_length = len(string1)
        count = 0
        for char1, char2 in zip(string1, string2):
            if char1 == char2:
                count += 1
        if string_length - count_miss == count:
            return (True, count_miss)
        if string_length == count:
            return (True, 0)
        return (False, 0)
        
        
                
                
            

def read_caves(file_path: str)-> list[Cave]:
    file = open(file_path, 'r')
    lines = file.readlines()
    cave_lines = []
    caves = []
    for line in lines:
        line = line.strip()
        if line == "":
            caves.append(Cave(cave_lines))
            cave_lines = []
            continue
        cave_lines.append(line)
    caves.append(Cave(cave_lines))
    return caves
        
            
                
            
if __name__ == "__main__":
    myCave = []
    # Part 1
    sum_notes = 0
    myCaves = read_caves(input_path)
    for cave in myCaves:
        sum_notes += cave.get_symmetry()
    print(sum_notes)
    
    sum_notes_fix_smudge = 0
    for cave in myCaves:
        sum_notes_fix_smudge += cave.get_smudge_symmetry()
    print(sum_notes_fix_smudge)
    