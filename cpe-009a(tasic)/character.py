class Character():
    def __init__(self, username):
        self.__username = username
        self.__hp = 100
        self.__mana = 100
        self.__damage = 5
        self.__stren = 0 #strength stat
        self.__vit = 0 #vitality stat
        self.__int = 0 #inteligence stat
        self.__agi = 0 #agility stat
    def getUsername(self):
        return self.__username
    def setUsername(self, new_username):
        self.__username = new_username
    def getHp(self):
        return self.__hp
    def setHp(self, new_hp):
        self.__hp = new_hp
    def getMana(self):             #added getMana
        return self.__mana 
    def setMana(self, new_mana):   #added setMana
        self.__mana = new_mana
    def getDamage(self):
        return self.__damage
    def setDamage(self, new_damage):
        self.__damage = new_damage
    def getStrength(self):              #Changed all "str" to stren
        return self.__stren
    def setStrength(self, new_stren):
        self.__stren = new_stren
    def getVit(self):
        return self.__vit
    def setVit(self, new_vit):
        self.__vit = new_vit
    def getInt(self):
        return self.__int
    def setInt(self, new_int):
        self.__int = new_int
    def getAgi(self):
        return self.__agi
    def setAgi(self, new_agi):
        self.__agi = new_agi
    def reduceHp(self, damage_ammount):
        self.__hp = self.__hp - damage_ammount
    def addHp(self, heal_ammount):
        self.__hp = self.__hp + heal_ammount



print("test")
char1 = Character("kt50")       
print(char1.getUsername())
#removed "print(character1.__username)"