class parrot:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    species = "bird"

bob = parrot("Bob",6)
bill = parrot("Bill",7)

print("The first bird's name is",bob.name,"Bob's age is",bob.age,"Bob is a ",bob.species)
print("The second bird's name is",bill.name,"Bill's age is",bill.age,"Bill is a ",bill.species)
