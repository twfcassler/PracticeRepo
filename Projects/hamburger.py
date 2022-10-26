import random

class Order:
    def __init__(self):
        self.burger_count = self.randomBurgers()

    def randomBurgers(self):
        return random.randint(1, 20)

class Person:
    def __init__(self):
        self.customer_name = self.randomName()

    def randomName(self):
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(asCustomers)

class Customer(Person):
    def __init__(self)
        def super().__init__()
        self.order = Order()


