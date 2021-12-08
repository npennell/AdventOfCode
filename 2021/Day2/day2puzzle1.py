horizontal = 0
depth = 0
inputArray = []

with open('input.txt') as input:
    for line in input:
        line = line.strip('\n')
        line = line.strip('\t')
        inputArray.append(line)

line1 = inputArray[0]
print(line1)
split = line1.split(" ")
print(split[0][0])
for input in inputArray:
    split = input.split(" ")
    if split[0][0] == 'f':
        horizontal += int(split[1])
    elif split[0][0] == 'u':
        depth -= int(split[1])
    elif split[0][0] == 'd':
        depth += int(split[1])

total = depth * horizontal
print(total)
