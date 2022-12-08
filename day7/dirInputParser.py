import re 

class Directory:
    def __init__(self, name, files=[], directories=[]):
        self.name: str = name
        self.files: File[int] = files
        self.directories: Directory[str]= directories

class File:
    def __init__(self, name, size):
        self.name: str = name
        self.size: int = size

class FileSystemPointer:
    def __init__(self, currDirectory):
        self.currDirectory: str = currDirectory

# testFile = File("myFiles1", 33232)
# testDir3 = Directory( "myName3", testFile )
# testDir2 = Directory( "myName2", testFile,testDir3)
# testDir1 = Directory( "myName1", testFile, testDir2)
# testDir1_1 = Directory( "myName1", testFile, testDir2)
# testDir = Directory( "myName", testFile, {testDir1.name: testDir1, testDir1_1.name: testDir1_1})

# print(testDir.directories[testDir1.name].name)

file1 = open('input.txt', 'r')

lines = file1.readlines()
for line in lines:
    print(line)
    if(re.match("^\$ cd ([a-zA-Z0-9]{1,}|[\/])$", line)):
        currDir = Directory(line.split("$ cd ")[1])
    if(re.match("^dir", line)):
        currDir.directories.append({line.split("dir ")[1]: Directory(line.split("dir ")[1])})
    if(re.match("^[0-9]{1,}", line)):
        currDir.files.append(File(line.split(" ")[1], line.split(" ")[0]))

    if(re.match("^\$ cd ..", line)):
        currDir = currDir.directories[line.split("$ cd ")[1]]

print(fileSystem)     





        