from novice import Novice

class Magician(Novice):
    def __init__(self, username, types):
        super().__init__(username, types)
        self.setInt(10)
        self.setVit(5)
        self.setHp(self.getHp()+self.getVit())

    def heal(self):
        self.addHp(self.getInt())                                                      #added "()" after getInt, changed "-" to "+" for visual
        print(f"{self.getUsername()} performed Heal! +{self.getInt()}")
    
    def magicAttack(self, character):                                                  #changed name
        self.new_damage = self.getDamage()+self.getInt()
        character.reduceHp(self.new_damage)
        print(f"{self.getUsername()} performed Magic Attack! -{self.new_damage}")      #removed "()" after "new_damage"
