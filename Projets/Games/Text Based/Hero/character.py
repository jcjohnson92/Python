from weapon import *
import random

class Character():
    def __init__(self, name: str, health: int   ) -> None:
        self.name = name
        self.health = health
        self.health_max = health

    
    
        self.weapon = (fists,mace,sword,dagger)

    def attack(self, target,choice):
        print(f"{self.weapon[choice].name}")
        luck = random.randrange(1,10)
        target.health -= self.weapon[choice].damage + luck       
        target.health = max(target.health, 0)

        print(f"{self.name} dealt {self.weapon[choice].damage + luck} damage to {target.name}")
        print(f"Targets Health: {target.health} ")


