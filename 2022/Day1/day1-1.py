import utilFile
# store input
path = '../AdventOfCode/2022/Data/inputDay1.txt'
inputArray = utilFile.storeInput(path)

highestCalories = 0
currentCalories = 0

for input in inputArray:
    if input != '': # add to total if number
        currentCalories += int(input)
    else: # check if current total is highest
        if currentCalories > highestCalories:
            highestCalories = currentCalories
        currentCalories = 0 # reset counter

print(highestCalories)
