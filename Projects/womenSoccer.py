# Description: program that generates wins and losses of BYU Women's Soccer during their soccer season
# Author: Thomas Cassler

# imports built in random function
import random

# Prompts for team name and number of games
teamName = input("Enter the team name:  ")
gameNumber = int(input("Enter the number of games that make up the soccer season: "))

# Starting values for team's wins and losses
teamWin = 0
teamLoss = 0

# For-loop for entering opponents and generating scores between team and opponent
for iCount in range(1, gameNumber +1, 1):
    opponentName = input("Enter the name of opponent for game " + str(iCount) + ": ")
    teamRand = 0
    opponentRand = 0
    while (teamRand == opponentRand):
        teamRand = random.randrange(0, 10)
        opponentRand = random.randrange(0, 10)
        if teamRand > opponentRand:
            teamWin += 1
            print("Your team won game ", iCount," by ", teamRand, "-", opponentRand)
        elif teamRand < opponentRand:
            teamLoss += 1
            print("Your team lost game ", iCount," by ", teamRand, "-", opponentRand)
        else:
            continue

# Displays team's record  
print(teamName, " ", teamWin, "-", teamLoss)

# Formula for percentage of team's wins in all games
teamPercentage = teamWin/iCount

# Display comments based on score.
if teamPercentage >= 0.75: 
    print("NCAA Women's Soccer Tournament")
elif teamPercentage < 0.75 and teamPercentage >= 0.50:
    print("You had a good season")
else:
    print("Your team needs to practice!")