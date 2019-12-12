from game_of_greed import Game
import pytest
from collections import Counter

def test_greeting(game):
    set_scripts(['Welcome to Game of Greed'])

    game.play()


def test_greeting_prompt(game):

    set_scripts(
        ['Welcome to Game of Greed', 'OK. Maybe another time'],
        ['Wanna play? press y then enter to proceed. '],
        []
    )

    game.play()

def test_zilch(game):
    expected = 0
    actual = game.calculate_score((2,3,4,6,2,3))
    assert actual == expected

# @pytest.mark.skip('pending')
@pytest.mark.parametrize("dice,expected",[
    ((1,), 100),
    ((2,), 0),
    ((3,), 0),
    ((4,), 0),
    ((5,), 50),
    ((6,), 0),
    ((1,1), 200),
    ((2,2), 0),
    ((3,3), 0),
    ((4,4), 0),
    ((5,5), 100),
    ((6,6), 0),
    ((1,1,1,), 1000),
    ((2,2,2,), 200),
    ((3,3,3,), 300),
    ((4,4,4,), 400),
    ((5,5,5,), 500),
    ((6,6,6,), 600),
    ((1,1,1,1), 2000),
    ((2,2,2,2), 400),
    ((3,3,3,3), 600),
    ((4,4,4,4), 800),
    ((5,5,5,5), 1000),
    ((6,6,6,6), 1200),
    ((1,1,1,1,1), 3000),
    ((2,2,2,2,2), 600),
    ((3,3,3,3,3), 900),
    ((4,4,4,4,4), 1200),
    ((5,5,5,5,5), 1500),
    ((6,6,6,6,6), 1800),
    ((1,1,1,1,1,1), 4000),
    ((2,2,2,2,2,2), 800),
    ((3,3,3,3,3,3), 1200),
    ((4,4,4,4,4,4), 1600),
    ((5,5,5,5,5,5), 2000),
    ((6,6,6,6,6,6), 2400),
    ((1,2,3,4,5,6), 1500),
    ((1,1,2,2,3,3), 1500),
    ((6,6,6,1), 700),
    ((5,5,5,1,1,1), 1500),
    ((6,6,6,1,1,3), 800),
    ((1,2,3,4,5,6), 1500),
    ((1,1,5,5,5,5), 1200),
    ((2,3,4,6,2,3), 0)

])
def test_calculate_score(game, dice, expected):
    actual = game.calculate_score(dice)
    assert actual == expected

def test_calculate_score_simple():
    game = Game()
    actual = game.calculate_score((1,2))
    expected = 100
    assert expected == actual

@pytest.mark.parametrize("keepers,expected",[
    ((6,6,6,1), 700),
    ((6,6,6,1,1,3), 800),
])
def test_calculate_score_fancy(game, keepers, expected):
    actual = game.calculate_score(keepers)
    assert actual == expected


#################################################
## Below code is for helping out tests above ####
#################################################

scripts = {
    'prints' : [],
    'prompts' : [],
    'inputs' : [],
}

@pytest.fixture()
def game():
    play = Game(mock_print, mock_input)
    return play

def set_scripts(prints=[], prompts=[],inputs=[]):
    scripts['prints'] = prints
    scripts['prompts'] = prompts
    scripts['inputs'] = inputs

def mock_print(msg, *args):
    if len(scripts['prints']):
        assert scripts['prints'].pop(0) == msg


def mock_input(prompt, *args):

    if len(scripts['prompts']):
        assert prompt == scripts['prompts'].pop(0)

    if len(scripts['inputs']):
        return scripts['inputs'].pop(0)
