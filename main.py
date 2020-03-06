from Classes import Classes
from path import Path

def menu():
    menuChoice = input(f'''
                       ----DESTINY----
                       (1) Start Game
                       (2) Exit
                       Enter Choice: ''')
    if menuChoice == 1:
        Path()
    else:
        quit
        
    

