import re
input_path = ""

def hashing(str:str) -> int:
    value = 0
    for char in str:
        value += ord(char)
        value = value * 17 % 256
    return value

def read_code(file_path: str)-> list[str]:
    code_list = []
    file = open(file_path, 'r')
    lines = file.readlines()
    for line in lines:
        code_list = line.strip().split(",")
    return code_list



class Box_Storage:
    def __init__(self) -> None:
        self.boxes: dict[int, dict[str, int]] = {}
        pass
    def get_box(self, label: str) -> int:
        return hashing(label)
    def store_lens(self, label: str, value: int):
        box_number = self.get_box(label)
        if box_number not in self.boxes:
            self.boxes[box_number] = {}
        self.boxes[box_number][label] = value
    def delete_lens(self,  label: str):
        box_number = self.get_box(label)
        if box_number in self.boxes:
            if label in self.boxes[box_number]:
                del self.boxes[box_number][label]
    def calc_focusing_power(self) -> int:
        focusing_power = 0
        for (box_number, lenses) in self.boxes.items():
            box_focusing_power = 0
            for index_lens, (_, value) in enumerate(lenses.items()):
                box_focusing_power = (box_number + 1) * (index_lens + 1) * int(value)
                focusing_power += box_focusing_power
        return focusing_power
            
            
    


if __name__ == "__main__":

    # Part 1
    sum = 0
    code_list = read_code(input_path) 
    for code in code_list:
        sum += hashing(code)
    print(sum)
    
    # part 2
    my_box_storage = Box_Storage()
    for code in code_list:
        if "=" in code:
            lens_label, lens_value = re.split('=', code)
            my_box_storage.store_lens(lens_label,lens_value)
        if "-" in code:
            lens_label, _ = re.split('-', code)
            my_box_storage.delete_lens(lens_label)
        
    print(my_box_storage.calc_focusing_power())
        

