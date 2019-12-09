from game_of_greed import Game
import pytest

def test_greeting(sample_play):
    set_scripts(['Welcome to Game of Greed'])

    sample_play.dine()
