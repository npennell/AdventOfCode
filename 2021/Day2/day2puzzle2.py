horizontal = 0
depth = 0
aim = 0
inputArray = []

with open('input.txt') as input:
    for line in input:
        line = line.strip('\n')
        line = line.strip('\t')
        inputArray.append(line)

for input in inputArray:
    split = input.split(" ")
    if split[0][0] == 'f':
        horizontal += int(split[1])
        depth += aim * int(split[1])
    elif split[0][0] == 'u':
        aim -= int(split[1])
    elif split[0][0] == 'd':
        aim += int(split[1])
    
total = depth * horizontal
print(total)
