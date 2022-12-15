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
    
    # check if first fully contains second
    if firstElf[0] <= secondElf[0] and secondElf[1] <= firstElf[1]:
        # fully contained in first
        numOverlaps += 1
    # check if second fully contains first
    elif secondElf[0] <= firstElf[0] and firstElf[1] <= secondElf[1]: 
        numOverlaps += 1
        
print(numOverlaps)
    