from random import randint
from collections import Counter

# Roll and scoring legend
dice_roll_score_dict = {
    'Straight 1 - 6': 1500,
    'Three Pairs': 1500,
    #6
    'Three x 6': 600,
    'Four x 6': 1200,
    'Five x 6':	1800,
    'Six x 6': 2400,
    #5
    'Three x 5': 500,
    'Four x 5':	1000,
    'Five x 5': 1500,
    'Six x 5': 2000,
    #4
    'Three x 4': 400,
    'Four x 4':	800,
    'Five x 4':	1200,
    'Six x 4':	1600,
    #3
    'Three x 3': 300,
    'Four x 3':	600,
    'Five x 3':	900,
    'Six x 3': 1200,
    #2
    'Three x 2': 200,
    'Four x 2':	400,
    'Five x 2':	600,
    'Six x 2':	800,
    #1
    'Three x 1': 1000,
    'Four x 1':	2000,
    'Five x 1':	3000,
    'Six x 1':	4000
}

class Game:
    def __init__(self, print_func=print, input_func=input):
        self._print = print_func
        self._input = input_func
        self.score = 0
        self.pairs = 0
        self.roll = None
    
    #Greeting; Flow
    def play(self):
        self._print('Welcome to Game of Greed')
        question = self._input('Wanna play? press y then enter to proceed. ')
        if question == 'y':
            self.roll = self.roll_dice(6)
            #show dice to user
            self._print(self.roll)
            #what they wanna keep// input on what to keep?
            #score what they kept// calculate score with print
            #ask if they wanna roll again, or bank points
        else:
            self._print('OK. Maybe another time')

    def roll_dice(self, num):
        return tuple(randint(1, 6) for _ in range(num))

    def calculate_score(self, dice):
        dice = Counter(dice)
        is_straight = True
        for roll_value, count in dice.items():

            #if one of the values is not 1, there is no straight
            if count != 1:
                is_straight = False

            #increment pairs
            if count == 2:
                self.pairs += 1

        # if dice.items() == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}:
        #     self.score += int(dice_roll_score_dict['Straight 1 - 6'])

        #Straight
        if is_straight and len(dice) == 6:
            self.score += dice_roll_score_dict['Straight 1 - 6']
            return self.score
        #3 Pairs
        if self.pairs == 3:
            self.score += 1500
            return self.score
        #points for single 1's and 5's 
        if dice[1] == 1:
            self.score += dice[1] * 100
        if dice[5] == 1:
            self.score += dice[5] * 50
        if dice[1] == 2 and self.pairs < 2:
            self.score += dice[1] * 100
        if dice[5] == 2 and self.pairs < 2:
            self.score += dice[5] * 50

        # 6's        
        if dice[6] == 3:
            self.score += dice_roll_score_dict['Three x 6']
        elif dice[6] == 4:
            self.score += dice_roll_score_dict['Four x 6']
        elif dice[6] == 5:
            self.score += dice_roll_score_dict['Five x 6']
        elif dice[6] == 6:
            self.score += dice_roll_score_dict['Six x 6']

        # 5's
        if dice[5] == 3:
            self.score += dice_roll_score_dict['Three x 5']
        elif dice[5] == 4:
            self.score += dice_roll_score_dict['Four x 5']
        elif dice[5] == 5:
            self.score += dice_roll_score_dict['Five x 5']
        elif dice[5] == 6:
            self.score += dice_roll_score_dict['Six x 5']

        # 4's 
        if dice[4] == 3:
            self.score += dice_roll_score_dict['Three x 4']
        elif dice[4] == 4:
            self.score += dice_roll_score_dict['Four x 4']
        elif dice[4] == 5:
            self.score += dice_roll_score_dict['Five x 4']
        elif dice[4] == 6:
            self.score += dice_roll_score_dict['Six x 4']

        # 3's
        if dice[3] == 3:
            self.score += dice_roll_score_dict['Three x 3']
        elif dice[3] == 4:
            self.score += dice_roll_score_dict['Four x 3']
        elif dice[3] == 5:
            self.score += dice_roll_score_dict['Five x 3']
        elif dice[3] == 6:
            self.score += dice_roll_score_dict['Six x 3']

        # 2's
        if dice[2] == 3:
            self.score += dice_roll_score_dict['Three x 2']
        elif dice[2] == 4:
            self.score += dice_roll_score_dict['Four x 2']
        elif dice[2] == 5:
            self.score += dice_roll_score_dict['Five x 2']
        elif dice[2] == 6:
            self.score += dice_roll_score_dict['Six x 2']
        
        # 1's
        if dice[1] == 3:
            self.score += dice_roll_score_dict['Three x 1']
        elif dice[1] == 4:
            self.score += dice_roll_score_dict['Four x 1']
        elif dice[1] == 5:
            self.score += dice_roll_score_dict['Five x 1']
        elif dice[1] == 6:
            self.score += dice_roll_score_dict['Six x 1']

        else:
            self.score += 0
        return self.score 
        
    def bank_score(self):
        pass

if __name__ == "__main__":
    game = Game()
    game.play()
    game.calculate_score()
