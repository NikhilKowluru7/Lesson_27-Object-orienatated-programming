class dog:
    def __init__(self,colour,breed):
        self.breed = breed
        self.colour = colour
    animal  = "dog"
bob = dog("labrador","blonde")
bill = dog("Border Collie","black")
print("The first animal is a",bob.animal,"The dog's breed is",bob.breed,"The dog is",bob.colour)
print("The second animal is also a",bill.animal,"The dog's breed is",bill.breed,"The dog is",bill.colour)