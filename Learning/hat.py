import random

# when you only need it once
class Hat:
    houses = ["Gryffindor", "Hufflepuff","Ravenclaw","Slytherin"]
    @classmethod
    def sort(cls,name):
        house = random.choice(cls.houses)
        print(name, "is in", f"{house}")
    


Hat.sort("Harry") # since tere is a classmethod now, you dont need to use the typical hat =Hat()