import pytest
from src import TrainWatchmanCalculator
# import sys
# import os
# sys.path.append(os.path.abspath("../"))


def test_add():
    assert TrainWatchmanCalculator.add(6, 21) == 27
    assert TrainWatchmanCalculator.add(0, 56) == 56
    assert TrainWatchmanCalculator.add(-9, 9) == 0
    assert TrainWatchmanCalculator.add(-35, -19) == -54
    assert TrainWatchmanCalculator.add(0, 0) == 0


def test_subtract():
    assert TrainWatchmanCalculator.subtract(74, 30) == 44
    assert TrainWatchmanCalculator.subtract(4, 30) == -26
    assert TrainWatchmanCalculator.subtract(-9, -12) == 3
    assert TrainWatchmanCalculator.subtract(26, -24) == 50
    assert TrainWatchmanCalculator.subtract(-63, 220) == -283


def test_multiply():
    assert TrainWatchmanCalculator.multiply(13, 3) == 39
    assert TrainWatchmanCalculator.multiply(-17, 9) == -153
    assert TrainWatchmanCalculator.multiply(-48, -36) == 1728
    assert TrainWatchmanCalculator.multiply(74, 1) == 74
    assert TrainWatchmanCalculator.multiply(0, 0) == 0


def test_divide():
    assert TrainWatchmanCalculator.divide(112, 8) == 14
    assert TrainWatchmanCalculator.divide(3, 6) == 0.5
    assert TrainWatchmanCalculator.divide(-128, 4) == -32
    assert TrainWatchmanCalculator.divide(-2197, -169) == 13


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_modulo():
    assert TrainWatchmanCalculator.modulo(13, 5) == 3
    assert TrainWatchmanCalculator.modulo(2, 7) == 2
    assert TrainWatchmanCalculator.modulo(0, 8) == 0
    assert TrainWatchmanCalculator.modulo(9, 9) == 0
    assert TrainWatchmanCalculator.modulo(17, 1) == 0


def test_powerof():
    assert TrainWatchmanCalculator.power_of(13, 3) == 2197
    assert TrainWatchmanCalculator.power_of(-17, 2) == 289
    assert TrainWatchmanCalculator.power_of(4, -2) == 0.0625
    assert TrainWatchmanCalculator.power_of(-2, -5) == -0.03125
    assert TrainWatchmanCalculator.power_of(24, 0) == 1

