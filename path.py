from choices import Choices

class Path(object):
    def __init__(self):
        self.run()
    def start(self):
        print(f'''
              Welcome to Survivor. Don't Die. Good Luck
              ''')
        self.playerName = str(input("Enter your name: "))
        print("Hello " + self.playerName)
        self.startPoint = int(input(f'''
                Choose Start Location:
                (1) Jungle
                (2) Forest
                (3) Desert'''))
    def body(self):
        if self.startPoint == '1':
            Choices.jungle
        elif self.startPoint == '2':
            Choices.forest
        elif self.startPoint == '3':
            Choices.desert
    
    def ending(self):
        
    def run(self):
        self.start()
        self.body()
        self.ending()
        
    def survived(self):
        
        
