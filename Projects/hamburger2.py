# Braden Toone
# Create a program to track how many hamburgers customers eat.

from random import randint

# Order class
class Order():
    # Constructor that assigns burger_count by calling randomBurgers method
    def __init__(self):
        self.burger_count = self.randomBurgers()
    # randomBurgers method generates random number between 1 and 20 using randit
    def randomBurgers(self):
        return randint(1, 20)

# Person class
class Person():
    # Constructor that assigns customer_name by calling randomName method
    def __init__(self):
        self.customer_name = self.randomName()
    # randomName method that generates a random name out of a list of 9 using randint
    def randomName(self):
        nameList = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander","Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        randIndex = randint(0,8)
        return nameList[randIndex]

# Customer class that inherits Person class
class Customer(Person):
    # Constructor that calls Parent constructor and assigns order by calling Order object
    def __init__(self):
        super().__init__()
        self.order = Order()

# Created empty customerQueue and customerDictionary set to possible names with starting value of 0 burgers
customerQueue = []
customerDictionary = {"Jefe": 0, "El Guapo": 0, "Lucky Day": 0, "Ned Nederlander": 0,"Dusty Bottoms": 0, "Harry Flugleman": 0, "Carmen": 0, "Invisible Swordsman": 0, "Singing Bush": 0}

# Creating new customer instance, adding customer to customerQueue, and updating customerDictionary value looped 100 times
for i in range(0,99):
    customer = Customer()
    customerQueue.append(customer)
    customerDictionary[customer.customer_name] += customer.order.burger_count
    i += 1

# Creating a sorted customer list from customerDictionary
sortedCustomerList = sorted(customerDictionary.items(), key=lambda x: x[1], reverse=True)

# Prints each customer and their burger value in the sortedDictionary
for i in range(0, len(sortedCustomerList)):
    # sortedCustomerList is a nested list. customer.customer_name is accessed by [i][0], 
    # customer.order.burger_count is accessed by [i][1]
    print(str(sortedCustomerList[i][0]).ljust(30) + str(sortedCustomerList[i][1]))