from Objects import Objects

class Path(object):
    def __init__(self):
        self.run()
    def start(self):
        print(f'''
              Welcome to Destiny. Climb your way to the top. Good Luck
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
                           ''')
        if shopChoice == '1':
            armourChoice = int(input(f'''
                                 ----ARMOUR----
                                 (1) Helmet ${Objects.helmet['price']}
                                 (2) Chest Plate ${Objects.chestPlate['price']}
                                 (3) Gauntlets ${Objects.gauntlets['price']}
                                 (4) Boots ${Objects.boots['price']}
                                 '''))
            if armourChoice == '1':
                if Objects.money > Objects.helmet['price']:
                    Objects.armour.append(Objects.helmet)
                    Objects.hp += Objects.helmet['hpAdded']
                    Objects.money -= Objects.helmet['price']
            elif armourChoice == '2':
            elif armourChoice == '3':
            elif armourChoice == '4':
        elif shopChoice == '2':
        elif shopChoice == '3':
    def battle(self):
        
    def ending(self):
        print(f'''
              You have beat the game
              ''')
    def run(self):
        self.start()
        self.battle()
        self.ending()
        
        
 