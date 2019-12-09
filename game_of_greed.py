import collections

class Game:

    dice_roll = ['one', 'two', 'three', 'four', 'five', 'six']
    # print(collections.Counter(dice_roll))

    def __init__(self, print_func=print, input_func=input):
        self._print = print_func
        self._input = input_func

    def play(self):
        self._print('Welcome to Game of Greed')
        question = self._input('Wanna play? ')
        if question == 'y':
            self._print('Great! Check back tomorrow :D')
        else:
            self._print('OK. Maybe another time')

if __name__ == "__main__":
    game = Game()
    game.play()
