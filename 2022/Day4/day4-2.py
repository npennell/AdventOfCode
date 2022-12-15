import utilFile

# store input
path = '../AdventOfCode/2022/Data/inputDay4.txt'
inputArray = utilFile.storeInput(path)

numOverlaps = 0

for line in inputArray:
    # parse line into each elf
    lineSplit = line.split(',')
    
    firstElfSplit = lineSplit[0].split('-')
    firstElf = [int(firstElfSplit[0]), int(firstElfSplit[1])]
    secondElfSplit = lineSplit[1].split('-')
    secondElf = [int(secondElfSplit[0]), int(secondElfSplit[1])]
    
    # check if any overlap
    # second overlaps with first
    if firstElf[0] <= secondElf[0] and secondElf[0] <= firstElf[1] or firstElf[0] <= secondElf[1] and secondElf[1] <= firstElf[1]:
        numOverlaps += 1
    # first overlaps with second
    elif secondElf[0] <= firstElf[0] and firstElf[0] <= secondElf[1] or secondElf[0] <= firstElf[1] and firstElf[1] <= secondElf[1]:
        numOverlaps += 1
        
print(numOverlaps)
    