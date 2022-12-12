inputArray = []

with open('input.txt') as input:
    for line in input:
        line = line.strip('\n')
        line = line.strip('\t')
        inputArray.append(line)

input = {}
for i in range(0, 12):
    input[i] = {
        0: 0,
        1: 0,
    }

for line in inputArray:
    for i in range(0, 12):
        if line[i] == '0':
            input[i][0] += 1
        else:
            input[i][1] += 1

gamma = ""
epsilon = ""

for i in input:
    input0 = input[i][0]
    input1 = input[i][1]
    print('input0 =', input0, ' input1 =', input1)
    if input0 > input1:
        gamma = gamma + "0"
        epsilon = epsilon + "1"
    else:
        gamma = gamma + "1"
        epsilon = epsilon + "0"
        # gamma.append(str(input[i][1]))
        # epsilon.append(str(input[i][0]))

print(gamma, epsilon)
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
result = gamma * epsilon

print(result)