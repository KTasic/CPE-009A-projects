from novice import Novice
import random

class Archer(Novice):
    def __init__(self, username):
        super().__init__(username)
        self.setAgi(5)
        self.setInt(5)
        self.setVit(5)
        self.setHp(self.getHp()+self.getVit())
    
    def rangedAttack(self, character):
        self.new_damage = self.getDamage()+random.ran(0,self.getInt())
        character.reduceHp(self.new_damage)
        print(f"{self.getUsername()} performed a Ranged Attack! -{self.new_damage()}") #changed typo from "slasl" to "ranged"
