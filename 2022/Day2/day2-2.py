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
    # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
    # 1 for Rock, 2 for Paper, and 3 for Scissors
    # 0 if you lost, 3 if the round was a draw, and 6 if you won
    if(player == 'X'): # Lose
        if(opponent == 'A'): # Rock
            score += 3 # Scissors
        elif(opponent == 'B'): # Paper
            score += 1 # Rock
        else: # Scissors
            score += 2 # Paper
    elif(player == 'Y'): # Draw
        score += 3
        if(opponent == 'A'): # Rock
            score += 1 # Rock
        elif(opponent == 'B'): # Paper
            score += 2 # Paper
        else: # Scissors
            score += 3 # Scissors
    else: # Win
        score += 6
        if(opponent == 'A'): # Rock
            score += 2 # Paper
        elif(opponent == 'B'): # Paper
            score += 3 # Scissors
        else: # Scissors
            score += 1 # Rock
    
    totalScore += score
        
print(totalScore)
    