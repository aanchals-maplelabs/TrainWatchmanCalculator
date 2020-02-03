import pytest
from src import TrainWatchmanCalculator


def test_subtract():
    assert TrainWatchmanCalculator.subtract(74, 30) == 44
    assert TrainWatchmanCalculator.subtract(4, 30) == -26
    assert TrainWatchmanCalculator.subtract(-9, -12) == 3
    assert TrainWatchmanCalculator.subtract(26, -24) == 50
    assert TrainWatchmanCalculator.subtract(-63, 220) == -283
