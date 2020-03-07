import random
from path import Path
class Objects(object):
    
    def weapons(self):
        self.AceofSpades = {'damage' : 15, 'ammo' : 5, 'price' :900}
        self.BadJuju = {'damage' : 8, 'ammo' : 21, 'price' :700}
        self.HardLight = {'damage' : 5, 'ammo' : 30, 'price' :650}
        self.Revoker = {'damage' : 45, 'ammo' : 2, 'price' : 1500}
        self.LordofWolves = {'damage' : 19, 'ammo' : 4, 'price' :500}
        self.Recluse = {'damage' : 7, 'ammo' : 35, 'price' :800}
        
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
        self.weapons = [self.AceofSpades]
        self.super = [self.goldenGun]
        self.armour = []
        self.maxHp = 100
        self.hp = 100
        self.exp = 0
        self.money = 0
        self.critChance = 45
        self.superCharge = 0
        
    def warlock(self):
        self.wepaons = [self.HardLight]
        self.super = [self.novaBomb]
        self.armour = []
        self.maxHp = 130
        self.hp = 130
        self.exp = 0
        self.money = 0
        self.critChance = 20
        self.superCharge = 0
        
    def titan(self):
        self.weapons = [self.Recluse]
        self.super = [self.hammerofSol]
        self.armour = []
        self.maxHp = 200
        self.hp = 200
        self.exp = 0
        self.money = 0
        self.critChance = 10
        self.superCharge = 0
        
    def enemies(self):
        self.EmperorCalus = {'name' : 'Emperor Calus', 'damage' : 99, 'health' : 400}
        self.Shaxx = {'name' : 'Lord Shaxx', 'damage' : 50, 'health' : 150}
        self.DredgenYor = {'name' : 'Dredgen Yor', 'damage' : 30, 'health' : 140}
    
    def armour(self):
        self.helmet = {'hpAdded' : 10, 'price' : 100}
        self.chestPlate = {'hpAdded' : 15, 'price' :200}
        self.gauntlets = {'hpAdded' : 10, 'price' :120}
        self.boots = {'hpAdded' : 5, 'price' :50}
        