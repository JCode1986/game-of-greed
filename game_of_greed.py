import collections
import random

class Game:

    # print(collections.Counter(result_of_roll))

    def __init__(self, print_func=print, input_func=input):
        self._print = print_func
        self._input = input_func
        self.score = 0
        self.roll = [1, 2, 3, 4, 5, 6]

    def roll_die(self):
        pass

    def calculate_score(self, lst):
        for elem in lst:
            if elem == 1:
                self.score += 100
            elif elem == 5:
                self.score += 50
        return self.score
        
    def bank_score(self):
        pass

    def play(self):
        self._print('Welcome to Game of Greed')
        question = self._input('Wanna play? press y then enter to proceed. ')
        if question == 'y':
            self._print('Great! Check back tomorrow :D')
        else:
            self._print('OK. Maybe another time')

if __name__ == "__main__":
    game = Game()
    game.play()
    game.calculate_score([1, 2, 3, 4, 1, 2])
