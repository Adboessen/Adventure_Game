from Objects import Objects

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
                (3) Titan'''))
        if self.characterClass == '1':
            Objects.hunter()
        elif self.characterClass == '2':
            Objects.warlock()
        elif self.characterClass == '3':
            Objects.titan()
            
    def shop(self):
        shopChoice = input(f'''
                             -----SHOP-----
                           (1) Buy Armour
                           (2) Buy Weapons
                           (3) Reload Weapon
                           (4) Exit
                           ''')
        if shopChoice == '1':
            armourChoice = int(input(f'''
                                 ----ARMOUR----
                                 (1) Helmet ${Objects.helmet['price']}
                                 (2) Chest Plate ${Objects.chestPlate['price']}
                                 (3) Gauntlets ${Objects.gauntlets['price']}
                                 (4) Boots ${Objects.boots['price']}
                                 Enter Number: 
                                 '''))
            for i in range(len(Objects.armourList)):    
                if armourChoice == 'i':
                    if Objects.money > Objects.armourList[i['price']]:
                        Objects.armour.append(Objects.armourList[i])
                        Objects.hp += Objects.armourList[i['hpAdded']]
                        Objects.money -= Objects.armourList[['price']]
                    else:
                        print("Not enough money")
                        self.shop()
        elif shopChoice == '2':
            for i in range(len(Objects.weaponList)):
                print(f'''
                            -----WEAPONS-----
                            ({i}) {Objects.weaponList[i['name']]} ${Objects.wepaonList[i['price']]}
                            ''')
            weaponChoice = input("Enter Number: ")
        elif shopChoice == '3':
            print("Choose Weapon")
            for i in range(len(Objects.weapons)):
                print(f'''({i}) {Objects.weapons[i['name']]} Ammo left: {Objects.weapons[i['ammo']]}''')
            ammoChoice = input("Enter Choice: ")
            for i in range((Objects.weapons)):
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
        
    def ending(self):
        print(f'''
              You have beat the game
              ''')
    def run(self):
        self.start()
        self.battle()
        self.ending()
        
        
 