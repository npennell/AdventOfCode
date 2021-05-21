inputArray = []

with open("input.txt") as fp:
    for line in fp:
        line = line.strip('\n')
        line = line.strip('\t')
        inputArray.append(line)

fp.close()

valid = 0

for value in inputArray:
    print(value)

    #parse inputArray line
    current_string = value
    step1 = current_string.split('-')
    step2 = step1[1]
    step3 = step2.split(' ')
    step4 = step3[1]
    step5 = step4.split(':')
    step6 = step3[2]


    #assign values
    int1 = int(step1[0])
    int2 = int(step3[0])
    character = step5[0]
    password = step6
    count = 0


    for i in password:
        if i == character:
            count = count + 1

    print(count)
    if (count >= int1) and (count <= int2):
        valid = valid + 1

print(valid)
