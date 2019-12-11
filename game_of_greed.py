import random

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
    'Three x5': 500,
    'Four x 5':	1000,
    'Five x5': 1500,
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
        self.is_straight = True
        self.roll = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 3}
        #{1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}
    
    #Greeting; Flow
    def play(self):
        self._print('Welcome to Game of Greed')
        question = self._input('Wanna play? press y then enter to proceed. ')
        if question == 'y':
            self._print('Great! Check back tomorrow :D')
        else:
            self._print('OK. Maybe another time')

    def roll_die(self):
        pass

    def calculate_score(self):
        for roll_value, count in self.roll.items():

            #if one of the values is not 1, there is no straight
            if count != 1:
                self.is_straight = False

            #increment pairs
            if count == 2:
                self.pairs += 1

        #points for single 1's and 5's 
        self.score += self.roll[1] * 100
        self.score += self.roll[5] * 50

        if self.roll.items() == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}:
            self.score += int(dice_roll_score_dict['Straight 1 - 6'])

        #Straight
        if self.is_straight:
            self.score += dice_roll_score_dict['Straight 1 - 6']

        #3 Pairs
        if self.pairs == 3:
            self.score += 1500

        # 6's        
        if self.roll[6] == 3:
            self.score += dice_roll_score_dict['Three x 6']
        elif self.roll[6] == 4:
            self.score += dice_roll_score_dict['Four x 6']
        elif self.roll[6] == 5:
            self.score += dice_roll_score_dict['Five x 6']
        elif self.roll[6] == 6:
            self.score += dice_roll_score_dict['Six x 6']

        # 5's
        if self.roll[5] == 3:
            self.score += dice_roll_score_dict['Three x 5']
        elif self.roll[5] == 4:
            self.score += dice_roll_score_dict['Four x 5']
        elif self.roll[5] == 5:
            self.score += dice_roll_score_dict['Five x 5']
        elif self.roll[5] == 6:
            self.score += dice_roll_score_dict['Six x 5']

        # 4's 
        if self.roll[4] == 3:
            self.score += dice_roll_score_dict['Three x 4']
        elif self.roll[4] == 4:
            self.score += dice_roll_score_dict['Four x 4']
        elif self.roll[4] == 5:
            self.score += dice_roll_score_dict['Five x 4']
        elif self.roll[4] == 6:
            self.score += dice_roll_score_dict['Six x 4']

        # 3's
        if self.roll[3] == 3:
            self.score += dice_roll_score_dict['Three x 3']
        elif self.roll[3] == 4:
            self.score += dice_roll_score_dict['Four x 3']
        elif self.roll[3] == 5:
            self.score += dice_roll_score_dict['Five x 3']
        elif self.roll[3] == 6:
            self.score += dice_roll_score_dict['Six x 3']

        # 2's
        if self.roll[2] == 3:
            self.score += dice_roll_score_dict['Three x 2']
        elif self.roll[2] == 4:
            self.score += dice_roll_score_dict['Four x 2']
        elif self.roll[2] == 5:
            self.score += dice_roll_score_dict['Five x 2']
        elif self.roll[2] == 6:
            self.score += dice_roll_score_dict['Six x 2']
        
        # 1's
        if self.roll[1] == 3:
            self.score += dice_roll_score_dict['Three x 1']
        elif self.roll[1] == 4:
            self.score += dice_roll_score_dict['Four x 1']
        elif self.roll[1] == 5:
            self.score += dice_roll_score_dict['Five x 1']
        elif self.roll[1] == 6:
            self.score += dice_roll_score_dict['Six x 1']

        else:
            self.score += 0
        print(self.score)
        return self.score 
        
    def bank_score(self):
        pass

if __name__ == "__main__":
    game = Game()
    # game.play()
    game.calculate_score()
