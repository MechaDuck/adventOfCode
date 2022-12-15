import re

class Directory:
    def __init__(self, prevDir=None) -> None:
        self.prevDir: Directory = prevDir
        self.directories: dict[str, Directory] = {}
        self.files: File[int] = []
    def calcSize(self):
        size = 0
        for file in self.files:
            size += file.size
        return size

class File:
    def __init__(self, size, name) -> None:
        self.size: int = size
        self.name = name

file1 = open('input.txt', 'r')
Lines = file1.readlines()

# Strips the newline character
rootDir = Directory("")
ref = rootDir

for line in Lines:
    if re.match("^\$ cd [\/]", line):
        ref = rootDir

    if re.match("^\$ cd [a-zA-Z0-9]", line):
        ref = ref.directories[line.split("$ cd ")[1]]

    if re.match("^\$ cd \.\.", line):
        ref = ref.prevDir

    if re.match("^dir", line):
        ref.directories[line.split("dir ")[1]] = Directory(ref)


    if re.match("^[0-9]{1,}", line):
        ref.files.append(File(line.split(" ")[0], line.split(" ")[1]))

