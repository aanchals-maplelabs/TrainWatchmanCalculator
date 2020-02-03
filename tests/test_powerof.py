import pytest
from src import TrainWatchmanCalculator


def test_powerof():
    assert TrainWatchmanCalculator.power_of(13, 3) == 2197
    assert TrainWatchmanCalculator.power_of(-17, 2) == 289
    assert TrainWatchmanCalculator.power_of(4, -2) == 0.0625
    assert TrainWatchmanCalculator.power_of(-2, -5) == -0.03125
    assert TrainWatchmanCalculator.power_of(24, 0) == 1
