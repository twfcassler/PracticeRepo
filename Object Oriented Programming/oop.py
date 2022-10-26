class Car():
    make = "Hyundai"

    def __init__(self, myModel, myColor, type, isUnlocked, numWheels, mpg=None):
        #self.make = myMake
        self.model = myModel
        self.color = myColor
        self.type = type
        self.numWheels = 4
        self.isUnlocked = isUnlocked

        if numWheels ==2:
            self.body = "Motorcycle"
        else:
            self.body = "Car"

        self.mpg = mpg

    def drive(self):
        print("Vroom vroom...")
    
    def paint(self, newColor):
        self.color = newColor

    def checkEfficiency(self):
        if (self.mpg != None and self.mpg > 25) or self.type == "Electric":
            return True
        else:
            return False

carModel = input("What is the model? ")

myCar = Car(carModel, "Gray", "Electric", True, 4)
#myOtherCar = Car("Sonatoa", "Silver", "Gas", False, 2, 16)

print(myCar.mpg)
#print(myOtherCar.mpg)

print(myCar.checkEfficiency())

# Car.make = "Tesla"

# print(myCar.make)
# print(myOtherCar.make)

# myDreamCar = Car("Tesla", "Cybertruck", "Space Gray", "Electric", False)

# print("My Car Make", myCar.make)
# print("My Dream Car Make", myDreamCar.make)

# myCar.drive()

# myCar.paint("Blue")
# print(myCar.color)
# print(myDreamCar.color)

# print(myCar.type)

