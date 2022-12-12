# store input
inputArray = []
with open('../Data/inputDay1.txt') as input:
    for line in input:
        line = line.strip('\n')
        line = line.strip('\t')
        inputArray.append(line)

currentCalories = 0
topHighest = [0,0,0]

# go through each elf
for input in inputArray:
    if input != '':
        currentCalories += int(input)
    else:
        if currentCalories > topHighest[0]: # need to be added to top list
            # figure out which index to add to
            goalIndex = 0
            if currentCalories > topHighest[2]:
                goalIndex = 3
            elif currentCalories > topHighest[1]:
                goalIndex = 2
            else:
                goalIndex = 1
            topHighest.insert(goalIndex, currentCalories) # add in new total to array
            del topHighest[0] # remove first index item (lowest of 4)
            # highestCalories = currentCalories
        
        currentCalories = 0 # reset count

print(topHighest)
total = 0
# Add up total
for num in topHighest:
    total += num
print(total)
