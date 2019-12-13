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
        self.turns = 10
    
    #Greeting; Flow
    def play(self):
        self._print('Welcome to Game of Greed')
        question = self._input('Wanna play? press y then enter to proceed. ')
        if question == 'y':
            self._print('Game Rules: You get to roll 6 die. Single fives are worth 50 points | Single ones are worth 100 points | You get a certain amount of points when getting 3 pairs, three or more of the same number, or a straight. Choose to store your points, by picking specific die that gives you points. This also removes that die in the process, leaving you with less die to roll with. If you dont get any points, you will lose your turn, and lose any points you have stored in the process. Bank your points if you don\'t feel lucky.')

            self._input('Hit enter to start the game ')
            self.start()

        else:
            self._print('OK. Maybe another time')

    def start(self):
        self.score = 0

        round_num = 1

        for i in range(1, self.turns + 1):
            round_score = self.handle_round()

            self._print(f'You banked {round_score} points in round {round_num}')

            self.score += round_score

            round_num += 1

            self._print(f'You have {self.score} points total')


        self._print('Thanks for playing!')

    def roll_dice(self, num):
        return tuple(randint(1, 6) for _ in range(num))

    def validate_roll(self, roll):
        while True:

            keep_response = self._input('Enter which ones to keep: ')

            keepers = tuple(int(char) for char in keep_response)

            if self.validate(roll, keepers):
                return keepers
            else:
                self._print('No way pal')
                self._print(roll)

    def validate(self, roll, keepers):

        roll_counter = Counter(roll)
        keepers_counter = Counter(keepers)
        return len(keepers_counter - roll_counter) == 0

    def handle_round(self):
        num_dice = 6

        score = 0

        while(True):
            self._print(f'Rolling {num_dice} dice')

            roll = self.roll_dice(num_dice)

            zilch_check_score = self.calculate_score(roll)

            self._print(f'{self.turns}: You rolled {roll}')

            if zilch_check_score == 0:
                self._print('Oh noes! Zilch')
                return 0

            keepers = self.validate_roll(roll)

            # TODO: handle non scoring but mysteriously used dice
            num_dice -= len(keepers)

            score += self.calculate_score(keepers)

            self._print(f'You can bank {score} points or try for more')

            if num_dice == 0:
                num_dice = 6

            self._print(f'You have {num_dice} dice remaining')

            roll_again_response = self._input(f'Roll again? y/n: ')

            if not roll_again_response == 'y':
                break


        return score



    def calculate_score(self, dice):
        score = 0
        dice = Counter(dice)
        is_straight = True
        for roll_value, count in dice.items():

            #if one of the values is not 1, there is no straight
            if count != 1:
                is_straight = False

            #increment pairs
            if count == 2:
                self.pairs += 1

        #Straight
        if is_straight and len(dice) == 6:
            score += dice_roll_score_dict['Straight 1 - 6']
            return score
        #3 Pairs
        if self.pairs == 3:
            score += 1500
            return score
        #points for single 1's and 5's 
        if dice[1] == 1:
            score += dice[1] * 100
        if dice[5] == 1:
            score += dice[5] * 50
        if dice[1] == 2 and self.pairs < 2:
            score += dice[1] * 100
        if dice[5] == 2 and self.pairs < 2:
            score += dice[5] * 50

        # 6's        
        if dice[6] == 3:
            score += dice_roll_score_dict['Three x 6']
        elif dice[6] == 4:
            score += dice_roll_score_dict['Four x 6']
        elif dice[6] == 5:
            score += dice_roll_score_dict['Five x 6']
        elif dice[6] == 6:
            score += dice_roll_score_dict['Six x 6']

        # 5's
        if dice[5] == 3:
            score += dice_roll_score_dict['Three x 5']
        elif dice[5] == 4:
            score += dice_roll_score_dict['Four x 5']
        elif dice[5] == 5:
            score += dice_roll_score_dict['Five x 5']
        elif dice[5] == 6:
            score += dice_roll_score_dict['Six x 5']

        # 4's 
        if dice[4] == 3:
            score += dice_roll_score_dict['Three x 4']
        elif dice[4] == 4:
            score += dice_roll_score_dict['Four x 4']
        elif dice[4] == 5:
            score += dice_roll_score_dict['Five x 4']
        elif dice[4] == 6:
            score += dice_roll_score_dict['Six x 4']

        # 3's
        if dice[3] == 3:
            score += dice_roll_score_dict['Three x 3']
        elif dice[3] == 4:
            score += dice_roll_score_dict['Four x 3']
        elif dice[3] == 5:
            score += dice_roll_score_dict['Five x 3']
        elif dice[3] == 6:
            score += dice_roll_score_dict['Six x 3']

        # 2's
        if dice[2] == 3:
            score += dice_roll_score_dict['Three x 2']
        elif dice[2] == 4:
            score += dice_roll_score_dict['Four x 2']
        elif dice[2] == 5:
            score += dice_roll_score_dict['Five x 2']
        elif dice[2] == 6:
            score += dice_roll_score_dict['Six x 2']
        
        # 1's
        if dice[1] == 3:
            score += dice_roll_score_dict['Three x 1']
        elif dice[1] == 4:
            score += dice_roll_score_dict['Four x 1']
        elif dice[1] == 5:
            score += dice_roll_score_dict['Five x 1']
        elif dice[1] == 6:
            score += dice_roll_score_dict['Six x 1']

        else:
            score += 0
        return score 
        
if __name__ == "__main__":
    game = Game()
    game.play()
