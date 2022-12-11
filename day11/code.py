import operator
import math
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
}

class Item:
    def __init__(self, worryLevel: int) -> None:
        self.worryLevel = worryLevel
    def setWorryLEvel(self, worryLevel):        
        self.worryLevel = worryLevel
class Monkey:
    def __init__(self, items, operationOperator: operator, operationValue, testDivisibleValue: int, monkeyThrowToIfTrue: int, monkeyThrowToIfFalse: int):
        self.items: Item[int] = items
        self.operationOperator = operationOperator
        self.operationValue = operationValue
        self.testDivisibleValue = testDivisibleValue
        self.monkeyThrowToIfTrue = monkeyThrowToIfTrue
        self.monkeyThrowToIfFalse = monkeyThrowToIfFalse
        self.inspectionCount = 0
        self.dontWorry = False

    def increaseInspectionCount(self):
        self.inspectionCount += 1
    def throwFirstItem(self):
        self.__inspectItem()
        item = self.items.pop(0)
        if item.worryLevel % self.testDivisibleValue == 0:
            return [self.monkeyThrowToIfTrue, item]
        else:
            return [self.monkeyThrowToIfFalse, item]
    def stopWorrying(self, commonDenominator: int):
        self.dontWorry = True
        self.commonDenominator = commonDenominator
    def __inspectItem(self):
        self.increaseInspectionCount()
        if self.operationValue == "old":
            self.items[0].worryLevel = ops[self.operationOperator](self.items[0].worryLevel, self.items[0].worryLevel)
        else:
            self.items[0].worryLevel = ops[self.operationOperator](self.items[0].worryLevel, self.operationValue)
        if self.dontWorry:
            if self.items[0].worryLevel > self.commonDenominator:
                self.items[0].worryLevel = int(self.items[0].worryLevel % self.commonDenominator)
        else:
            self.items[0].worryLevel = int(self.items[0].worryLevel / 3)
    def catchItem(self, item: Item):
        self.items.insert(0, item)
    def getInspectionCount(self):
        return self.inspectionCount
class MonkeyCircus:
    def __init__(self) -> None:
        self.monkeys: Monkey[int] = []
    def addNewMonkey(self, monkey):
        self.monkeys.append(monkey)
    def runMonkeyRound(self):
        for i in range(self.monkeys):
            while len(self.monkeys[i].items) != 0:
                thrownItem = self.monkeys[i].throwFirstItem()
                self.monkeys[thrownItem[0]].catchItem(thrownItem[0])
    def findCommonDenominator(self):
        denominators = []
        for i in range(len(self.monkeys)):
            denominators.append(self.monkeys[i].testDivisibleValue)
        return math.lcm(*denominators)

def gatherAllMonkey(myMonkeyCircus):
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        if "Monkey " in line:
            monkeyNumber = int(line.split("Monkey ")[1].split(":")[0])
        elif "Starting items: " in line:
            items = line.split("Starting items: ")[1].split(", ")
            items[-1] = items[-1].strip()
            for i in range(len(items)):
                items[i] = Item(int(items[i]))
        elif "Operation: new = old " in line:
            monkeyOperator = line.split("Operation: new = old ")[1][0]
            monkeyOperatorValue = line.split("Operation: new = old ")[1].split(" ")[1].strip()
            if monkeyOperatorValue != "old":
                monkeyOperatorValue = int(monkeyOperatorValue)
        elif "Test: divisible by " in line:    
            testDivisibleValue = int(line.split("Test: divisible by ")[1].strip())
        elif "If true: throw to monkey " in line:
            monkeyThrowToIfTrue = int(line.split("If true: throw to monkey ")[1].strip())
        elif "If false: throw to monkey " in line:
            monkeyThrowToIfFalse = int(line.split("If false: throw to monkey ")[1].strip())
            myMonkeyCircus.addNewMonkey(Monkey(items, monkeyOperator, monkeyOperatorValue, testDivisibleValue, monkeyThrowToIfTrue, monkeyThrowToIfFalse))
def runXRounds(roundCount, monkeyCircus):        

    for x in range(0, roundCount):
        for i in range(len(monkeyCircus.monkeys)):
            for p in range(len(monkeyCircus.monkeys[i].items)):
                throwElement = monkeyCircus.monkeys[i].throwFirstItem()
                monkeyCircus.monkeys[throwElement[0]].catchItem(throwElement[1])
    rankingInspectionCount = []
    for i in range(len(monkeyCircus.monkeys)):
        rankingInspectionCount.append(monkeyCircus.monkeys[i].getInspectionCount())

    rankingInspectionCount.sort() 
    monkeyBusiness = rankingInspectionCount[-1] * rankingInspectionCount[-2]
    print(monkeyBusiness)

## Part 1
myMonkeyCircus = MonkeyCircus()
gatherAllMonkey(myMonkeyCircus)
runXRounds(20, myMonkeyCircus)
## Part 2 
myMonkeyCircus.monkeys.clear()
gatherAllMonkey(myMonkeyCircus)
lcd = myMonkeyCircus.findCommonDenominator()

for i in range(len(myMonkeyCircus.monkeys)):
    myMonkeyCircus.monkeys[i].stopWorrying(lcd)
runXRounds(10000, myMonkeyCircus)

    




        

