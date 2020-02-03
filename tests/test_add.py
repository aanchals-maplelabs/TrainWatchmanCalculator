import pytest
from src import TrainWatchmanCalculator


def test_add():
    assert TrainWatchmanCalculator.add(6, 21) == 27
    assert TrainWatchmanCalculator.add(0, 56) == 56
    assert TrainWatchmanCalculator.add(-9, 9) == 0
    assert TrainWatchmanCalculator.add(-35, -19) == -54
    assert TrainWatchmanCalculator.add(0, 0) == 0