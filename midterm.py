# Description: Program that calculates each Olympic Athlete's Glory
#Author: Thomas Cassler

#Class for individual
class Person:
    first_name = ""
    last_name = ""

    def __init__(self, firstName, lastName):
        self.first_name = firstName
        self.last_name = lastName

    def get_fullname(self):
        return self.first_name + " " + self.last_name

#Class for medals
class Medals:
    def __init__(self, medal, quantity, dollar):
        self.medal_type = medal
        self.total_amount = quantity
        self.dollar_amount = dollar

#Class for athletes
class Athlete(Person):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName)
        self.medals_earned = []
        self.total_amount = 0

#Prompt for number of athletes
numAthletes = int(input("How many athletes? \n"))

# For loop for inputting data for every athlete
for iCount in range(1, numAthletes +1, 1):
    fName = str(input("Enter Athlete " + str(iCount) + "'s first name: \n"))
    lName = str(input("Enter Athlete " + str(iCount) + "'s last name: \n"))

    #Object for Athlete class
    athlete = Athlete(fName, lName)
    
    #Input for gold medals
    goldCount = int(input("Enter " + fName + "'s gold medal count: \n"))
    goldValue = goldCount * 37500
    medals = Medals("G", goldCount, goldValue)
    athlete.medals_earned.append(medals)

    #Input for silver medals
    silverCount = int(input("Enter " + fName + "'s silver medal count: \n"))
    silverValue = silverCount * 22500
    medals = Medals("S", silverCount, silverValue)
    athlete.medals_earned.append(medals)

    #Input for bronze medals
    bronzeCount = int(input("Enter " + fName + "'s bronze medal count: \n"))
    bronzeValue = bronzeCount * 15000
    medals = Medals("B", bronzeCount, bronzeValue)
    athlete.medals_earned.append(medals)
    # athlete.total_amount() == athlete.total_amount() + bronzeValue

    #Calculation for total amount
    totalAmount = goldValue + silverValue + bronzeValue

    #Results
    print(athlete.get_fullname() + " earned $" + str(totalAmount))
    print(str(goldCount) + " Gold medal(s) worth $" + str(goldValue))
    print(str(silverCount) + " Gold medal(s) worth $" + str(silverValue))
    print(str(bronzeCount) + " Gold medal(s) worth $" + str(bronzeValue))
    print("\n \n")

