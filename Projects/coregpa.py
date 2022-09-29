# Description: Assignment for calculating the GPA in advanced way
# Author: Thomas Cassler

# Inputs for grades
overallGPA = float(input("Enter your overall GPA: "))
creditsGPA = float(input("Enter your last 30 credits GPA: "))
accGrade = input("Enter your grade for Accounting 200: ")
is201Grade = input("Enter your grade for IS 201: ")
is303Grade = input("Enter your grade for IS 303: ")
essayScore = int(input("Enter your essay score between 0 and 4: "))

# if-statements for Accounting 200 grades
if (accGrade.upper() == "A"):
    accGrade = 4.0
elif (accGrade.upper() == "A-"):
    accGrade = 3.7
elif (accGrade.upper() == "B+"):
    accGrade = 3.4
elif (accGrade.upper() == "B"):
    accGrade = 3.0
elif (accGrade.upper() == "B-"):
    accGrade = 2.7
elif (accGrade.upper() == "C+"):
    accGrade = 2.4
elif (accGrade.upper() == "C"):
    accGrade = 2.0
elif (accGrade.upper() == "C-"):
    accGrade = 1.7
elif (accGrade.upper() == "D+"):
    accGrade = 1.4
elif (accGrade.upper() == "D"):
    accGrade = 1.0
elif (accGrade.upper() == "D-"):
    accGrade = 0.7
else:
    accGrade = 0

# if-statements for IS 201 grades
if (is201Grade.upper() == "A"):
    is201Grade = 4.0
elif (is201Grade.upper() == "A-"):
    is201Grade = 3.7
elif (is201Grade.upper() == "B+"):
    is201Grade = 3.4
elif (is201Grade.upper() == "B"):
    is201Grade = 3.0
elif (is201Grade.upper() == "B-"):
    is201Grade = 2.7
elif (is201Grade.upper() == "C+"):
    is201Grade = 2.4
elif (is201Grade.upper() == "C"):
    is201Grade = 2.0
elif (is201Grade.upper() == "C-"):
    is201Grade = 1.7
elif (is201Grade.upper() == "D+"):
    is201Grade = 1.4
elif (is201Grade.upper() == "D"):
    is201Grade = 1.0
elif (is201Grade.upper() == "D-"):
    is201Grade = 0.7
else:
    is201Grade = 0

# if-statements for IS 303 grades
if (is303Grade.upper() == "A"):
    is303Grade = 4.0
elif (is303Grade.upper() == "A-"):
    is303Grade = 3.7
elif (is303Grade.upper() == "B+"):
    is303Grade = 3.4
elif (is303Grade.upper() == "B"):
    is303Grade = 3.0
elif (is303Grade.upper() == "B-"):
    is303Grade = 2.7
elif (is303Grade.upper() == "C+"):
    is303Grade = 2.4
elif (is303Grade.upper() == "C"):
    is303Grade = 2.0
elif (is303Grade.upper() == "C-"):
    is303Grade = 1.7
elif (is303Grade.upper() == "D+"):
    is303Grade = 1.4
elif (is303Grade.upper() == "D"):
    is303Grade = 1.0
elif (is303Grade.upper() == "D-"):
    is303Grade = 0.7
else:
    is303Grade = 0

# New GPA formula
newGPA = (accGrade * .05) + (is201Grade * .3) + (is303Grade * .3) + (overallGPA * .12) + (creditsGPA * .18) + (essayScore * .05)

# Display of results
print("Total Apply GPA is calculated ", round(newGPA, 5))

if newGPA >= 3.8:
    print("Chances are very good.")
elif newGPA >= 3.5 and newGPA < 3.8:
    print("Chances are good.")
elif newGPA >= 3.2 and newGPA < 3.5:
    print("Chances are so-so.")
else:
    print("You might want to retake IS 201 and/or IS 303.")