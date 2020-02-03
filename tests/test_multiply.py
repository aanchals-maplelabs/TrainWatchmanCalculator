import pytest
from src import TrainWatchmanCalculator


def test_multiply():
    assert TrainWatchmanCalculator.multiply(13, 3) == 39
    assert TrainWatchmanCalculator.multiply(-17, 9) == -153
    assert TrainWatchmanCalculator.multiply(-48, -36) == 1728
    assert TrainWatchmanCalculator.multiply(74, 1) == 74
    assert TrainWatchmanCalculator.multiply(0, 0) == 0
