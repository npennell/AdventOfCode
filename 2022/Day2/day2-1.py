import utilFile
# store input
path = '../AdventOfCode/2022/Data/inputDay2.txt'
inputArray = utilFile.storeInput(path)
totalScore = 0

for line in inputArray:
    score = 0
    opponent = line[0]
    player = line[2]
    # A for Rock, B for Paper, and C for Scissors
    # 0 if you lost, 3 if the round was a draw, and 6 if you won
    if(player == 'X'): # Rock
        score += 1
        if(opponent == 'A'):
            score += 3
        elif(opponent == 'C'):
            score += 6
    elif(player == 'Y'): # Paper
        score += 2
        if(opponent == 'B'):
            score +=3
        elif(opponent == 'A'):
            score +=6
    else: # Scissors
        score += 3
        if(opponent == 'C'):
            score += 3
        elif(opponent == 'B'):
            score +=6
    
    totalScore += score
        
print(totalScore)
    