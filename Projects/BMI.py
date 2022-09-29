# Author: Thomas Cassler
# Description: BMI Assignment that calculates BMI based on weight and height

# inputs
sFirstName = input("Enter your first name: ")
sLastName = input("Enter your last name: ")
iHeight = int(input("Enter your height in feet: "))
iInch = int(input("Enter your additional height in inches: "))
iWeight = int(input("Enter your weight in pounds: "))

iTotalH = (iHeight * 12) + iInch #calculation of total height

fBMI = (iWeight / iTotalH / iTotalH) * 703 #calculation of BMI

# outputs
print(sFirstName, sLastName)
print("has a BMI of", round(fBMI, 1))
