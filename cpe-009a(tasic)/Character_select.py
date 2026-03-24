from swordsman import Swordsman
from archer import Archer
from magician import Magician

def charSelect(user_input, char):
    match user_input:
        case 1:
            return Swordsman(char,"swordsman")
        case 2: 
            return Archer(char, "archer")
        case 3:
            return Magician(char, "magician")
    
def charSelect_solo(user_input, char, username):
    match user_input:
        case 1:
            oldhp = char.getHp()
            oldstr = char.getStrength()
            oldint = char.getInt()
            char1 = Swordsman(char,"swordsman")
            char1.setHp(char1.getHp()+oldhp)
            char1.setStrength(char1.getStrength()+oldstr)
            char1.setInt(char1.getInt()+oldint)
            char1.setUsername(username)
            return char1
        case 2: 
            oldhp = char.getHp()
            oldstr = char.getStrength()
            oldint = char.getInt()
            char1 = Archer(char, "archer")
            char1.setHp(char1.getHp()+oldhp)
            char1.setStrength(char1.getStrength()+oldstr)
            char1.setInt(char1.getInt()+oldint)
            char1.setUsername(username)
            return char1
        case 3:
            oldhp = char.getHp()
            oldstr = char.getStrength()
            oldint = char.getInt()
            char1 = Magician(char, "magician")
            char1.setHp(char1.getHp()+oldhp)
            char1.setStrength(char1.getStrength()+oldstr)
            char1.setInt(char1.getInt()+oldint)
            char1.setUsername(username)
            return char1