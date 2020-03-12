import Objects
import random
class Path(object):
    def __init__(self):
        self.run()
    def start(self):
        print(f'''
              Welcome Gaurdian. Climb your way to the top. Good Luck
              ''')
        self.playerName = str(input("Enter your name: "))
        print("Hello " + self.playerName)
        self.characterClass = int(input(f'''
                Choose Class:
                (1) Hunter
                (2) Warlock
                (3) Titan
                Enter Choice: '''))
        #sets starting values for player data based on class
        if self.characterClass == 1:
            Objects.weapons.append(Objects.AceofSpades)
            Objects.super.append(Objects.goldenGun)
            Objects.armour = []
            Objects.maxHp = 100
            Objects.hp = 100
            Objects.exp = 0
            Objects.money = 0
            Objects.critChance = 45
            Objects.superCharge = 0
        elif self.characterClass == 2:
            Objects.weapons.append(Objects.HardLight)
            Objects.super.append(Objects.novaBomb)
            Objects.armour = []
            Objects.maxHp = 130
            Objects.hp = 130
            Objects.exp = 0
            Objects.money = 0
            Objects.critChance = 20
            Objects.superCharge = 0
        elif self.characterClass == 3:
            Objects.weapons.append(Objects.Recluse)
            Objects.super.append(Objects.hammerofSol)
            Objects.armour = []
            Objects.maxHp = 200
            Objects.hp = 200
            Objects.exp = 0
            Objects.money = 0
            Objects.critChance = 10
            Objects.superCharge = 0 
    
    def shop(self):
        shopChoice = int(input(f'''
                        -----SHOP-----
                        Money: ${Objects.money}
                        (1) Buy Armour
                        (2) Buy Weapons
                        (3) Reload Weapon
                        (4) Exit
                        Enter Choice: '''))
        if shopChoice == 1:
            print(f'''
                        -----ARMOUR-----''')
            #prints all armour
            for i in range(len(Objects.armourList)):
                armourPointer = Objects.armourList[i]
                print(f'''                        ({i + 1}) [{armourPointer['name']}] ${armourPointer['price']}''')
            armourChoice = int(input("Enter Number: "))
            #gets selected armour info and uses it to do stuff
            armourPointer = Objects.armourList[(armourChoice - 1)]    
            if Objects.money >= armourPointer['price'] and armourPointer['owned'] == False:
                Objects.armour.append(Objects.armourList[i])
                armourPointer['owned'] == True
                Objects.hp += armourPointer['hpAdded']
                Objects.money -= armourPointer['price']
                self.shop()
            else:
                print("Not enough money or already owned")
                self.shop()
                        
        elif shopChoice == 2:
            print(f'''
                        -----WEAPONS-----''')
            #prints all weapons
            for i in range(len(Objects.weaponList)):
                weaponPointer = Objects.weaponList[i]
                print(f'''                        ({i + 1}) [{weaponPointer['name']}] ${weaponPointer['price']}''')                   
            weaponChoice = int(input("Enter Number: "))
            #gets chosen weapon info and does more stuff
            weaponPointer = Objects.weaponList[(weaponChoice - 1)]
            if Objects.money >= weaponPointer['price'] and weaponPointer['owned'] == False:
                Objects.weapons.append(Objects.weaponList[i])
                armourPointer['owned'] == True
                Objects.money -= armourPointer['price']
                self.shop()
            else:
                print("Not enough money or already owned")
                self.shop()
            
        elif shopChoice == 3:
            print("Choose Weapon")
            #lists all owned weapons
            for i in range(len(Objects.weapons)):
                ammoPointer = Objects.weapons[i]
                print(f'''({i + 1}) [{ammoPointer['name']}] Ammo left: {ammoPointer['ammo']}''')
            ammoChoice = int(input("Enter Number: "))
            #gets weapons chosen and refills the magazine
            ammoPointer = Objects.weapons[(ammoChoice - 1)]
            if Objects.money > ((ammoPointer['magSize'] - ammoPointer['ammo']) * ammoPointer['ammoPrice']) and ammoPointer['ammo'] < ammoPointer['magSize']:
                Objects.money -= ((ammoPointer['magSize'] - ammoPointer['ammo']) * ammoPointer['ammoPrice'])
                while ammoPointer['magSize'] > ammoPointer['ammo']:
                    ammoPointer['ammo'] += 1
                print("Magazine Filled")
                self.shop()
            else:
                print("Not enough money or mag full")
                self.shop()
                
        else:
            print("Exiting Shop...")
            
    def battle(self):
        print("ENTERING BATTLE")
        for e in range(len(Objects.enemiesList)):
            enemy = Objects.enemiesList[e]
            Objects.hp = Objects.maxHp
            print("NEW ENEMY: " + enemy['name'])
            while Objects.hp > 0 and enemy['health'] > 0:
                self.shop()
                critRandom = random.randint(1,100)
                #choose weapon to use
                print("Choose weapon for attack")
                for i in range(len(Objects.weapons)):
                    weaponPointer = Objects.weapons[i]
                    print(f'''
                      ({i + 1}) [{weaponPointer['name']}] Damage: {weaponPointer['damage']} Ammo: {weaponPointer['ammo']}
                      ''')
                weaponChoice = int(input("Enter Number: "))
                selectedWeapon = Objects.weapons[(weaponChoice - 1)]
                if selectedWeapon['ammo'] > 0:
                #deals damage based on crit or not
                    if critRandom <= Objects.critChance:
                        enemy['health'] -= (selectedWeapon['damage'] * 1.5)
                        print("CRIT!!! You dealt " + str((selectedWeapon['damage'] * 1.5)) + " damage")
                        selectedWeapon['ammo'] -= 1
                        #gain money for damage done
                        Objects.money += (selectedWeapon['damage'] * 2)
                        #super charged by damage
                        Objects.superCharge += (selectedWeapon['damage'] + .5)
                    else:   
                        enemy['health'] -= selectedWeapon['damage']
                        print("You dealt " + str(selectedWeapon['damage']) + " damage")
                        selectedWeapon['ammo'] -= 1
                        #gain money for damage done
                        Objects.money += (selectedWeapon['damage'] * 2)
                        #super charged by damage
                        Objects.superCharge += (selectedWeapon['damage'] + .5)
                else:
                    print("Out of ammo")
                
                #uses super if charge is full
                if Objects.superCharge >= 100:
                    playerSuper = Objects.super[i]
                    superInput = int(input(f'''
                                           {playerSuper['name']} is charged
                                           (1) Use Super 
                                           (2) Keep Super
                                           '''))
                    if superInput == 1:
                        for i in range(int(super['strength'])):
                            print("Super dealt " + playerSuper['damage'])
                            enemy['health'] -= playerSuper['damage']
                        Objects.superCharge = 0
                #damaged by enemy
                Objects.hp -= enemy['damage']
                print("You took " + str(enemy['damage']) + " damage")
                #print ui of player and enemy
                print(f'''
                      [{self.playerName}]                         [{enemy['name']}]
                      Weapon: {selectedWeapon['name']}            Damage: {enemy['damage']}
                      HP: {Objects.hp}                            HP: {enemy['health']}
                      Super Charge: {Objects.superCharge}/100
                      Money: ${Objects.money}
                      ''')
            #if player is dead go to losing
            if Objects.hp <= 0:
                self.endingLost()
        #wins if all enemies have been defeated
        self.endingWin()
        
    def endingWin(self):
        print("You have beat the game")
    
    def endingLost(self):
        print("You have lost the game. Returning to menu...")
        self.start()
        
    def run(self):
        self.start()
        self.battle()
        
        
 