class Animal:
    def __init__(self, name, legs, species):
        self.name = name
        self.legs = legs
        self.species = species

    def setLegs(self, legs):
        self.legs = legs

    def getLegs(self):
        return self.legs 
    
    def printInfo(self):
        print(f"Name{self.name}, Legs: {self.legs}, Species: {self.species}")

animal1 = Animal("Fido", 4, "Dog")
animal2 = Animal("Tweety", 2, "Bird")

print(animal1.name)
print(animal2.name)

animal1.legs = 3

animal2.setLegs = (6)

print(animal1.getLegs())
print(animal2.getLegs())

animal1.printInfo()
animal2.printInfo()