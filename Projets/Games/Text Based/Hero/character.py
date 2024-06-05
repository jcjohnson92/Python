from weapon import *
import random

class Character():
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
        self.health_max = health

    
        
        self.weapon = mace

    def attack(self, target):
        target.health -= mace.damage        
        target.health = max(target.health, 0)
        print(f"{self.name} dealt {self.weapon.damage} damage to {target.name}")

    

class Player(Character):
    def __init__(self, name:str, health:int) -> None:
        super().__init__(name=name, health=health)


class Computer(Character):
    def __init__(self, name:str, health:int) -> None:
        super().__init__(name=name, health=health)

