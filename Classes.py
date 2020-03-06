import random
from path import Path
class Classes(object):
    
    def weapons(self):
        self.AceofSpades = {'damage' : 15, 'strength' : 5}
        self.knife = {'damage' : 8, 'strength' : 21}
        self.bow = {'damage' : 10, 'strength' : 30}
        self.longsword = {'damage' : 45, 'strength' : 2}
        self.spell = {'damage' : 11, 'strength' : 11}
        self.spear = {'damage' : 7, 'strength' : 35}
        
    def supers(self):
        self.goldenGun = {'name' : 'Golden Gun', 'damage' : 20, 'strength' : 5}
        self.novaBomb = {'name' : 'Nova Bomb', 'damage' : 30, 'strength' : 3}
        self.hammerofSol = {'name' : 'Hammer of Sol', 'damage' : 15, 'strength' : 7}
        
    def playerHealthbar(self):
        percentageHealth = self.hp / self.maxHp
        print(f'''
              ({self.hp})
              ''')
        for i in range(percentageHealth*10):
            print(f'''
                   =
                  ''')
    
    def hunter(self):
        self.weapons = [self.sword, self.knife]
        self.super = [self.goldenGun]
        self.consumables = []
        self.maxHp = 100
        self.hp = 100
        self.exp = 0
        self.money = 0
        self.critChance = 45
        
    def warlock(self):
        self.wepaons = [self.spell, self.bow]
        self.super = [self.novaBomb]
        self.consumables = []
        self.maxHp = 130
        self.hp = 130
        self.exp = 0
        self.money = 0
        self.critChance = 20
        
    def titan(self):
        self.weapons = [self.spear, self.longsword]
        self.super = [self.hammerofSol]
        self.consumables = []
        self.maxHp = 200
        self.hp = 200
        self.exp = 0
        self.money = 0
        self.critChance = 10
        
    def enemies(self):
        self.DarkKnight = {'damage' : 99, 'health' : 400}
        self.kinght = {'damage' : 50, 'health' : 150}
    
    def consumable(self):