from swordsman import Swordsman
from archer import Archer
from magician import Magician

class Boss(Swordsman, Archer, Magician): # multiple inheritance

    def __init__(self, username, types):
       super().__init__(username, types)
       self.setStrength(10)
       self.setVit(25)
       self.setInt(15)
       self.setHp(self.getHp()+self.getVit())
       #for fairness
       self.__cd1 = 0
       self.__cd2 = 0
       self.__cd3 = 0
       self.__cd4 = 0

    def getCD1(self):
       return self.__cd1
    def setCD1(self, newCD):
       self.__cd1 = newCD
    def getCD2(self):
       return self.__cd2
    def setCD2(self, newCD):
       self.__cd2 = newCD
    def getCD3(self):
       return self.__cd3
    def setCD3(self, newCD):
       self.__cd3 = newCD
    def getCD4(self):
       return self.__cd4
    def setCD4(self, newCD):
       self.__cd4 = newCD

       