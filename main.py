from character import Character 
import random

def main():
    boss = Character(name='Boss', hp=100, ability_power=10, dodge=0.15)
    protagonist = Character(name='You', hp=100, ability_power=10, dodge=0.15)
    
    while True:
        
        print("1.Heal, 2.Attack")
        answer =  int(input("Action:"))
        if(answer == 1):
            protagonist.heal()

        boss.attack(protagonist)
        
        boss_status = boss.check_life()
        protagonist_status = protagonist.check_life()
        if not boss_status or not protagonist_status:
            break
    print('Game over!')


if __name__ == '__main__':
    main()
