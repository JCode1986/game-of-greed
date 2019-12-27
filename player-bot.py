""""
Create a Game of Greed Player Bot
ONLY use public methods
- Game class constructor
- play
- calculate_score
"""

from game import Game
import collections
from collections import Counter

class LazyPlayer:
    # constructor, play and calcuate_score available
    # everything else is done only with I/O
    def __init__(self):
        self.roll = None

    def _print(self, *args):
        print(args[0])

    def _input(self, *args):
        print(args[0], 'n')
        return 'n'

class IDontKnowWhatIamDoingPlayer:
    """ Bot set up to run specific combos"""

    def __init__(self):
        self.roll = None
        self.game = None
        self.combinations = {
        1:{1:100, 2:200, 3:1000, 4:2000, 5:3000, 6:4000},
        2:{3:200, 4:400, 5:600, 6:800},
        3:{3:300, 4:600, 5:900, 6:1200},
        4:{3:400, 4:800, 5:1200, 6:1600},
        5:{1:50, 2:100, 3:500, 4:1000, 5:1500, 6:2000},
        6:{3:600, 4:1200, 5:1800, 6:2400},
        }

    def _print(self, *args):
        msg = args[0]
        if msg.startswith("You rolled"):
            self.roll = [int(char) for char in msg if char.isdigit()]

        print(msg)

    def _input(self, *args):
        prompt = args[0]

        if prompt == "Wanna play? ":
            print(prompt, 'y')
            return 'y'

        if prompt == 'Enter dice to keep: ':

            score = self.game._calculate_score(self.roll)

            roll_counter = collections.Counter(self.roll)
            str_to_return = ''
            for index, (key, val) in enumerate(roll_counter.items()):

                if index == 6 and key in self.combinations and val == 1 or val == 5:
                    return self.roll
                
                if score > 400:
                    return self.roll

                if val in self.combinations[key].keys():

                    str_to_return+=str(key)
            return(str_to_return)

if __name__ == "__main__":    
    dummy = IDontKnowWhatIamDoingPlayer()
    game = Game(dummy._print, dummy._input)
    dummy.game = game
    game._play(20)