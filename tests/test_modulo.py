import pytest
from src import TrainWatchmanCalculator


def test_modulo():
    assert TrainWatchmanCalculator.modulo(13, 5) == 3
    assert TrainWatchmanCalculator.modulo(2, 7) == 2
    assert TrainWatchmanCalculator.modulo(0, 8) == 0
    assert TrainWatchmanCalculator.modulo(9, 9) == 0
    assert TrainWatchmanCalculator.modulo(17, 1) == 0
