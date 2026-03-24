from character import Character
import random
class Novice(Character):
    def basicAttack(self, character):
        dmg = self.getDamage()#* random.randint(0,100)
        character.reduceHp(dmg)                                           #added "()"after "getDamage"    
        print(f"{self.getUsername()} performed a Basic Attack! -{dmg}") 
        


char1 = Novice("kt50", "mage")       
print(char1.getUsername())
print(char1.getHp())
#nothing is still happening visually