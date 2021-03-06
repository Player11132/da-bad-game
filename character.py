import random

class Character:
    
    def __init__(self, name, hp=100, ability_power=10, dodge=0.15):
        self._name          = name
        self._hp            = hp
        self._ability_power = ability_power
        self._dodge         = dodge

    
    def check_life(self):
        if self._hp <= 0:
            return False
        return True
    
    
    def heal(self):
        luck = random.uniform(0, 1)
        heal = luck * self._ability_power
        self._hp += heal
        

    def attack(self, target):
        luck = random.uniform(0, 1)
        damage = luck * self._ability_power
        target.take_damage(damage)
        return damage

    
    def take_damage(self, damage):
        luck = random.uniform(0, 1)
            self._hp -= damage
