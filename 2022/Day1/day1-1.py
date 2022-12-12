# store input
inputArray = []
with open('input.txt') as input:
    for line in input:
        line = line.strip('\n')
        line = line.strip('\t')
        inputArray.append(line)

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
