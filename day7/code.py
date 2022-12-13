import re 

class Directory:
    def __init__(self, name, prevDirectory):
        self.name: str = name
        self.files: File[int] = []
        self.directories = {}
        self.prevDirectory = prevDirectory

class File:
    def __init__(self, name, size):
        self.name: str = name
        self.size: int = size

class FileSystemPointer:
    def __init__(self, currDirectory):
        self.currDirectory: str = currDirectory

file1 = open('example_input.txt', 'r')
fileSystem = Directory("/", "/")
lines = file1.readlines()
for line in lines:
    print(line)
    if(re.match("^\$ cd ([a-zA-Z0-9]{1,}|[\/])$", line)):
        if line.strip() == "$ cd /":
        else: 
    if(re.match("^dir", line)):
    if(re.match("^[0-9]{1,}", line)):

    if(re.match("^\$ cd ..", line)):


print(fileSystem)     





        