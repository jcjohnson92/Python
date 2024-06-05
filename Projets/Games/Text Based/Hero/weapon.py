import random
mace_lst = (11,12,13)
luck = random.randrange(1,5)

class Weapons():
    def __init__(self, name:str, type:str, damage:list, value:int) -> None:
        self.name = name
        self.type = type
        self.damage = damage
        self.value = value

 
fists = Weapons(name="Fists", type="Physical", damage=(5+luck),value=0)
sword = Weapons(name="Sword", type="Slash", damage=12, value=10)
mace = Weapons(name="Mace", type="Blunt", damage=11, value=7)
