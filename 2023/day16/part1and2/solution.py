from enum import Enum

input_path = ""

class Light_Dir(Enum):
    RIGHT = "r"
    LEFT = "l"
    DOWN = "d"
    UP = "u"

class Light_Passed_Dir(Enum):
    LR = "right"
    RL = "left"
    UD = "down"
    DU = "up"

class Cave_Element(Enum):
    PIPE = "|"
    FRONTSLASH = "/"
    BACKSLASH = "\\"
    MINUS = "-"
    DOT = "."
    LIGHT = "#"
class Cave_Element_Storage:
    def __init__(self, char:str)-> None:
        self.element: Cave_Element = self.match_char_to_enum(char)
        self.light_passed: bool = False
        self.light_passed_dir: [Light_Passed_Dir] = []
        return 
    def match_char_to_enum(self, char: str) -> Cave_Element:
        try:
            return Cave_Element(char)
        except ValueError:
            raise ValueError(f"Character '{char}' does not match any Cave_Element")
    def __str__(self) -> str:
        return self.element.value

class Cave:
    def __init__(self, file_path: str) -> None:
        self.build_cave(file_path)
        return
    def count_light_passages(self) -> int:
        count = 0
        for row in self.cave_matrix:
            for element in row:
                if element.light_passed is True:
                    count = count + 1
        return count
    def build_cave(self, file_path: str)-> None:
        self.cave_matrix: list[list[Cave_Element_Storage]] = []
        file = open(file_path, 'r')
        lines = file.readlines()
        for line in lines:
            tmp = []
            for char in line.strip():
                tmp.append(Cave_Element_Storage(char))
            self.cave_matrix.append(tmp)
    def print_matrix(self)-> None:
        for row in self.cave_matrix:
            for element in row:
                print(element, end=" ")
            print()
    def simulate_next_light(self, coords: [(int, int, Light_Dir)]) -> [(int, int, Light_Dir)]:
        next_coords = []
        for coord in coords:
            if coord[1] >= len(self.cave_matrix) or coord[1] < 0:
                continue
            if coord[0] >= len(self.cave_matrix[0]) or coord[0] < 0:
                continue
                
            offset_to_next = self.get_next_coordinates(coord[2], self.cave_matrix[coord[1]][coord[0]])
            for offset in offset_to_next:
                next_x = offset[0] + coord[0]
                next_y = offset[1] + coord[1]
                next_dir = offset[2]
                next_coords.append((next_x, next_y, next_dir))
        return next_coords
             
    def get_cave_dimensions(self)-> (int, int):
        return (len(self.cave_matrix), len(self.cave_matrix[0]))

    def get_next_coordinates(self, dir: Light_Dir, collision: Cave_Element_Storage)-> [(int,int, Light_Dir)]:
        collision.light_passed = True

        if collision.element is Cave_Element.PIPE:
            if dir is Light_Dir.UP:
                return [(0, -1, Light_Dir.UP)]
            if dir is Light_Dir.DOWN:
                return [(0,1,Light_Dir.DOWN)]
            return [(0, 1, Light_Dir.DOWN),(0, -1, Light_Dir.UP)]
        if collision.element is Cave_Element.MINUS:
            if dir is Light_Dir.RIGHT:
                return [(1, 0, Light_Dir.RIGHT)]
            if dir is Light_Dir.LEFT:
                return [(-1, 0, Light_Dir.LEFT)]
            return [(-1, 0, Light_Dir.LEFT),(1, 0, Light_Dir.RIGHT)]
        if collision.element is Cave_Element.FRONTSLASH:
            if dir is Light_Dir.RIGHT:
                return [(0, -1, Light_Dir.UP)]
            if dir is Light_Dir.LEFT:
                return [(0, 1, Light_Dir.DOWN)]
            if dir is Light_Dir.UP:
                return [(1, 0, Light_Dir.RIGHT)]
            if dir is Light_Dir.DOWN:
                return [(-1, 0, Light_Dir.LEFT)]
        if collision.element is Cave_Element.BACKSLASH:
            if dir is Light_Dir.RIGHT:
                return [(0, 1, Light_Dir.DOWN)]
            if dir is Light_Dir.LEFT:
                return [(0, -1, Light_Dir.UP)]
            if dir is Light_Dir.UP:
                return [(-1, 0, Light_Dir.LEFT)]
            if dir is Light_Dir.DOWN:
                return [(1, 0, Light_Dir.RIGHT)]
        if collision.element is Cave_Element.DOT or collision.element is Cave_Element.LIGHT:
            if dir in collision.light_passed_dir:
                return []
            next_coord = []      
            if dir is Light_Dir.RIGHT:
                next_coord=  [(1, 0, Light_Dir.RIGHT)]
            if dir is Light_Dir.LEFT:
                next_coord= [(-1, 0, Light_Dir.LEFT)]
            if dir is Light_Dir.UP:
                next_coord= [(0, -1, Light_Dir.UP)]
            if dir is Light_Dir.DOWN:
                next_coord= [(0,1,Light_Dir.DOWN)]
            collision.light_passed_dir.append(dir)
            collision.element = Cave_Element.LIGHT
            return next_coord
        return []
        







if __name__ == "__main__":
    # Part 1
    myCave = Cave(input_path)
    myCave.print_matrix()
    
    coord = [(0,0,Light_Dir.RIGHT)]
    while(True):
        coord =  myCave.simulate_next_light(coord)
        if len(coord) <= 0:
            break
    myCave.print_matrix()
    print(myCave.count_light_passages())
    print("\n")
        
    # Part 2
    #Create Start coordinates
    dimension = myCave.get_cave_dimensions()
    #Top-Down
    start_coords = []
    for x in range(dimension[0]):
        start_coords.append([(x,0,Light_Dir.DOWN)])
    for y in range(dimension[1]):
        start_coords.append([(0,y,Light_Dir.RIGHT)])
    for x in range(dimension[0]):
        start_coords.append([(x,dimension[1]-1,Light_Dir.UP)])
    for y in range(dimension[1]):
        start_coords.append([(dimension[0]-1,y,Light_Dir.LEFT)])
    
    energy_level = []
    for coord in start_coords:
        myCave = Cave(input_path)
        while(True):
            coord =  myCave.simulate_next_light(coord)
            if len(coord) <= 0:
                break
        energy_level.append(myCave.count_light_passages())
    print(max(energy_level))
        
    