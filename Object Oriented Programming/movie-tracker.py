
class Person():
    def __init__(self):
        self.name = name
        self.age = age


class Director(Person):
    def __init__(self, name, age, numOscars):
        super().__init__(name, age)
        self.numOscars = 0

    def introduction(self):
        print("My name is " + self.name + " and I have " + str(self.numOscars) + " oscars.")


class Movie():
    def __init__(self, title, director, ageRating):
        # Title, Director, Age Rating, User Score, Is In Theaters
        self.title = title
        self.director = director
        self.ageRating = ageRating
        self.userScore = 0
        self.iiTheaters = False

    def getDescription(self):
        # "<tite> was directed by <directors> and has a rating of <userScore>"
        return self.title + " was directed by " + self.director.name + " and has a rating of " + str(self.userScore)

    def addToTheater(self):
        self.isInTheaters = True

movieDirector = Director("Denie Villenue", 50, 2)
movieDirector.introduction
myMovie = Movie("Dune", movieDirector, "PG-13")
print(myMovie.title)

print(myMovie.getDescription())

myMovie.addToTheater()
print(myMovie.isInTheaters)

# Loop and get user ratings

# How many users?
numUsers = int(input("How many users rated the movie? "))
totalRating = 0

for user in range(numUsers):
    userRating = float(input("What is your rating of the movie? "))
    totalRating += userRating

averageRating = totalRating / numUsers
myMovie.userScore = averageRating

print(myMovie.getDescription())