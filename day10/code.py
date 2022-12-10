class CPURegister:
    def __init__(self) -> None:
        self.currX: int = 1


def drawSprite(spritePos, tickCount: int):
    if tickCount % 40 == 0 and tickCount != 0:
        print("\n", end="")
    if abs(spritePos - (tickCount % 40)) == 1  or abs(spritePos - (tickCount % 40)) == 0:
        print ("#", end="")
    else:
        print(".", end="")

    return

def tick(instructionStack, CPUReg: CPURegister):
    currInstruction = instructionStack[0]
    if type(currInstruction) == int:
        CPUReg.currX = CPUReg.currX + int(currInstruction)
    instructionStack.pop(0)
    return

instructionsStack = []
file1 = open('input.txt', 'r')
Lines = file1.readlines()
for line in Lines:
    instruction = line.split(" ")[0].strip()
    if instruction == "noop":
        instructionsStack.append(instruction)
    else:
        value = int(line.split(" ")[1].strip())
        instructionsStack.append(instruction)
        instructionsStack.append(value)
myCPUReg = CPURegister()

ticks = 0
signalStrength = 0
while(len(instructionsStack) != 0):
    drawSprite(myCPUReg.currX, ticks)
    ticks += 1

    if ticks == 20 or ticks == 60 or ticks == 100 or ticks == 140 or ticks == 180 or ticks == 220:
        signalStrength += myCPUReg.currX * ticks
    tick(instructionsStack, myCPUReg)

print("\n")
print(signalStrength)

