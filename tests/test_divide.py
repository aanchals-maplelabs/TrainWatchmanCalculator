import pytest
from src import TrainWatchmanCalculator


def test_divide():
    assert TrainWatchmanCalculator.divide(112, 8) == 14
    assert TrainWatchmanCalculator.divide(3, 6) == 0.5
    assert TrainWatchmanCalculator.divide(-128, 4) == -32
    assert TrainWatchmanCalculator.divide(-2197, -169) == 13


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
