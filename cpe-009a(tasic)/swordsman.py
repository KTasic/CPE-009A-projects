from novice import Novice

class Swordsman(Novice):
    def __init__(self, username):
        super().__init__(username)
        self.setStrength(5)
        self.setVit(10)
        self.setHp(self.getHp()+self.getVit())
    
    def slashAttack(self, character):
        self.new_damage = self.getDamage()+self.getStrength()
        character.reduceHp((self, self.new_damage()))
        print(f"{self.getUsername()} performed a Slash Attack! -{self.new_damage()}")

