# Description: Class program for Women's Soccer program
# Author: Thomas Cassler

# Class
class soccerTeam:
    # Constructor
    def __init__(self, tName, wins, losses, score, allowed):
        # Instance Attributes
        self.teamName = tName
        self.numWins = wins
        self.numLosses = losses 
        self.goalsScored = score
        self.goalsAllowed = allowed

    # Method
    def seasonStatus(self):
        if (self.numWins/(self.numWins + self.numLosses)) >= 0.75: 
            return "NCAA Women's Soccer Tournament"
        elif (self.numWins/(self.numWins + self.numLosses)) < 0.75 and (self.numWins/(self.numWins + self.numLosses)) >= 0.50:
            return "You had a good season"
        else:
            return "Your team needs to practice!"

# Object
winResult = soccerTeam("BYU", 5, 5, 50, 100)
# Output of result
print(winResult.seasonStatus())



