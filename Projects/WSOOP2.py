# Description: program that generates wins and losses of BYU Women's Soccer during their soccer season using class. 
# Author: Thomas Cassler

# imports built in random function
import random

# Class
class soccerTeam:
    # Constructor
    def __init__(self, tName, wins, losses, scored, allowed):
        # Instance Attributes
        self.teamName = tName
        self.numWins = wins
        self.numLosses = losses
        self.goalsScored = scored
        self.goalsAllowed = allowed

    # Method for Status
    def seasonStatus(self):
        if (self.numWins/(self.numWins + self.numLosses)) >= 0.75: 
            return "NCAA Women's Soccer Tournament!!!"
        elif (self.numWins/(self.numWins + self.numLosses)) < 0.75 and (self.numWins/(self.numWins + self.numLosses)) >= 0.50:
            return "You had a good season!"
        else:
            return "Your team needs to practice :/"

    # Method for Results
    def seasonResults(self):
        print("")
        print(self.teamName)
        print(self.numWins, "-", self.numLosses)
        print(self.goalsScored, "-", self.goalsAllowed)

# Prompts for team name and number of games
stName = input("Enter the team name:  ")
gameNumber = int(input("Enter the number of games that make up the soccer season: "))

# Starting values for team's wins and losses
teamWin = 0
teamLoss = 0
gScored = 0
gAllowed = 0

# For-loop for entering opponents and generating wins, losses, and scores between team and opponent
for iCount in range(1, gameNumber +1, 1):
    opponentName = input("Enter the name of opponent for game " + str(iCount) + ": ")
    teamRand = 0
    opponentRand = 0
    while (teamRand == opponentRand):
        teamRand = random.randrange(0, 10)
        opponentRand = random.randrange(0, 10)
        if teamRand > opponentRand:
            teamWin += 1
            gScored += teamRand
            gAllowed += opponentRand
            print("Your team won game ", iCount," by ", teamRand, "-", opponentRand)
        elif teamRand < opponentRand:
            teamLoss += 1
            gScored += teamRand
            gAllowed += opponentRand
            print("Your team lost game ", iCount," by ", teamRand, "-", opponentRand)
        else:
            continue

# Object
soccerTeam = soccerTeam(stName, teamWin, teamLoss, gScored, gAllowed)

# Outputs
soccerTeam.seasonResults()
print(soccerTeam.seasonStatus())