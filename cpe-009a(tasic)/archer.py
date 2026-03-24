from novice import Novice
import random

class Archer(Novice):
    def __init__(self, username, types):
        super().__init__(username, types)
        self.setAgi(5)
        self.setInt(5)
        self.setVit(5)
        self.setHp(self.getHp()+self.getVit())
    
    def rangedAttack(self, character):
        self.new_damage = self.getDamage()+random.randint(0,self.getInt()+15)             #changed "random.ran" to "random.randint"
        character.reduceHp(self.new_damage)
        print(f"{self.getUsername()} performed a Ranged Attack! -{self.new_damage}") #changed typo from "slasl" to "ranged", removed "()" from "self.new_damage"
