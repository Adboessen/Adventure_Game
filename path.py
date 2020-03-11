import Objects
import playerClasses
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
        if self.characterClass == '1':
            playerClasses.weapons = [Objects.AceofSpades]
            playerClasses.super = [Objects.goldenGun]
            playerClasses.armour = []
            playerClasses.maxHp = 100
            playerClasses.hp = 100
            playerClasses.exp = 0
            playerClasses.money = 0
            playerClasses.critChance = 45
            playerClasses.superCharge = 0
        elif self.characterClass == '2':
            playerClasses.weapons = [Objects.HardLight]
            playerClasses.super = [Objects.novaBomb]
            playerClasses.armour = []
            playerClasses.maxHp = 130
            playerClasses.hp = 130
            playerClasses.exp = 0
            playerClasses.money = 0
            playerClasses.critChance = 20
            playerClasses.superCharge = 0
        elif self.characterClass == '3':
            playerClasses.weapons = [Objects.Recluse]
            playerClasses.super = [Objects.hammerofSol]
            playerClasses.armour = []
            playerClasses.maxHp = 200
            playerClasses.hp = 200
            playerClasses.exp = 0
            playerClasses.money = 0
            playerClasses.critChance = 10
            playerClasses.superCharge = 0 
    
    def shop(self):
        shopChoice = input(f'''
                        -----SHOP-----
                        (1) Buy Armour
                        (2) Buy Weapons
                        (3) Reload Weapon
                        (4) Exit
                        Enter Choice: ''')
        
        if shopChoice == '1':
            print(f'''
                        -----ARMOUR-----''')
            for i in range(len(Objects.armourList)):
                armourPointer = Objects.armourList[i]
                print(f'''                        ({i + 1}) {armourPointer['name']} ${armourPointer['price']}''')
            armourChoice = input("Enter Number: ")
            for i in range(len(Objects.armourList)):
                armourPointer = Objects.armourList[i]    
                if armourChoice == 'i':
                    if playerClasses.money > armourPointer['price']:
                        playerClasses.armour.append(Objects.armourList[i])
                        playerClasses.hp += armourPointer['hpAdded']
                        playerClasses.money -= armourPointer['price']
                    else:
                        print("Not enough money")
                        self.shop()
                        
        elif shopChoice == '2':
            print(f'''
                        -----WEAPONS-----''')
            for i in range(len(Objects.weaponList)):
                weaponPointer = Objects.weaponList[i]
                print(f'''                        ({i + 1}) {weaponPointer['name']} ${weaponPointer['price']}''')                   
            weaponChoice = input("Enter Number: ")
            
        elif shopChoice == '3':
            print("Choose Weapon")
            for i in range(len(Objects.weapons)):
                ammoPointer = Objects.weapons[i]
                print(f'''({i}) {ammoPointer['name']} Ammo left: {ammoPointer['ammo']}''')
            ammoChoice = input("Enter Number: ")
            for i in range(len(Objects.weapons)):
                if ammoChoice == 'i - 1':
                    if Objects.money > ((Objects.weapons[i['magSize']] - Objects.weapons[i['ammo']]) * Objects.weapons[i['ammoPrice']]):
                        Objects.money -= ((Objects.weapons[i['magSize']] - Objects.weapons[i['ammo']]) * Objects.weapons[i['ammoPrice']])
                        while Objects.weapons[i['magSize']] > Objects.weapons[i['ammo']]:
                            Objects.weapons[i['ammo']] += 1
                        print("Magazine Filled")
                    else:
                        print("Not enough money")
                        self.shop()
        else:
            print("Exiting Shop")
            
    def battle(self):
        print("Entering Battle")
        self.shop()
        while 
        
    def ending(self):
        print("You have beat the game")
        
    def run(self):
        self.start()
        self.battle()
        self.ending()
        
        
 