class HouseOfElves:
    def __init__(self) -> None:
        self.elves: Elf[int] = [Elf()]
    def addElf(self):
        self.elves.append(Elf())
    def findMostCalories(self):
        max =  self.elves[0].calories
        for i in range(len(self.elves)):
            if self.elves[i].calories > max:
                max = self.elves[i].calories
        return max  
    def findCaloriesOfTopThree(self):
        newArr = []
        for i in range(len(self.elves)):
            newArr.append(self.elves[i].calories)
        newArr.sort()
        return newArr[-1] + newArr[-2] + newArr[-3]
class Elf:
    def __init__(self) -> None:
        self.calories: int = 0
    def loadFood(self, newCalories):
        self.calories += newCalories

file1 = open('input.txt', 'r')
Lines = file1.readlines()

myHouseOfElves = HouseOfElves()
elfcount: int = 0
for line in Lines:
    if line.strip().isnumeric():
        myHouseOfElves.elves[elfcount].loadFood(int(line.strip()))
    else:
        elfcount += 1
        myHouseOfElves.addElf()

print(myHouseOfElves.findMostCalories())
print(myHouseOfElves.findCaloriesOfTopThree())

