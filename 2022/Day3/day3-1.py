import utilFile
import string
# store input
path = '../AdventOfCode/2022/Data/inputDay3.txt'
inputArray = utilFile.storeInput(path)

prioritySum = 0
priorityList = list(string.ascii_lowercase) + list(string.ascii_uppercase)

for line in inputArray:
    firstHalf = []  
    secondHalf = []
    lineLen = len(line)
    lineLenHalf = int(lineLen / 2)
    
    # for each line, divide letters in half
    firstHalf = line[0:lineLenHalf]
    secondHalf = line[lineLenHalf:lineLen]
    
    # find shared character from both lists
    commonChar = set(firstHalf).intersection(secondHalf)

    # find value for that letter & add to running total
    priority = priorityList.index(list(commonChar)[0]) + 1
    prioritySum += priority

print(prioritySum)