inputNumArray = []

#store info from file
fp = open("inputNums.txt", "r")

with open("inputNums.txt") as input:
    for line in input:
        line = line.strip('\n')
        line = line.strip('\t')
        line = int(line)
        inputNumArray.append(line)

fp.close()


#work with input
icount = 0
jcount = 1
answer = 0
#i is the starting value
for i in inputNumArray:
    icount = icount + 1
    print("icount", icount)
    for j in range(icount, len(inputNumArray)-1):
        jcount = jcount + 1
    
        if jcount == 199:
            jcount = icount + 1
        print("jcount", jcount)
        for k in range(jcount, len(inputNumArray)):

            total = i + inputNumArray[j] + inputNumArray[k]
            print (total)
            if total == 2020:
                answer = i * inputNumArray[j] * inputNumArray[k]


print('answer = ', answer)
