from character import Character

class Novice(Character):
    def basicAttack(self, character):
        character.reduceHp(self.getDamage)
        print(f"{Novice.getUsername()} performed a Basic Attack! -{self.getDamage()}") #changed self to novice
        


char1 = Novice("kt50")       
print(char1.getUsername())
print(char1.getHp())
#nothing is still happening visually