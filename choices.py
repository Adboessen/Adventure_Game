from path import Path
class Choices(object):
    
    def jungle(self):
        riverChoice = input(f'''
                       You arrive at a river
                       (1) Swim across
                       (2) Follow river
                       (3) Turn around
                        ''')
        if riverChoice == '1':
            print(f'''
                You were eaten by an alligator
                ''')
            Path.ending
        elif riverChoice == '2':
            boatChoice = input(f'''
                            You see a boat on the shore
                            (1) Continue
                            (2) Get in it
                            ''')
            if boatChoice == '1':
                movementChoice = input(f'''
                                You see movement further into the jungle
                                (1) Ignore it
                                (2) Investigate it
                                ''')
                if movementChoice == '1':
                    waterfallChoice = input(f'''
                                   The river ends at a waterfall
                                   (1) Go into the jungle
                                   (2) Try to go down it
                                   ''')
                    if waterfallChoice == '1':
                        jungleChoice = input(f'''
                                             You have been walking for over five hours and feel dehydrated
                                             (1) Continue
                                             (2) Search for water
                                             ''')
                        if jungleChoice == '1':
                            print(f'''
                                  You colapse shortly after from dehydration
                                  ''')
                            Path.ending
                        elif jungleChoice == '2':
                            print(f'''
                                  You find water but it makes you sick and you die
                                  ''')
                            Path.ending
                    elif waterfallChoice == '2':
                        print(f'''
                              You slipped and died scaling the waterfall
                              ''')
                        Path.ending
            elif boatChoice == '2':
                print(f'''
                        There was a hole in the boat and you drowned
                    ''')
                Path.ending
        elif riverChoice == '3':
            villageChoice = input(f'''
                                  You see a village in the distance
                                  (1) Go around it
                                  (2) Enter the village
                                  ''')
            if villageChoice == '1':
                templeChoice = input(f'''
                                     You arrive at an ancient temple 
                                     (1) Go inside
                                     (2) 
                                     ''')
            elif villageChoice == '2':
                print(f'''
                      You are captured by the village people and sacrifed to the gods
                      ''')
                Path.ending