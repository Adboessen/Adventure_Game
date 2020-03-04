from choices import Choices
from path import Path

def menu():
    menuChoice = input(f'''
                       ----SURVIVOR----
                       (1) Start Game
                       (2) Exit
                       Enter Choice: ''')
    if menuChoice == 1:
        Path()
    else:
        quit
        
    

