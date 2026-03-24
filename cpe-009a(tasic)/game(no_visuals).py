from novice import Novice
from swordsman import Swordsman
from archer import Archer
from magician import Magician
from boss import Boss
from Character_select import charSelect, charSelect_solo
import random

def boss_actions(wins, atacker, defender):
    if wins <= 2:
        atacker.basicAttack(defender)
    elif wins > 2:
        if atacker.getHp() < 50 and atacker.getCD4() == 0:
            if atacker.getCD4() == 0:
                atacker.heal()
                atacker.setCD4(6)
            else:
                atacker.setCD4(atacker.getCD4()-1)
        else:
            choice = random.randint(1,4)
            decided = False
            while decided == False:
                match choice:
                    case 1:
                        atacker.basicAttack(defender)
                        decided = True
                    case 2:
                        if atacker.getCD1() == 0:
                            atacker.slashAttack(defender)
                            atacker.setCD1(4)
                            decided = True
                        else:
                            atacker.setCD1(atacker.getCD1()-1)
                    case 3:
                        if atacker.getCD2() == 0:
                            atacker.rangedAttack(defender)
                            atacker.setCD2(6)
                            decided = True
                        else:
                            atacker.setCD2(atacker.getCD2()-1)
                    case 4:
                        if atacker.getCD3() == 0:
                            atacker.magicAttack(defender)
                            atacker.setCD3(6)
                            decided = True
                        else:
                            atacker.setCD3(atacker.getCD3()-1)

    atacker.setCD1(max(0,atacker.getCD1()-1))
    atacker.setCD2(max(0,atacker.getCD2()-1))
    atacker.setCD3(max(0,atacker.getCD3()-1))
    atacker.setCD4(max(0,atacker.getCD4()-1))


                    
        


def battle_pvp(p1, p2):
    print("\n===== BATTLE START =====")
    players = [p1, p2]
    random.shuffle(players)

    while p1.getHp() > 0 and p2.getHp() > 0:
        attacker = players[0]
        defender = players[1]

        print(f"\n{attacker.getUsername()}'s turn!")
        
        match attacker.getType():
            case "swordsman":
                print("********************************")
                print("*                               ")
                print(f"*     [{attacker.getUsername()} pick a move]     ")
                print("*                               ")
                print("*          1. Basic attack         ")
                print("*          2. slash Attack            ")
                print("*                               ")
                print("*                               ")
                print("*                               ")
                print("********************************")
                move = int(input("enter move(number): "))
                if move == 1:
                    attacker.basicAttack(defender)
                elif move == 2:
                    attacker.slashAttack(defender)
            case "archer":
                print("********************************")
                print("*                               ")
                print(f"*     [{attacker.getUsername()} pick a move]     ")
                print("*                               ")
                print("*          1. Basic attack         ")
                print("*          2. ranged Attack           ")
                print("*                               ")
                print("*                               ")
                print("*                               ")
                print("********************************")
                move = int(input("enter move(number): "))
                if move == 1:
                    attacker.basicAttack(defender)
                elif move == 2:
                    attacker.rangedAttack(defender)
            case "magician":
                print("********************************")
                print("*                               ")
                print(f"*     [{attacker.getUsername()} pick a move]     ")
                print("*                               ")
                print("*          1. Basic attack         ")
                print("*          2. Heal           ")
                print("*          3. magic Attack           ")
                print("*                               ")
                print("*                               ")
                print("********************************")
                move = int(input("enter move(number): "))
                if move == 1:
                    attacker.basicAttack(defender)
                elif move == 2:
                    attacker.heal()
                elif move == 3:
                    attacker.magicAttack(defender)
                
        print(f"{p1.getUsername()} HP: {max(0,p1.getHp())}")
        print(f"{p2.getUsername()} HP: {max(0,p2.getHp())}")

        players.reverse()
    
    if p1.getHp() > 0:
        print(f"\n{p1.getUsername()} wins!")
        return p1
    else:
        print(f"\n{p2.getUsername()} wins!")
        return p2

def battle_solo():
    char1 = Novice(input("enter username: "), "novice")       
    print("\n===== BATTLE START =====") 
    wins = 0
    upgraded = False
    while char1.getHp() > 0:
        print(f"\n===== Round {wins+1} =====")             
        mob = Boss("Monster", "mob")
        if wins <= 2:
            mob.setHp(10)
        if upgraded == False and wins >= 2:
            print("*********************************")
            print("*                               ")
            print(f"*     [{char1.getUsername()} Select upgrade Character]     ")
            print("*                               ")
            print("*          1. Swordsman         ")
            print("*          2. Archer            ")
            print("*          3. Magician          ")
            print("*                               ")
            print("*                               ")
            print("*********************************")
            char1 = charSelect_solo(int(input("what would you like to do? (enter number): ")), char1, char1.getUsername())
            upgraded = True
        while char1.getHp() > 0 and mob.getHp() > 0:
            attacker = char1
            defender = mob

            print(f"\n{attacker.getUsername()}'s turn!")
        
            match attacker.getType():
                case "swordsman":
                    print("********************************")
                    print("*                               ")
                    print(f"*     [{attacker.getUsername()} pick a move]     ")
                    print("*                               ")
                    print("*          1. Basic attack         ")
                    print("*          2. slash Attack            ")
                    print("*                               ")
                    print("*                               ")
                    print("*                               ")
                    print("********************************")
                    move = int(input("enter move(number): "))
                    if move == 1:
                        attacker.basicAttack(defender)
                    elif move == 2:
                        attacker.slashAttack(defender)
                case "archer":
                    print("********************************")
                    print("*                               ")
                    print(f"*     [{attacker.getUsername()} pick a move]     ")
                    print("*                               ")
                    print("*          1. Basic attack         ")
                    print("*          2. ranged Attack           ")
                    print("*                               ")
                    print("*                               ")
                    print("*                               ")
                    print("********************************")
                    move = int(input("enter move(number): "))
                    if move == 1:
                        attacker.basicAttack(defender)
                    elif move == 2:
                        attacker.rangedAttack(defender)
                case "magician":
                    print("********************************")
                    print("*                               ")
                    print(f"*     [{attacker.getUsername()} pick a move]     ")
                    print("*                               ")
                    print("*          1. Basic attack         ")
                    print("*          2. Heal           ")
                    print("*          3. magic Attack           ")
                    print("*                               ")
                    print("*                               ")
                    print("********************************")
                    move = int(input("enter move(number): "))
                    if move == 1:
                        attacker.basicAttack(defender)
                    elif move == 2:
                        attacker.heal()
                    elif move == 3:
                        attacker.magicAttack(defender)
                case "novice":
                    print("********************************")
                    print("*                               ")
                    print(f"*     [{attacker.getUsername()} pick a move]     ")
                    print("*                               ")
                    print("*          1. Basic attack         ")
                    print("*                               ")
                    print("*                               ")
                    print("*                               ")
                    print("*                               ")
                    print("********************************")
                    move = int(input("enter move(number): "))
                    if move == 1:
                        attacker.basicAttack(defender)
            boss_actions(wins, mob, char1)

            print(f"{char1.getUsername()} HP: {max(0,char1.getHp())}")
            print(f"{mob.getUsername()} HP: {max(0,mob.getHp())}")
        
        if char1.getHp() > 0:
            wins += 1
            print(f"\n{char1.getUsername()} wins! Here is your rewards")
            print("********************************")
            print("*                               ")
            print(f"*     [{char1.getUsername()} Select Reward]     ")
            print("*                               ")
            print("*          1. HP + 50         ")
            print("*          2. Str +10            ")
            print("*          3. Int +10          ")
            print("*                               ")
            print("*                               ")
            print("********************************")
            reward = int(input("what would you like to get? (enter number): ")) 
            match reward:
                case 1:
                    char1.setHp(char1.getHp()+50)
                case 2:
                    char1.setStrength(char1.getStrength()+10)
                case 3:
                    char1.setInt(char1.getInt()+10)

        else:
            print(f"\n{char1.getUsername()} Lose!")

        





play = True

while play == True:
    #home screen
    print("*********************************")
    print("*                               *")
    print("*           [R. P. G]           *")
    print("*                               *")
    print("*          1. Solo              *")
    print("*          2. P. V. P.          *")
    print("*          3. Quit              *")
    print("*                               *")
    print("*                               *")
    print("*********************************")
    user_input = int(input("what would you like to do? (enter number): "))
    
    #selection
    match user_input:
        case 3:
            print("Bye-bye")
            play = False

        case 2:
            print("*********************************")
            print("*                               *")
            print("*     [P1 Select Character]     *")
            print("*                               *")
            print("*          1. Swordsman         *")
            print("*          2. Archer            *")
            print("*          3. Magician          *")
            print("*                               *")
            print("*                               *")
            print("*********************************")
            p1Char = charSelect(int(input("what would you like to do? (enter number): ")), "p1")
            p1Char.setUsername(input("enter username: "))

            print("*********************************")
            print("*                               *")
            print("*     [P2 Select Character]     *")
            print("*                               *")
            print("*          1. Swordsman         *")
            print("*          2. Archer            *")
            print("*          3. Magician          *")
            print("*                               *")
            print("*                               *")
            print("*********************************")
            p2Char = charSelect(int(input("what would you like to do? (enter number): ")), "p2")
            p2Char.setUsername(input("enter username: "))

            battle_pvp(p1Char, p2Char)
        
        case 1:
            battle_solo()


















#magician vs swordsman
'''print(f"{p1Char.getUsername()} HP: {p1Char.getHp()}")
print(f"{p2Char.getUsername()} HP: {p2Char.getHp()}")
p1Char.slashAttack(p1Char)
p1Char.basicAttack(p1Char)
print(f"{p1Char.getUsername()} HP: {p1Char.getHp()}")
print(f"{p2Char.getUsername()} HP: {p2Char.getHp()}")
p2Char.heal()
p2Char.magicAttack(p1Char)
print(f"{p1Char.getUsername()} HP: {p1Char.getHp()}")
print(f"{p2Char.getUsername()} HP: {p2Char.getHp()}")'''

            

            
            


            






 
    


    
