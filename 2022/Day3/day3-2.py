import utilFile
import string
# store input
path = '../AdventOfCode/2022/Data/inputDay3.txt'
inputArray = utilFile.storeInput(path)

prioritySum = 0 # running total
priorityList = list(string.ascii_lowercase) + list(string.ascii_uppercase) # list of alphabet in priority order
i = 0 # loop variable

while i < len(inputArray):
    # get every 3 lines in group
    firstLine = inputArray[i]
    secondLine = inputArray[i+1]
    thirdLine = inputArray[i+2]
    
    # find common between all 3 lines
    commonSet = set(firstLine).intersection(secondLine)
    commonSet = set(commonSet).intersection(thirdLine)
    
    # find priority value and add to sum
    priority = priorityList.index(list(commonSet)[0]) + 1
    prioritySum += priority
    
    i += 3

print(prioritySum)