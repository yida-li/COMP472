####################################################
# 15. : Inheritance
####################################################
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        return(self.lastname)


class Sex(Person):
    def __init__(self, fname, lname, gender):
        super().__init__(fname, lname)
        self.GEN = gender


print("\nsuper() function that will make the child class inherit all the methods and properties from its parent: BTW\n\n")


x = Sex("Mike", "Olsen", "female")

print("Printing one of its own variable : {}, calling a function from its parent object : {}".
      format(x.GEN, x.printname()))

Art = " -- "


class Mutant(Sex):
    def __init__(self, fname, lname, gender, superpower):
        super().__init__(fname, lname, gender)
        self.SP = superpower

    def printEverything(self):
        print(self.firstname, Art, self.lastname, Art, self.GEN, Art, self.SP)


print("\n NOW Multi-level inheritance BTW\n\n")
y = Mutant("Max", "Eisenhardt", "male", "magnetism")


y.printEverything()
