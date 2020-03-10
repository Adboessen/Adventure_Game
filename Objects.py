import random
class Objects(object):
    
    def guns(self):
        self.AceofSpades = {'name' : 'Ace of Spades', 'damage' : 15, 'ammo' : 5, 'price' :900, 'ammoPrice' : 10, 'magSize' : 5}
        self.BadJuju = {'name' : 'Bad Juju','damage' : 8, 'ammo' : 21, 'price' :700, 'ammoPrice' : 6, 'magSize' : 21}
        self.HardLight = {'name' : 'Hard Light','damage' : 5, 'ammo' : 30, 'price' :650, 'ammoPrice' : 5, 'magSize' : 30}
        self.Revoker = {'name' : 'Revoker','damage' : 45, 'ammo' : 2, 'price' : 1500, 'ammoPrice' : 200, 'magSize' : 2}
        self.LordofWolves = {'name' : 'Lord of Wolves','damage' : 19, 'ammo' : 4, 'price' :500, 'ammoPrice' : 50, 'magSize' : 4}
        self.Recluse = {'name' : 'Recluse','damage' : 7, 'ammo' : 35, 'price' :800, 'ammoPrice' : 3, 'magSize' : 35}
        self.weaponList = [self.AceofSpades, self.BadJuju, self.HardLight, self.Revoker, self.LordofWolves, self.Recluse]
        
    def armour(self):
        self.helmet = {'name' : 'Helemt', 'hpAdded' : 10, 'price' : 100}
        self.chestPlate = {'name' : 'Chest Plate', 'hpAdded' : 15, 'price' :200}
        self.gauntlets = {'name' : 'Gauntlets', 'hpAdded' : 10, 'price' :120}
        self.boots = {'name' : 'Boots', 'hpAdded' : 5, 'price' :50}
        self.armourList = [self.helmet, self.chestPlate, self.gauntlets, self.boots]
        
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
        self.weapons = [self.HardLight]
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
        self.enemiesList [self.DredgenYor, self.Shaxx, self.EmperorCalus]
    
   