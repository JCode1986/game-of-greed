from game_of_greed import Game
import pytest

def test_greeting(sample_play):
    set_scripts(['Welcome to Game of Greed'])

    sample_play.play()


def test_greeting_prompt(sample_play):

    set_scripts(
        ['Welcome to Game of Greed', 'OK. Maybe another time'],
        ['Wanna play? press y then enter to proceed. '],
        []
    )

    sample_play.play()

def test_scoring_ones_and_fives(sample_play):
    actual = sample_play.calculate_score([1, 2, 3, 4, 5, 6])
    expected = 150
    assert actual == expected

def test_scoring_multiple_ones_and_fives(sample_play):
    actual = sample_play.calculate_score([1, 5, 1, 5, 1, 6])
    expected = 400
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
def sample_play():
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
