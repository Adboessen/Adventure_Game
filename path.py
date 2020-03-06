from Classes import Classes

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
            Classes.hunter()
        elif self.characterClass == '2':
            Classes.warlock()
        elif self.characterClass == '3':
            Classes.titan()
            
    def shop(self):
        shopChoice = input(f'''
                             -----SHOP-----
                           (1) Buy Consumable
                           (2) Buy Weapons
                           (3) Reload Weapon
                           ''')
        if shopChoice == '1':
            cunsumableChoice = input(f'''
                                     (1) Orb of Light
                                     (2) Health
                                     (3) Damage
                                     ''')
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
        
        
